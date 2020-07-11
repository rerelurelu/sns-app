from django.db import models


class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    author = models.CharField(max_length=20)
    images = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    read_text = models.CharField(max_length=50, null=True, blank=True, default='a')
