from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Course
from ..forms import CourseForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    paginate_by = 20
    context_object_name = "course_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CourseListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CourseListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CourseListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CourseListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CourseListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CourseListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CourseListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CourseListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CourseListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CourseListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CourseListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CourseListView, self).get_template_names()


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CourseDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CourseDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CourseDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CourseDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CourseDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CourseDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CourseDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CourseDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CourseDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CourseDetailView, self).get_template_names()


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    # fields = ['syllabus', 'pub_date', 'order']
    template_name = "courses/course_create.html"
    success_url = reverse_lazy("course_list")

    def __init__(self, **kwargs):
        return super(CourseCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CourseCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CourseCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CourseCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CourseCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CourseCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CourseCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CourseCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CourseCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CourseCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CourseCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CourseCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CourseCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:course_detail", args=(self.object.pk,))


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    # fields = ['syllabus', 'pub_date', 'order']
    template_name = "courses/course_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "course"

    def __init__(self, **kwargs):
        return super(CourseUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CourseUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CourseUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CourseUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CourseUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CourseUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CourseUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CourseUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CourseUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CourseUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CourseUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CourseUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CourseUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CourseUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CourseUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CourseUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CourseUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:course_detail", args=(self.object.pk,))


class CourseDeleteView(DeleteView):
    model = Course
    template_name = "courses/course_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "course"

    def __init__(self, **kwargs):
        return super(CourseDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CourseDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CourseDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CourseDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CourseDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CourseDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CourseDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CourseDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CourseDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CourseDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:course_list")
