from django.urls import path
from . import views

urlpatterns = [
    path('',                    views.home,                     name='home'),
    path('about/',              views.about,                    name='about'),
    path('songs/',              views.ArtistList.as_view(),     name='artists_index'),
    path('songs/<int:pk>',      views.ArtistDetail.as_view(),   name='artists_detail'),
    path('songs/create/',       views.ArtistCreate.as_view(),   name='artists_create'),
    path('songs/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artists_update'),
    path('songs/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artists_delete'),
]