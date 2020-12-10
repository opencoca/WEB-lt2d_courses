from django.conf.urls import url
from ..views import (LessionListView, LessionCreateView, LessionDetailView,
                     LessionUpdateView, LessionDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(LessionCreateView.as_view()),
        name="lession_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(LessionUpdateView.as_view()),
        name="lession_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(LessionDeleteView.as_view()),
        name="lession_delete"),

    url(r'^(?P<pk>\d+)/$',
        LessionDetailView.as_view(),
        name="lession_detail"),

    url(r'^$',
        LessionListView.as_view(),
        name="lession_list"),
]
