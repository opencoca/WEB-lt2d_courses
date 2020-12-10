from django.conf.urls import url
from ..views import (PageListView, PageCreateView, PageDetailView,
                     PageUpdateView, PageDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(PageCreateView.as_view()),
        name="page_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PageUpdateView.as_view()),
        name="page_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PageDeleteView.as_view()),
        name="page_delete"),

    url(r'^(?P<pk>\d+)/$',
        PageDetailView.as_view(),
        name="page_detail"),

    url(r'^$',
        PageListView.as_view(),
        name="page_list"),
]
