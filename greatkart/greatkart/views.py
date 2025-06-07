from category.models import Category
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.all()
    category = Category.objects.all() 
    context = {'products': products, 'categories': category}
    return render(request, 'home1.html', context)



