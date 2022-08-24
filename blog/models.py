from django.db import models
import logging
# Create your models here.

_logger = logging.getLogger(__name__)

class BlogPost(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.IntegerField(default=0)

