from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.JSONField()

    def __str__(self):
        return self.title



class Bird(models.Model):
    common_name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=250)


    def __str__(self):
        return self.common_name
