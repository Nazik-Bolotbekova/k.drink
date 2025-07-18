from django.urls import path

from apps.drinks.views import index_view

urlpatterns = [
    path('index/',index_view)
]