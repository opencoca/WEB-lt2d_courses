from django.contrib import admin
from .models import Syllabus, Course, Lession, Page, Snap
from django_baker.admin import ExtendedModelAdminMixin
from adminsortable2.admin import SortableAdminMixin


class SyllabusAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = []


class CourseAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = []


class LessionAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = []


class PageAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = []

@admin.register(Snap)
class SnapAdmin(SortableAdminMixin, ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = []
    list_per_page = 10

admin.site.register(Syllabus, SyllabusAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lession, LessionAdmin)
admin.site.register(Page, PageAdmin)
