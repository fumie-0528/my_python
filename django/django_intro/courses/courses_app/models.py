from django.db import models
from datetime import datetime


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Name should be at least 5 characters"
        if len(postData['description']) < 15:
            errors["description"] = "Description should be at least 10 characters"
        return errors
        
class Course(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = CourseManager() 