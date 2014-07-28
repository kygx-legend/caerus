from django.db import models

class Code(models.Model):
  content = models.TextField()
  language = models.CharField(max_length=32)
  filename = models.CharField(max_length=32)
  path = models.CharField(max_length=32)
  target = models.CharField(max_length=32)
