from django.conf.urls import url
from ..views import (CourseListView, CourseCreateView, CourseDetailView,
                     CourseUpdateView, CourseDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CourseCreateView.as_view()),
        name="course_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CourseUpdateView.as_view()),
        name="course_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CourseDeleteView.as_view()),
        name="course_delete"),

    url(r'^(?P<pk>\d+)/$',
        CourseDetailView.as_view(),
        name="course_detail"),

    url(r'^$',
        CourseListView.as_view(),
        name="course_list"),
]
