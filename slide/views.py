from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from .models import Slideshow

def index(request):
    latest_slideshow_list = Slideshow.objects.order_by('-date_published')[:5]
    context = {'latest_slideshow_list': latest_slideshow_list}
    return render(request, 'slide/index.html', context)

def show(request, slug):
    slideshow = Slideshow.objects.filter(slug=slug).first()
    if slideshow:
        return render(request, 'slide/show.html', {'slideshow': slideshow})
    else:
        raise Http404(f'No slideshow found at {slug}')
