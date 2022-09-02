import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def quantity_dish(dish, n):
    dish_quan = {}
    for d, q in DATA[dish].items():
        try:
            dish_quan[d] = q*int(n)
        except:
            dish_quan[d] = q
    return dish_quan

def omlet(request):
    template_name = 'calculator/index.html'
    n = request.GET.get('servings', 1)
    context = {
        'recipe': quantity_dish('omlet', n)
    }
    return render(request, template_name, context)

def pasta(request):
    template_name = 'calculator/index.html'
    n = request.GET.get('servings', 1)
    context = {
        'recipe': quantity_dish('pasta', n)
        }
    return render(request, template_name, context)

def buter(request):
    template_name = 'calculator/index.html'
    n = request.GET.get('servings', 1)
    context = {
        'recipe': quantity_dish('buter', n)
    }
    return render(request, template_name, context)


