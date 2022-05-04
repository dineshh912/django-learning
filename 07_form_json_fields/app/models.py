from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.JSONField()
    contact = models.JSONField()

    def __str__(self):
        return self.name



class address_type(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Bird(models.Model):
    common_name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=250)


    def __str__(self):
        return self.common_name
