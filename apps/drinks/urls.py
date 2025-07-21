from django.urls import path

from apps.drinks.views import index_view, DrinkView,create_review,order_view,order_success_view

urlpatterns = [

    path('product/',DrinkView.as_view(),name='product'),
    path('index/', index_view, name='index'),
    path('review/',create_review,name='review'),
    path('order_success/',order_success_view,name='order_success'),
    path('order/<int:drink_id>/',order_view,name='order'),




]