from django.db import models
from django.contrib.auth.models import User

class SearchHistory(models.Model):
    user        = models.ForeignKey(User)
    word        = models.CharField(max_length=255)
    timestamp   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.word