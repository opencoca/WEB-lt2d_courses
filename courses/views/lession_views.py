from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Lession
from ..forms import LessionForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class LessionListView(ListView):
    model = Lession
    template_name = "courses/lession_list.html"
    paginate_by = 20
    context_object_name = "lession_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(LessionListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LessionListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LessionListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(LessionListView, self).get_queryset()

    def get_allow_empty(self):
        return super(LessionListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(LessionListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(LessionListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(LessionListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(LessionListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(LessionListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(LessionListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LessionListView, self).get_template_names()


class LessionDetailView(DetailView):
    model = Lession
    template_name = "courses/lession_detail.html"
    context_object_name = "lession"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(LessionDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LessionDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LessionDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LessionDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(LessionDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(LessionDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LessionDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LessionDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LessionDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LessionDetailView, self).get_template_names()


class LessionCreateView(CreateView):
    model = Lession
    form_class = LessionForm
    # fields = ['title', 'subtitle', 'order']
    template_name = "courses/lession_create.html"
    success_url = reverse_lazy("lession_list")

    def __init__(self, **kwargs):
        return super(LessionCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(LessionCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LessionCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LessionCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(LessionCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LessionCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LessionCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LessionCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(LessionCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LessionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LessionCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(LessionCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LessionCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:lession_detail", args=(self.object.pk,))


class LessionUpdateView(UpdateView):
    model = Lession
    form_class = LessionForm
    # fields = ['title', 'subtitle', 'order']
    template_name = "courses/lession_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "lession"

    def __init__(self, **kwargs):
        return super(LessionUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LessionUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LessionUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LessionUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LessionUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(LessionUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(LessionUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(LessionUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LessionUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LessionUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LessionUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(LessionUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LessionUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LessionUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LessionUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LessionUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LessionUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:lession_detail", args=(self.object.pk,))


class LessionDeleteView(DeleteView):
    model = Lession
    template_name = "courses/lession_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "lession"

    def __init__(self, **kwargs):
        return super(LessionDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LessionDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(LessionDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(LessionDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LessionDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(LessionDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(LessionDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LessionDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LessionDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LessionDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LessionDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:lession_list")
