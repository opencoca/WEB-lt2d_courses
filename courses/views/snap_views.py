from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Snap
from ..forms import SnapForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class SnapListView(ListView):
    model = Snap
    template_name = "courses/snap_list.html"
    paginate_by = 25
    context_object_name = "snap_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(SnapListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SnapListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SnapListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(SnapListView, self).get_queryset()

    def get_allow_empty(self):
        return super(SnapListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(SnapListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(SnapListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(SnapListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(SnapListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(SnapListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(SnapListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SnapListView, self).get_template_names()


class SnapDetailView(DetailView):
    model = Snap
    template_name = "courses/snap_detail.html"
    context_object_name = "snap"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(SnapDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SnapDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SnapDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SnapDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(SnapDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(SnapDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SnapDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SnapDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SnapDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SnapDetailView, self).get_template_names()

class SnapManifestView(SnapDetailView):
    template_name = "courses/snap_manifest.json"

class SnapSWView(SnapDetailView):
    template_name = "courses/snap_sw.js"
    content_type='text/javascript'

class SnapCreateView(CreateView):
    model = Snap
    form_class = SnapForm
    # fields = ['title', 'subtile', 'description', 'slug', 'file']
    template_name = "courses/snap_create.html"
    success_url = reverse_lazy("snap_list")

    def __init__(self, **kwargs):
        return super(SnapCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(SnapCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SnapCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SnapCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(SnapCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SnapCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SnapCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SnapCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(SnapCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SnapCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SnapCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(SnapCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SnapCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:snap_detail", args=(self.object.slug,))


class SnapUpdateView(UpdateView):
    model = Snap
    form_class = SnapForm
    #fields = ['title', 'subtile', 'description', 'slug', 'file','http_only']
    template_name = "courses/snap_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "snap"

    def __init__(self, **kwargs):
        return super(SnapUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SnapUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SnapUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SnapUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SnapUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(SnapUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(SnapUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(SnapUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SnapUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SnapUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SnapUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(SnapUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SnapUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SnapUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SnapUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SnapUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SnapUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:snap_detail", args=(self.object.slug,))


class SnapDeleteView(DeleteView):
    model = Snap
    template_name = "courses/snap_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "snap"

    def __init__(self, **kwargs):
        return super(SnapDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SnapDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(SnapDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(SnapDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SnapDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(SnapDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(SnapDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SnapDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SnapDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SnapDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SnapDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:snap_list")
