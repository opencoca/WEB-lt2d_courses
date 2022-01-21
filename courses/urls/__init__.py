from django.urls import path
from django.conf.urls import include

app_name="courses"

urlpatterns = [

    path('syllabus/', include('courses.urls.syllabus_urls')),  # NOQA
    path('courses/', include('courses.urls.course_urls')),
    path('lessons/', include('courses.urls.lesson_urls')),
    path('pages/', include('courses.urls.page_urls')),
    path('snaps/', include('courses.urls.snap_urls')),
]
