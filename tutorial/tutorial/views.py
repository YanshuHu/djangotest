from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Home page! hi ihsan. whats up')
def home_page(request):
    return render(request, 'home.html')
