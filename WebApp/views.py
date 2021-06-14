from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Sample(request):
    return HttpResponse("<h1>.................Docker World is so interesting...............</h1>")