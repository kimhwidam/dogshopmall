from django.shortcuts import render, redirect
from dog.forms import DogRecommendationForm
from tensorflow.keras.models import load_model
from survey_data.models import DogSurvey
import numpy as np
from sklearn.preprocessing import LabelEncoder

model = load_model('Final_NCF2.h5')

label_encoders = {}
fields_to_encode = ['색상', '크기', '연령대', '상태', '견종']

for field in fields_to_encode:
    encoder = LabelEncoder()
    encoder.fit(DogSurvey.objects.values_list(field, flat=True))
    label_encoders[field] = encoder

def recommendation_view(request):
    if request.method == 'POST':
        form = DogRecommendationForm(request.POST)
        if form.is_valid():
            return redirect('recommendation_results') 
    else:
        form = DogRecommendationForm()

    return render(request, 'dog/recommendation.html', {'form': form})

def recommendation_results(request):
    if request.method == 'POST':
        color = request.POST.get('색상')
        species = request.POST.get('견종')
        size = request.POST.get('크기')
        state = request.POST.get('상태')
        age = request.POST.get('연령대')

        color_encoded = label_encoders['색상'].transform([color])[0]
        species_encoded = label_encoders['견종'].transform([species])[0]
        size_encoded = label_encoders['크기'].transform([size])[0]
        state_encoded = label_encoders['상태'].transform([state])[0]
        age_encoded = label_encoders['연령대'].transform([age])[0]

        all_dog_foods = DogSurvey.objects.values('CP', 'CF', 'CR', 'CB', 'CA', 'PO', 'WA', '사료', '브랜드', '사료_코드').distinct()

        input_data = {
            '색상': [color_encoded],
            '견종': [species_encoded],
            '크기': [size_encoded],
            '상태': [state_encoded],
            '연령대': [age_encoded],
        }

        predictions = []
        seen_combinations = set()  # 중복 방지를 위한 세트

        for dog_food in all_dog_foods:
            input_data.update({field: [float(dog_food[field])] for field in ['CP', 'CF', 'CR', 'CB', 'CA', 'PO', 'WA']})
            prediction = model.predict([np.array(input_data[field]) for field in input_data])
            predicted_class = int(np.argmax(prediction, axis=1)[0])
            
            food_code = dog_food['사료_코드']  # 사용할 고유한 식별자 선택

            if food_code not in seen_combinations:
                seen_combinations.add(food_code)  # 중복 방지를 위해 코드를 세트에 추가

                survey_info = DogSurvey.objects.filter(사료_코드=food_code).first()

                if survey_info:
                    predictions.append({
                        '사료': survey_info.사료,
                        '브랜드': survey_info.브랜드,
                        '사료_코드': survey_info.사료_코드,
                        'CP': dog_food['CP'],
                        'CF': dog_food['CF'],
                        'CR': dog_food['CR'],
                        'CB': dog_food['CB'],
                        'CA': dog_food['CA'],
                        'PO': dog_food['PO'],
                        'WA': dog_food['WA'],
                        'predicted_class': predicted_class,
                    })

        sorted_predictions = sorted(predictions, key=lambda x: x['predicted_class'], reverse=True)
        top_5_foods_info = sorted_predictions[:5]

        return render(request, 'dog/food_recommendation.html', {'top_5_foods_information': top_5_foods_info})

    else:
        form = DogRecommendationForm()
        return render(request, 'dog/recommendation.html', {'form': form})
