from django.db import models

class User(models.Model):
    name = models.TextField()
    email_address = models.CharField(max_length=45)
    age = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
