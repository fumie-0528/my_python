from django.db import models
from datetime import datetime, timedelta
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'

        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'

        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="Invalid email address"

        email_check=User.objects.filter(email=postData['email'])
        if email_check:
            errors['duplicate']="Invalid email already taken"
     
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Passwords do not match'
        
        return errors
    def register(self, postData):
        pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
        return User.objects.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = pw,
        )
    def authenticate(self, email, password):
        users=User.objects.filter(email=email)
        if users:
            user=users[0]
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return True
            else:
                return False
        return False

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    objects = UserManager()

class TripManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['destination']) < 3:
            errors["destination"] = "Destination must have at least 3 characters."        
        if len(postData['plan']) == 0:
            errors["plan"] = "Plan is empty"
        if datetime.strptime(postData['date_start'], '%Y-%m-%d') < datetime.now():
            errors['date_start'] = 'Start Date cannot be the past date'
        if datetime.strptime(postData['date_end'], '%Y-%m-%d') < datetime.now():
            errors['date_end'] = 'End Date cannot be the past date'
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    plan = models.CharField(max_length=255)
    planner = models.ForeignKey(User, related_name = "trip",on_delete=models.CASCADE)
    joined = models.ManyToManyField(User, related_name = "joined_trips")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)            
    objects= TripManager()