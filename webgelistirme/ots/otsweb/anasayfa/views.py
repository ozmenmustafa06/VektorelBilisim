from django.shortcuts import render
from django.http import HttpResponse

def anasayfa(request):
    return HttpResponse("Web siteme hoş geldiniz.")


