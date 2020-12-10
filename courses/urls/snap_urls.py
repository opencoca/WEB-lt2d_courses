from django.conf.urls import url
from ..views import (SnapListView, SnapCreateView, SnapDetailView,
                     SnapUpdateView, SnapDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(SnapCreateView.as_view()),
        name="snap_create"),

    url(r'^(?P<slug>[-\w]+)/update/$',
        login_required(SnapUpdateView.as_view()),
        name="snap_update"),

    url(r'^(?P<slug>[-\w]+)/delete/$',
        login_required(SnapDeleteView.as_view()),
        name="snap_delete"),

    url(r'^(?P<slug>[-\w]+)/$',
        SnapDetailView.as_view(),
        name="snap_detail"),

    url(r'^$',
        SnapListView.as_view(),
        name="snap_list"),
]
