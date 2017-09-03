from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData["name"]) < 2:
            errors["name"] = "Name should be more than 3 characters"

        if len(postData["alias"]) < 2:
            errors["alias"] = "Username should be more than 3 characters"
        
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Entered an invalid email" 
        
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be more than 8 characters"

        if postData["password"] != postData["confirm"]:
            errors["confirm"] = "Passwords don't match"

        if len(postData["dob"]) < 8:
            errors["dob"] = "Date of Birth should be more than 8 characters"


        return errors;


class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	dob = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	friends = models.ManyToManyField('self', related_name = "more_friends")
	objects = UserManager()
