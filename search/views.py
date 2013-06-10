from datetime import date


from django.http import HttpResponse, Http404
from django.conf import settings
from django.views.generic import ListView, DetailView
from django.views.generic.edit import BaseUpdateView
from django.views.generic.dates import DayArchiveView, TodayArchiveView


from .models import Search


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        exclude = ('hashtag', )

class SearchCreateView:
	model = Search
	form_class = SearchForm
    template_name = 'search/search.html' 
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        form.instance.hashtag = self.request.hashtag
        return super(SearchCreateView, self).form_valid(form)