import json
from django.shortcuts import get_object_or_404, render
from .models import Slideshow

def index(request):
    latest_slideshow_list = Slideshow.objects.order_by('-date_published')[:5]
    context = {'latest_slideshow_list': latest_slideshow_list}
    return render(request, 'slide/index.html', context)

def show(request, slug):
    slideshow = get_object_or_404(Slideshow, slug=slug)
    engine = 'remark' # TODO Replace 'remark' with name of current engine

    options = slideshow.user.profile.options
    if options is None:
        options = {}

    try:
        options.update(slideshow.options)
    except TypeError:
        pass

    slideshow.options = options

    try:
        engine_options = options[engine]
    except KeyError:
        engine_options = {}

    return render(request, 'slide/show.html', {'slideshow': slideshow, 'options': json.dumps(engine_options)})
