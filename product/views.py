from django.shortcuts import redirect, render, get_object_or_404
from survey_data.models import DogSurvey
import random
from datetime import timedelta
from django.utils import timezone
from product.models import Review
from datetime import datetime
from product.models import Product
from itertools import groupby

def random_datetime():
    random_date = timezone.now() - timedelta(days=random.randint(1, 365))
    random_time = random_time = timedelta(
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    )
    return random_date + random_time

def product_view(request, brand_code=None):
    brands = DogSurvey.objects.values_list('브랜드_코드', flat=True).distinct()

    selected_brand = brand_code 

    if brand_code:
        dog_surveys = DogSurvey.objects.filter(브랜드_코드=brand_code)
    else:
        dog_surveys = DogSurvey.objects.all()

    unique_surveys = [
        max(group, key=lambda survey: survey.사료_코드)
        for _, group in groupby(sorted(dog_surveys, key=lambda survey: survey.사료_코드), key=lambda survey: survey.사료_코드)
    ]

    products = [survey.as_product() for survey in unique_surveys]

    return render(request, 'product/product_view.html', {'products': products, 'brands': brands, 'selected_brand': selected_brand})


def product_detail(request, product_id):
    survey_data = DogSurvey.objects.filter(사료_코드=product_id).first()
    product_list = [survey_data.as_product()] if survey_data else []

    reviews = []
    
    all_reviews = DogSurvey.objects.filter(사료_코드=product_id)
    for survey in all_reviews:
        review = {
            'rating': int(survey.평점),
            'content': survey.후기,
            'created_at': random_datetime()
        }
        reviews.append(review)

    user_reviews = Review.objects.filter(product_id=product_id, user=request.user)
    for user_review in user_reviews:
        user_review_dict = {
            'rating': user_review.rating,
            'content': user_review.content,
            'created_at': user_review.create_dt 
        }
        reviews.append(user_review_dict)

    return render(request, 'product/product_detail.html', {'product_list': product_list, 'reviews': reviews})


def submit_review(request, product_id):  
    product = get_object_or_404(Product, product_id=product_id) 
    if request.method == 'POST':
        rating = request.POST.get('rating')
        content = request.POST.get('content')

        review = Review(
            user=request.user,  
            product_id=product,  
            rating=rating,
            content=content,
            create_dt=datetime.now()
        )
        review.save()

        return redirect('product_detail', product_id=product_id)