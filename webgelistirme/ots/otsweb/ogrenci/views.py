from django.shortcuts import render
from django.http import HttpResponse

def ogrenci(request):
    return HttpResponse("Şuanda öğrenci sayfasındasınız.")


