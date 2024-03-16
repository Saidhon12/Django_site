from django.db import models

category = (
    ("BMW", "BMW"),
    ("Mercedes", "Mercedes"),
    ("Audi", "Audi"),
    ("Kia", "Kia"),
    ("GM", "GM"),
    ("Toyota", "Toyota"),
    ("Chery", "Chery"),
    ("Tesla", "Tesla"),
    ("BYD", "BYD"),
)

class Product(models.Model):
    name = models.CharField(max_length=200)
    narx = models.IntegerField()
    kategoriya = models.CharField(max_length=200, choices = category)
    malumot  = models.TextField()
    rasm  = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 20)
    password = models.CharField(max_length = 10)
    username = models.CharField(max_length = 20)


class Admins(models.Model):
    name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 10)
    is_boss = models.BooleanField(default = False)


