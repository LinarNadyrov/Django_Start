from django.shortcuts import render

def main (request):
    return render(request, 'mainapp/index.html')

def products (request):
    context = {'username': 'moscow', 'products': ['Кошка', 'Медведь']}
    return render(request, 'mainapp/products.html', context=context)

def contact (request):
    return render(request, 'mainapp/contacts.html')