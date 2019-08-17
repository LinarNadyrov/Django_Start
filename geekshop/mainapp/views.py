from django.shortcuts import render
from .models import ProductCategory, Product

def main (request):
    return render(request, 'mainapp/index.html')

#def products (request):
#    context = {'username': 'moscow', 'products': ['Кошка', 'Медведь']}
#    return render(request, 'mainapp/products.html', context=context)

def contact (request):
    return render(request, 'mainapp/contacts.html')

def products (request):
    title = 'продукты'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/products.html', content)

