from django.db import models

class Book(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)
    description = models.TextField()