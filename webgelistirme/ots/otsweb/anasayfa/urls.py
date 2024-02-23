from django.urls import path
from . import views

urlpatterns = [
    path('anasayfa/', views.anasayfa, name='anasayfa'),
    path('ogrenci/', views.ogrenci, name='ogrenci'),
]
