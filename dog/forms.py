from django import forms
from survey_data.models import DogSurvey

class DogRecommendationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DogRecommendationForm, self).__init__(*args, **kwargs)

        # Get unique values from the database for each field
        color_choices = DogSurvey.objects.values_list('색상', flat=True).distinct()
        size_choices = DogSurvey.objects.values_list('크기', flat=True).distinct()
        age_choices = DogSurvey.objects.values_list('연령대', flat=True).distinct()
        state_choices = DogSurvey.objects.values_list('상태', flat=True).distinct()
        species_choices = DogSurvey.objects.values_list('견종', flat=True).distinct()

        # Create SelectBox fields with the unique choices
        self.fields['색상'] = forms.ChoiceField(
            choices=[(color, color) for color in color_choices],
            label="색상"
        )
        self.fields['크기'] = forms.ChoiceField(
            choices=[(size, size) for size in size_choices],
            label="크기"
        )
        self.fields['연령대'] = forms.ChoiceField(
            choices=[(age, age) for age in age_choices],
            label="연령대"
        )
        self.fields['상태'] = forms.ChoiceField(
            choices=[(state, state) for state in state_choices],
            label="상태"
        )
        self.fields['견종'] = forms.ChoiceField(
            choices=[(species, species) for species in species_choices],
            label="견종"
        )
