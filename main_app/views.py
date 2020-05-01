from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artist

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class ArtistList(ListView):
  model = Artist

  def get_queryset(self):
    return Artist.objects.all()


class ArtistDetail(DetailView):
  model = Artist


class ArtistCreate(CreateView):
  model = Artist
  fields = '__all__' 


class ArtistUpdate(UpdateView):
  model = Artist
  fields = ['name', 'description']

class ArtistDelete(DeleteView):
  model = Artist
  success_url = '/songs/'