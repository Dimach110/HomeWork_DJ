
from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_list = request.GET.get('sort')
    if sort_list == 'name':
        sort = 'name'
    elif sort_list == 'min_price':
        sort = 'price'
    elif sort_list == 'max_price':
        sort = '-price'
    else:
        sort = 'release_date'
    context = {
        'phones': Phone.objects.all().order_by(sort)
    }
    print(Phone.name)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    products = Phone.objects.filter(slug=slug)
    for product in products:
        context = {'phone': product}
    return render(request, template, context)

