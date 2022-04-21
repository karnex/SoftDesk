from django.db import models

from authentication.models import User


CONTRIBUTOR_ROLE = [('Auteur', 'Auteur'), ('Contributeur', 'Contributeur')]
TYPE_CHOICES = [('front-end', 'front-end'), ('back-end', 'back-end'), ('iOS', 'iOS'), ('Android', 'Android')]


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    contributors = models.ManyToManyField(User, through='Contributor')


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=CONTRIBUTOR_ROLE)
