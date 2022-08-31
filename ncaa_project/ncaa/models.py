from django.db import models

# Create your models here.
# tunr/models.py


class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    divison = models.CharField(max_length=100)
    wins = models.PositiveSmallIntegerField()
    losses = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, related_name='player')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    injured_reserved_list = models.BooleanField()

    def __str__(self):
        return self.name
