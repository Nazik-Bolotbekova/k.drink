from django import forms
from .models import DrinkCategory, Review

class DrinkCategoryForm(forms.ModelForm):
    class Meta:
        model = DrinkCategory
        fields = ['name', 'description']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['email','fio','review','rating']

