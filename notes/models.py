from __future__ import unicode_literals

from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=512,blank=False)
    note = models.TextField(blank=False)

    def __str__(self):
        return self.title
