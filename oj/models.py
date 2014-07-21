from django.db import models

class SourceCode(models.Model):
  content = models.CharField(max_length=1000)
