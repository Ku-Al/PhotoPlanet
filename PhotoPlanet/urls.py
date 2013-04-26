from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'PhotoPlanet.views.home', name='home'),
    url(
        r'^all/',
        TemplateView.as_view(template_name="PhotoPlanet/all.html"),
        name='all'),
    url(r'^feedback/', include('feedback.urls'))
    url(r'^search/', include('search.urls'))
)
