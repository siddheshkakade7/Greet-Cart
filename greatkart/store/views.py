from cart.models import CartItem
from cart.views import _cart_id
from category.models import Category
from django.shortcuts import get_object_or_404, render

from .models import Product


def products_by_category(request, category_name=None):
    # Retrieve the category based on the slug
    category = get_object_or_404(Category, slug=category_name)
    
    # Retrieve products related to the selected category
    products = Product.objects.filter(category=category)
     # field name in model
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'products_by_category.html', context)


def store(request, category_name=None):
    products = Product.objects.all().filter(is_available=True)
    products_count = products.count()
    category = Category.objects.all() 
    if category_name:
        categories = get_object_or_404(Category, slug=category_name)
        products = Product.objects.all().filter(category=categories)
        products_count = products.count()

    context = {'products': products, 'products_count': products_count,'categories': category}
    return render(request, 'store.html', context)


def product_detail(request, category_name=None, product_name=None):
    try:
        single_product = Product.objects.get(category__slug=category_name, slug=product_name)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    context = {'single_product': single_product,
               'in_cart': in_cart}
    return render(request, 'product_detail.html', context)
