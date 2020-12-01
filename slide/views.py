import json
from django.shortcuts import get_object_or_404, render
from .models import Slideshow

def index(request):
    latest_slideshow_list = Slideshow.objects.order_by('-date_published')[:5]
    context = {'latest_slideshow_list': latest_slideshow_list}
    return render(request, 'remark/index.html', context) # TODO get from site wide config

def show(request, slug):
    slideshow = get_object_or_404(Slideshow, slug=slug)

    options = slideshow.user.profile.options
    if options is None:
        options = {}

    try:
        options.update(slideshow.options)
    except TypeError:
        pass

    engine = options.get('engine', 'remark').replace('../', '') # TODO get from site wide config

    slideshow.options = options

    try:
        engine_options = options[engine]
    except KeyError:
        engine_options = {}

    return render(
        request,
        f'{engine}/show.html',
        {
            'slideshow': slideshow,
            'options': json.dumps(engine_options),
        }
    )
