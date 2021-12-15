from django.urls import path
from ..views import (LessionListView, LessionCreateView, LessionDetailView,
                     LessionUpdateView, LessionDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('^create/',  # NOQA
        login_required(LessionCreateView.as_view()),
        name="lession_create"),

    path('<int:pk>/update/',
        login_required(LessionUpdateView.as_view()),
        name="lession_update"),

    path('<int:pk>/delete/',
        login_required(LessionDeleteView.as_view()),
        name="lession_delete"),

    path('<int:pk>/',
        LessionDetailView.as_view(),
        name="lession_detail"),

    path('',
        LessionListView.as_view(),
        name="lession_list"),
]
