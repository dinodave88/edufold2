from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'edufold/index.html')

def app1(request):
    return render(request, 'edufold/app1.html')

