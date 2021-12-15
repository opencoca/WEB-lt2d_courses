from django.urls import path
from ..views import (SyllabusListView, SyllabusCreateView, SyllabusDetailView,
                     SyllabusUpdateView, SyllabusDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('create/',  # NOQA
        login_required(SyllabusCreateView.as_view()),
        name="syllabus_create"),

    path('<slug:slug>/update/',
        login_required(SyllabusUpdateView.as_view()),
        name="syllabus_update"),

    path(r'<slug:slug>/delete/',
        login_required(SyllabusDeleteView.as_view()),
        name="syllabus_delete"),

    path(r'<slug:slug>/',
        SyllabusDetailView.as_view(),
        name="syllabus_detail"),

    path(r'',
        SyllabusListView.as_view(),
        name="syllabus_list"),
]
