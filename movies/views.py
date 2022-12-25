from django.shortcuts import render
from models import Movies

# Create your views here.


def movies_list(request):
    all = Movies.objects.all()
    return render(request, 'movies.html', {'data':all})



def movies_movie(request, id):
    movie = Movies.objects(id=id)
    return render(request, 'singel.html', {'data':movie})