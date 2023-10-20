from django.http import HttpResponse
from django.shortcuts import render, redirect
from movieapp.models import Movie
from .forms import Movieform


# Create your views here.
def demo(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index(demo).html',context)
    #return HttpResponse("Hello an Demo")

def details(request,movie_id):

    mov=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movf':mov})
    # return HttpResponse("Movie Num : %s" %movie_id)

def add_movie(request):

    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']

        movie_add_database=Movie(name=name,desc=desc,year=year,img=img)
        movie_add_database.save()
    return render(request, "add.html")

def update(request,id):
    movieup=Movie.objects.get(id=id)
    formup=Movieform(request.POST or None,request.FILES,instance=movieup)
    if formup.is_valid():
        formup.save()
        return redirect('/')
    return render(request,'edit.html',{'form':formup,'movie':movieup})


def delete(request,id):
    if request.method=='POST':
        moviedel=Movie.objects.get(id=id)
        moviedel.delete()
        return redirect('/')
    return render(request, 'delete.html')