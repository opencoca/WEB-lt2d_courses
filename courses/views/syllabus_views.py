from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Syllabus
from ..forms import SyllabusForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class SyllabusListView(ListView):
    model = Syllabus
    template_name = "courses/syllabus_list.html"
    paginate_by = 20
    context_object_name = "syllabus_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(SyllabusListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SyllabusListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SyllabusListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(SyllabusListView, self).get_queryset()

    def get_allow_empty(self):
        return super(SyllabusListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(SyllabusListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(SyllabusListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(SyllabusListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(SyllabusListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(SyllabusListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(SyllabusListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SyllabusListView, self).get_template_names()


class SyllabusDetailView(DetailView):
    model = Syllabus
    template_name = "courses/syllabus_detail.html"
    context_object_name = "syllabus"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(SyllabusDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SyllabusDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SyllabusDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SyllabusDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(SyllabusDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(SyllabusDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SyllabusDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SyllabusDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SyllabusDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SyllabusDetailView, self).get_template_names()


class SyllabusCreateView(CreateView):
    model = Syllabus
    form_class = SyllabusForm
    # fields = ['slug', 'name', 'order']
    template_name = "courses/syllabus_create.html"
    success_url = reverse_lazy("syllabus_list")

    def __init__(self, **kwargs):
        return super(SyllabusCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(SyllabusCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SyllabusCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SyllabusCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(SyllabusCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SyllabusCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SyllabusCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SyllabusCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(SyllabusCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SyllabusCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SyllabusCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(SyllabusCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SyllabusCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:syllabus_detail", args=(self.object.slug,))


class SyllabusUpdateView(UpdateView):
    model = Syllabus
    form_class = SyllabusForm
    # fields = ['slug', 'name', 'order']
    template_name = "courses/syllabus_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "syllabus"

    def __init__(self, **kwargs):
        return super(SyllabusUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SyllabusUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SyllabusUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SyllabusUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SyllabusUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(SyllabusUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(SyllabusUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(SyllabusUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SyllabusUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SyllabusUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SyllabusUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(SyllabusUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SyllabusUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SyllabusUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SyllabusUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SyllabusUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SyllabusUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:syllabus_detail", args=(self.object.slug,))


class SyllabusDeleteView(DeleteView):
    model = Syllabus
    template_name = "courses/syllabus_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "syllabus"

    def __init__(self, **kwargs):
        return super(SyllabusDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SyllabusDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(SyllabusDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(SyllabusDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SyllabusDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(SyllabusDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(SyllabusDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SyllabusDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SyllabusDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SyllabusDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SyllabusDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:syllabus_list")
