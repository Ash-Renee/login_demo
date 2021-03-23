from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}

        if len(post_data['first_name']) < 2:
            errors['first_name'] = "hey you are too short!"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "hey you are too short!"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"

        if 'birth_date' not in post_data:
                errors['birth_date'] = "Must enter a birth date" ##why do you have this commented out?

        if len(post_data['birth_date']) < 2:
                errors['birth_date'] = "Must enter birth date" ##how do we ensure correct format?

        if len(post_data['password']) < 8:
                errors['password'] = "Password must be at least 8 Disney characters long!"

        if post_data['password'] != post_data['confirm_password']:
                errors['confirm_password'] = "Password and Confirm Password must match!"
        
        return errors 


class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    birth_date = models.DateTimeField()
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"Shows {self.first_name} {self.last_name} {self.email}"
