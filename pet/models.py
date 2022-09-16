from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

class Pet(models.Model):
    name = models.CharField(max_length=120)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="owner")

    def __str__(self):
        return (f"{self.name}")