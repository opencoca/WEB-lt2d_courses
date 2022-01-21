from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Lesson
from ..forms import LessonForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class LessonListView(ListView):
    model = Lesson
    template_name = "courses/lesson_list.html"
    paginate_by = 20
    context_object_name = "lesson_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(LessonListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LessonListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LessonListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(LessonListView, self).get_queryset()

    def get_allow_empty(self):
        return super(LessonListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(LessonListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(LessonListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(LessonListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(LessonListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(LessonListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(LessonListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LessonListView, self).get_template_names()


class LessonDetailView(DetailView):
    model = Lesson
    template_name = "courses/lesson_detail.html"
    context_object_name = "lesson"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(LessonDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LessonDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LessonDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LessonDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(LessonDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(LessonDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LessonDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LessonDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LessonDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LessonDetailView, self).get_template_names()


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    # fields = ['title', 'subtitle', 'order']
    template_name = "courses/lesson_create.html"
    success_url = reverse_lazy("lesson_list")

    def __init__(self, **kwargs):
        return super(LessonCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(LessonCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LessonCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LessonCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(LessonCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LessonCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LessonCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LessonCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(LessonCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LessonCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LessonCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(LessonCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LessonCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:lesson_detail", args=(self.object.pk,))


class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm
    # fields = ['title', 'subtitle', 'order']
    template_name = "courses/lesson_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "lesson"

    def __init__(self, **kwargs):
        return super(LessonUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LessonUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LessonUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LessonUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LessonUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(LessonUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(LessonUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(LessonUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LessonUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LessonUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LessonUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(LessonUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LessonUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LessonUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LessonUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LessonUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LessonUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:lesson_detail", args=(self.object.pk,))


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = "courses/lesson_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "lesson"

    def __init__(self, **kwargs):
        return super(LessonDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LessonDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(LessonDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(LessonDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LessonDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(LessonDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(LessonDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LessonDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LessonDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LessonDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LessonDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:lesson_list")
