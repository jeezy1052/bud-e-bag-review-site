from django import forms
from django.forms import ModelForm
from .models import Reviewer



class ReviewForm(ModelForm):

    
    class Meta():
        model = Reviewer
        fields = ('username', 'strain', 'consumpition_method', 'is_skunk_one', 'is_harsh_two', 'is_fire_three', 'is_hall_of_fame_four', 'image', 'review',)

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Review Name'}),
            'strain':   forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Strain Name'}),
            'consumpition_method': forms.Select(attrs={'class':'form-select'}),
            'is_skunk_one': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_harsh_two': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_fire_three': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_hall_of_fame_four': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'review': forms.Textarea(attrs={'class':'form-control', 'cols': 200, 'rows': 3, 'placeholder': 'Leave Review'}),
        }

        

