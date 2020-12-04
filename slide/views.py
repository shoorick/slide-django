import json
from django.shortcuts import get_object_or_404, render
from .models import Slideshow

'''
Make list of available slideshows
'''
def index(request):
    latest_slideshow_list = Slideshow.objects.order_by('-date_published')[:5]
    context = {'latest_slideshow_list': latest_slideshow_list}
    return render(request, 'remark/index.html', context) # TODO get from site wide config

'''
Show certain slideshow identified by slug
'''
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

    if engine == 'cleaver':
        slides, cleaver_options = slideshow.parse_cleaver_slides()
        default_cleaver_options = {'controls': True, 'progress': True, 'encoding': 'utf-8'}
        options = {**default_cleaver_options, **options, **cleaver_options}
        slideshow.slides = slides

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
