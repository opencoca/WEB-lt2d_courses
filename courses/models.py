import datetime
from django.urls import reverse

from django.db import models
from dataclasses import dataclass, field
from django.template.defaultfilters import slugify
from django.utils import timezone

class IntegerRangeField(models.IntegerField):
    """
    Allows for integers fields with custom ranges.

    example: size = fields.IntegerRangeField(min_value=1, max_value=5)
    """
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Syllabus(models.Model):
    """
    Syllabus have a one to one relationship with Courses
    """
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']
        verbose_name_plural = "Syllabus"

    def __str__(self):
        return "%s Stllabus" % self.name

    def save(self, *args, **kwargs): # new
        """
        Example of automatic slugified meeting
        if not self.meet:
            self.meet = slugify(self.name)
        """
        return super().save(*args, **kwargs)


class Course(models.Model):
    """
    """
    syllabus  = models.OneToOneField(
        Syllabus,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    pub_date = models.DateTimeField('date published')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']
        #verbose_name_plural = "1. Course"

    def __str__(self):
        return self.syllabus.name

    def name(self):
        return self.syllabus.name

    def recent_course(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=180)

class Lession(models.Model):
    """
    This represents a Lession, or chapter
    """
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    course = models.ManyToManyField(Course, blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']
        #verbose_name_plural = "2. Lessions"

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    lession = models.ManyToManyField(Lession, blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']
        #verbose_name_plural = "2. Pages"

    def __str__(self):
        return self.title

class Snap(models.Model):
    """
    """
    title = models.CharField(max_length=200)
    subtile = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    page = models.ManyToManyField(Lession, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    file = models.FileField(upload_to='snap/%Y/%m/%d/', null=True, verbose_name="")
#    timestamp  = models.DateTimeField('date published')
#    timestamp.editable = True

    class Meta:
        ordering = ['my_order']

    def get_absolute_url(self):
        return reverse ("snap_detail", kwargs={"slug":self.slug})

    def __str__(self):
        return self.title + ": " + str(self.my_order)

