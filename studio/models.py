from django.db import models
from django.urls import reverse

class Video(models.Model):
    Video_Description= models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    videofile= models.FileField(upload_to='videos/%Y/%m/%d/', null=True, verbose_name="")
#    timestamp  = models.DateTimeField('date published')
#    timestamp.editable = True

    class Meta:
        ordering = ['slug']

    def get_absolute_url(self):
        return reverse ("deploy:detail", kwargs={"slug":self.slug})

    def __str__(self):
        return self.Video_Description + ": " + str(self.id)
