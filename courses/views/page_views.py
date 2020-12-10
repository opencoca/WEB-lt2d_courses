from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Page
from ..forms import PageForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class PageListView(ListView):
    model = Page
    template_name = "courses/page_list.html"
    paginate_by = 20
    context_object_name = "page_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PageListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PageListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PageListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PageListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PageListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PageListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PageListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PageListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PageListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PageListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PageListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PageListView, self).get_template_names()


class PageDetailView(DetailView):
    model = Page
    template_name = "courses/page_detail.html"
    context_object_name = "page"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PageDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PageDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PageDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PageDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PageDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PageDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PageDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PageDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PageDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PageDetailView, self).get_template_names()


class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'subtitle', 'order']
    template_name = "courses/page_create.html"
    success_url = reverse_lazy("page_list")

    def __init__(self, **kwargs):
        return super(PageCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PageCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PageCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PageCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PageCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PageCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PageCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PageCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PageCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PageCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PageCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PageCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PageCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:page_detail", args=(self.object.pk,))


class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'subtitle', 'order']
    template_name = "courses/page_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "page"

    def __init__(self, **kwargs):
        return super(PageUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PageUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PageUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PageUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PageUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PageUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PageUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PageUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PageUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PageUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PageUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PageUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PageUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PageUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PageUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PageUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PageUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:page_detail", args=(self.object.pk,))


class PageDeleteView(DeleteView):
    model = Page
    template_name = "courses/page_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "page"

    def __init__(self, **kwargs):
        return super(PageDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PageDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PageDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PageDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PageDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PageDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PageDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PageDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PageDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PageDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PageDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("courses:page_list")
