from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the Studio index.")

class VideoDetailView(DetailView):
    queryset = Video.objects.all()

class VideoListView(ListView):

    paginate_by = 10  # <app>/<modelname>_list.html

    def get_queryset(self, *args, **kwargs):
        qs = Video.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(Video_Description__icontains=query) | Q(videofile__icontains=query))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(VideoListView, self).get_context_data(*args, **kwargs)
        return context



