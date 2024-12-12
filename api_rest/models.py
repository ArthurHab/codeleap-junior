from django.db import models
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, null=False, blank=False)
    created_datatime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title