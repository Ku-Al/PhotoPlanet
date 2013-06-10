from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from .views import (
    HomePhotosListView, AllPhotosListView)

urlpatterns = patterns(
    'PhotoPlanet.views',
    url(r'^$', HomePhotosListView.as_view(), name='home'),
    url(r'^all/$', AllPhotosListView.as_view(), name='all'),
    url(r'^about/$', TemplateView.as_view(template_name='PhotoPlanet/about.html'), name='about'),
)

urlpatterns += patterns(
    '',   
    url(r'^feedback/', include('feedback.urls')),
    url(r'^search/', include('search.urls'))
)
