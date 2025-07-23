from django import forms
from .models import DrinkCategory, Review, Order

class DrinkCategoryForm(forms.ModelForm):
    class Meta:
        model = DrinkCategory
        fields = ['name', 'description']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['email','fio','review','rating']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','city','address','phone_number','payment']

