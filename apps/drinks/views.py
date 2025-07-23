
from django.shortcuts import render,redirect
from .service import get_weather
from django.views.generic import View, DetailView

from .models import Drink, DrinkCategory
from .forms import ReviewForm, OrderForm


# def index_view(request):
#     return render(request,'index.html')

# def product_view(request):
#     return render(request,'product.html')

class DrinkView(View):
    def get(self,request):
        drinks = Drink.objects.all()
        categories = DrinkCategory.objects.all()
        return render(request,'product.html',{'drinks':drinks,'categories':categories})

def index_view(request):
        drinks = Drink.objects.all()
        weather_data = get_weather("Bishkek") if request.user.is_authenticated else None
        return render(request, "index.html", {
            "weather": weather_data,
            "drinks": drinks
        })

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'create_review.html', {'form': form})
    else:
        form = ReviewForm()
        return render(request, 'create_review.html', {'form': form})

# def order_view(request,drink_id):
#     drink = Drink.objects.get(id=drink_id)
#     return render(request,'order.html',{'drink':drink})

def order_success_view(request):
    return render(request, 'order_success.html')

def order_view2(request,drink_id):
    drink = Drink.objects.get(id=drink_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = drink.price
            order.save()
            return redirect('order_success')


        else:
            return render(request,'order.html',{"form":form,'drink':drink})
    else:
        form = OrderForm()
        return render(request, 'order.html', {'form': form,'drink':drink})


class DrinkDetailView(DetailView):
    model = Drink
    template_name = 'detail.html'
    context_object_name = 'drink'