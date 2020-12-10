from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin
from django_reverse_admin import ReverseModelAdmin

from .models import *

@admin.register(Video)
class VideoAdmin(SortableAdminMixin, admin.ModelAdmin):
        model = Video
