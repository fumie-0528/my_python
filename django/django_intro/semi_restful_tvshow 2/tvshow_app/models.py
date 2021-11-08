from django.db import models

class Tvshow(models.Model):
    title = models.TextField()
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


