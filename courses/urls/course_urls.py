from django.urls import path
from ..views import (CourseListView, CourseCreateView, CourseDetailView,
                     CourseUpdateView, CourseDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('create/',  # NOQA
        login_required(CourseCreateView.as_view()),
        name="course_create"),

    path('<int:pk>/update/',
        login_required(CourseUpdateView.as_view()),
        name="course_update"),

    path('<int:pk>/delete/',
        login_required(CourseDeleteView.as_view()),
        name="course_delete"),

    path('<int:pk>/',
        CourseDetailView.as_view(),
        name="course_detail"),

    path('',
        CourseListView.as_view(),
        name="course_list"),
]
