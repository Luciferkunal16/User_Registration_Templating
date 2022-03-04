from django.db import models


class UserDetail(models.Model):
    """
    created this class for table in database
    """
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=40)
    age = models.IntegerField(default=None)
