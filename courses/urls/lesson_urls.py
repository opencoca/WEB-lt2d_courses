from django.urls import path
from ..views import (LessonListView, LessonCreateView, LessonDetailView,
                     LessonUpdateView, LessonDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('^create/',  # NOQA
        login_required(LessonCreateView.as_view()),
        name="lesson_create"),

    path('<int:pk>/update/',
        login_required(LessonUpdateView.as_view()),
        name="lesson_update"),

    path('<int:pk>/delete/',
        login_required(LessonDeleteView.as_view()),
        name="lesson_delete"),

    path('<int:pk>/',
        LessonDetailView.as_view(),
        name="lesson_detail"),

    path('',
        LessonListView.as_view(),
        name="lesson_list"),
]
