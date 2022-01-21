from django import forms
from .models import Syllabus, Course, Lession, Page, Snap


class SyllabusForm(forms.ModelForm):

    class Meta:
        model = Syllabus
        fields = ['slug', 'name', 'order']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(SyllabusForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(SyllabusForm, self).is_valid()

    def full_clean(self):
        return super(SyllabusForm, self).full_clean()

    def clean_slug(self):
        slug = self.cleaned_data.get("slug", None)
        return slug

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_order(self):
        order = self.cleaned_data.get("order", None)
        return order

    def clean(self):
        return super(SyllabusForm, self).clean()

    def validate_unique(self):
        return super(SyllabusForm, self).validate_unique()

    def save(self, commit=True):
        return super(SyllabusForm, self).save(commit)


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['syllabus', 'pub_date', 'order']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CourseForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CourseForm, self).is_valid()

    def full_clean(self):
        return super(CourseForm, self).full_clean()

    def clean_syllabus(self):
        syllabus = self.cleaned_data.get("syllabus", None)
        return syllabus

    def clean_pub_date(self):
        pub_date = self.cleaned_data.get("pub_date", None)
        return pub_date

    def clean_order(self):
        order = self.cleaned_data.get("order", None)
        return order

    def clean(self):
        return super(CourseForm, self).clean()

    def validate_unique(self):
        return super(CourseForm, self).validate_unique()

    def save(self, commit=True):
        return super(CourseForm, self).save(commit)


class LessionForm(forms.ModelForm):

    class Meta:
        model = Lession
        fields = ['title', 'subtitle','url', 'order']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(LessionForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(LessionForm, self).is_valid()

    def full_clean(self):
        return super(LessionForm, self).full_clean()

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        return title

    def clean_subtitle(self):
        subtitle = self.cleaned_data.get("subtitle", None)
        return subtitle

    def clean_order(self):
        order = self.cleaned_data.get("order", None)
        return order

    def clean(self):
        return super(LessionForm, self).clean()

    def validate_unique(self):
        return super(LessionForm, self).validate_unique()

    def save(self, commit=True):
        return super(LessionForm, self).save(commit)


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'order']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PageForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PageForm, self).is_valid()

    def full_clean(self):
        return super(PageForm, self).full_clean()

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        return title

    def clean_subtitle(self):
        subtitle = self.cleaned_data.get("subtitle", None)
        return subtitle

    def clean_order(self):
        order = self.cleaned_data.get("order", None)
        return order

    def clean(self):
        return super(PageForm, self).clean()

    def validate_unique(self):
        return super(PageForm, self).validate_unique()

    def save(self, commit=True):
        return super(PageForm, self).save(commit)


class SnapForm(forms.ModelForm):

    class Meta:
        model = Snap
        fields = ['title', 'subtile', 'description', 'slug','http_only', 'file']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(SnapForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(SnapForm, self).is_valid()

    def full_clean(self):
        return super(SnapForm, self).full_clean()

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        return title

    def clean_subtile(self):
        subtile = self.cleaned_data.get("subtile", None)
        return subtile

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_slug(self):
        slug = self.cleaned_data.get("slug", None)
        return slug

    def clean_file(self):
        file = self.cleaned_data.get("file", None)
        return file

    def clean(self):
        return super(SnapForm, self).clean()

    def validate_unique(self):
        return super(SnapForm, self).validate_unique()

    def save(self, commit=True):
        return super(SnapForm, self).save(commit)

