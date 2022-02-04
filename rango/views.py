from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	content = 'Rango says hey there partner!' + '<a href="/rango/about/">About</a>'
	return HttpResponse(content)

def about(request):
	content =  'Rango says here is the about page.' + '<a href="/rango/">Index</a>'
	return HttpResponse(content)