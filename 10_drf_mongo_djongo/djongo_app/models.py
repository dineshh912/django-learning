from django.db import models
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
# Create your models here.

class Account(models.Model):
    email = models.EmailField()


class ShortLink(models.Model):
    id = models.CharField(max_length=12, primary_key=True, default=get_random_string)
    account = models.ForeignKey(Account, 
                                on_delete=models.CASCADE,
                                related_name='short_links')
    redirect_to = models.URLField()

    def __str__(self):
        return self.redirect_to