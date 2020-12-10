from django.conf.urls import include, url

app_name="courses"

urlpatterns = [

    url(r'^syllabus/', include('courses.urls.syllabus_urls')),  # NOQA
    url(r'^courses/', include('courses.urls.course_urls')),
    url(r'^lessions/', include('courses.urls.lession_urls')),
    url(r'^pages/', include('courses.urls.page_urls')),
    url(r'^snaps/', include('courses.urls.snap_urls')),
]
