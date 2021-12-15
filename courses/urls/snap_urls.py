from django.urls import path
from ..views import (SnapListView, SnapCreateView, SnapDetailView,
                     SnapUpdateView, SnapDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('create/',  # NOQA
        login_required(SnapCreateView.as_view()),
        name="snap_create"),

    path('<slug:slug>/update/',
        login_required(SnapUpdateView.as_view()),
        name="snap_update"),

    path('<slug:slug>/delete/',
        login_required(SnapDeleteView.as_view()),
        name="snap_delete"),

    path('<slug:slug>',
        SnapDetailView.as_view(),
        name="snap_detail"),

    path('',
        SnapListView.as_view(),
        name="snap_list"),
]
