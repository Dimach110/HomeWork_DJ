from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = request.GET.get('order', 'group') # 'group' -  указано значение по умолчанию
    students = Student.objects.prefetch_related('teachers').order_by(ordering).all()
    context = {
        'object_list': students,
    }
    return render(request, template, context)

def teachers_list(request):
    template = 'school/teachers_list.html'
    ordering = request.GET.get('order', 'name')
    teachers = Teacher.objects.prefetch_related('students').order_by(ordering).all()
    context = {
        'object_list': teachers,
    }
    return render(request, template, context)


