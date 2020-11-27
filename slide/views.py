from django.shortcuts import get_object_or_404, render

from .models import Slideshow

def index(request):
    latest_slideshow_list = Slideshow.objects.order_by('-date_published')[:5]
    context = {'latest_slideshow_list': latest_slideshow_list}
    return render(request, 'slide/index.html', context)

def show(request, slug):
    slideshow = get_object_or_404(Slideshow, slug=slug)
    return render(request, 'slide/show.html', {'slideshow': slideshow})
