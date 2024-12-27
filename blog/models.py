from django.db import models
from django.conf import settings

# Create your models here.
class Tag(models.Model):
  value = models.TextField(max_length = 100)

  def _str_(self):
    return self.value

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  created_at = models.DateTimeField(auto_now_add = True)
  modified_at = models.DateTimeField(auto_now = True)
  published_at = models.DateTimeField(blank = True, null = True)
  title = models.TextField(max_length = 100)
  slug = models.SlugField()
  summary = models.TextField(max_length = 500)
  content = models.TextField()
  tags = models.ManyToManyField(Tag, related_name = "posts")

  def _str_(self):
    return f"{self.author} {self.title}"