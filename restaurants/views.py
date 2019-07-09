from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
	return HttpResponse("<h1> Hello</h1>")

def any_thing(request):
	return render(request,"any_thing.html")