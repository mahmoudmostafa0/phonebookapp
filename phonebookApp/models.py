from django.db import models


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=200)


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.ManyToManyField(PhoneNumber)
    email = models.EmailField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name
