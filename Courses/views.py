from django.shortcuts import render
from.models import Courses

# Create your views here.

def Courses_list(request):
    all = Courses.objects.all()
    return render(request, 'courses.html', {'data':all})


def Courses_detaile(request):
    pass