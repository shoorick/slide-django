# from django.shortcuts import render

from django.http import HttpResponse
from .models import Slideshow

def index(request):
    latest_slideshow_list = Slideshow.objects.order_by('-date_published')[:5]
    output = ', '.join([s.name for s in latest_slideshow_list])
    return HttpResponse(output)

def show(request, slug):
    s = Slideshow.objects.filter(slug=slug).first()
    output = f'Slideshow {s.name}' if s else f'No slideshow found at {slug}'
    return HttpResponse(output)
