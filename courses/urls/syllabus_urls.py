from django.conf.urls import url
from ..views import (SyllabusListView, SyllabusCreateView, SyllabusDetailView,
                     SyllabusUpdateView, SyllabusDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(SyllabusCreateView.as_view()),
        name="syllabus_create"),

    url(r'^(?P<slug>[-\w]+)/update/$',
        login_required(SyllabusUpdateView.as_view()),
        name="syllabus_update"),

    url(r'^(?P<slug>[-\w]+)/delete/$',
        login_required(SyllabusDeleteView.as_view()),
        name="syllabus_delete"),

    url(r'^(?P<slug>[-\w]+)/$',
        SyllabusDetailView.as_view(),
        name="syllabus_detail"),

    url(r'^$',
        SyllabusListView.as_view(),
        name="syllabus_list"),
]
