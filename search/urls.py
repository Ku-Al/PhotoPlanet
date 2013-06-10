from django.conf.urls import patterns, url
from search.views import SearchCreateView

urlpatterns = patterns(
    '',
    url(
        r'^$',
        SearchCreateView.as_view(),
        name='search')
)