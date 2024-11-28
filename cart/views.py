from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from cart.models import Cart
from survey_data.models import DogSurvey
from django.contrib.auth.decorators import login_required
from user.models import User



def cart_items(request):
    data = Cart.objects.select_related('product_id', 'user').all()

    total_price = 0 

    for item in data:
        total_price += item.count * item.product_id.price
        
    return render(request, 'cart/cart_items.html', {'data': data,  'total_price': total_price})

@login_required
def add_to_cart(request, product_id, user):
    survey = DogSurvey.objects.filter(사료_코드=product_id).first()
    if survey:
        product = survey.as_product()
        user = get_object_or_404(User, pk=user)

        existing_cart_item = Cart.objects.filter(product_id=product, user=user).first()

        if existing_cart_item:
            existing_cart_item.count += 1
            existing_cart_item.save()
        else:
            Cart.objects.create(product_id=product, user=user, count=1)

    return HttpResponseRedirect(reverse('cart_items'))




@login_required
def delete_from_cart(request, cart_id):
    print('delete_from_cart 뷰가 호출되었습니다.')  # 디버깅 코드
    print('cart_id:', cart_id)
    item = get_object_or_404(Cart, cart_id=cart_id)  # 수정된 코드
    print('삭제할 상품:', item.product_id.name)  # 디버깅 코드
    
    try:
        item.delete()
        print('상품이 삭제되었습니다')  # 디버깅 코드
    except Exception as e:
        print('상품 삭제 중 오류 발생:', e)  # 디버깅 코드

    # 아이템이 실제로 삭제되었는지 확인하는 코드
    try:
        item = Cart.objects.get(cart_id=cart_id)
        print('상품이 여전히 존재합니다:', item.product_id.name)  # 디버깅 코드
    except Cart.DoesNotExist:
        print('상품이 성공적으로 삭제되었습니다.')  # 디버깅 코드
        
    return HttpResponseRedirect(reverse('cart_items'))