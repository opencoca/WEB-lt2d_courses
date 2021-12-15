from django.urls import path
from ..views import (PageListView, PageCreateView, PageDetailView,
                     PageUpdateView, PageDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('create/',  # NOQA
        login_required(PageCreateView.as_view()),
        name="page_create"),

    path('<int:pk>/update/',
        login_required(PageUpdateView.as_view()),
        name="page_update"),

    path('<int:pk>/delete/',
        login_required(PageDeleteView.as_view()),
        name="page_delete"),

    path('<int:pk>',
        PageDetailView.as_view(),
        name="page_detail"),

    path('',
        PageListView.as_view(),
        name="page_list"),
]
