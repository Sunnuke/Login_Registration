from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def user_validation(self, postData):
        errors = {}
        # Filter index for name format
        gex = re.compile(r'^[a-zA-Z]+$')
        # Filter index for Email format
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # Checking for numerical characters(first name)
        if not gex.match(postData['fname']):
            errors['fnumname'] = "Your First Name should not have numerical characters!"
        # Checking length of characters(first name)
        if len(postData['fname']) < 2:
            errors['fname'] = "Your First Name should be at least 2 characters!"
        # Checking for numerical characters(last name)
        if not gex.match(postData['lname']):
            errors['lnumname'] = "Your Last Name should not have numerical characters!"
        # Checking length of characters(last name)
        if len(postData['fname']) < 2:
            errors['fname'] = "Your Last Name should be at least 2 characters!"
        # Checking format of email and characters
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Your Last Name should be at least 2 characters!"
        


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)