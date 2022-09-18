from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = request.GET.get('order', 'group') # 'group' -  указано значение по умолчанию
    # print(ordering)
    # if not ordering:
    #     ordering = 'group'
    print(ordering)
    students = Student.objects.order_by(ordering).all()
    context = {
        'object_list': students,
    }
    return render(request, template, context)
