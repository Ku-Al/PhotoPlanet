from datetime import date


from django.http import HttpResponse, Http404
from django.conf import settings
from django.views.generic import ListView, DetailView
from django.views.generic.edit import BaseUpdateView
from django.views.generic.dates import DayArchiveView, TodayArchiveView


from .models import Photo


# TODO: refactor! this is duplicated in load_photos.py management command
LARGE_MEDIA_MAX_ID = 100000000000000000
MEDIA_COUNT = 20
#MEDIA_TAG = 'donetsk'
PHOTOS_PER_PAGE = 10


class HomePhotosListView(TodayArchiveView):
    queryset = Photo.objects.filter(
        vote_count__gt=0).order_by('-vote_count', '-like_count').all()
    date_field = "created_time"
    allow_empty = True
    paginate_by = 10
    context_object_name = 'photos'

class AllPhotosListView(ListView):
    model = Photo
    queryset = Photo.objects.order_by('-created_time').all()
    template_name = 'photoplanet/all.html'  # default is app_name/model_list.html
    context_object_name = 'photos'  # default is object_list
    paginate_by = 10


    
