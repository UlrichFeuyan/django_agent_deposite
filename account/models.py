from django.contrib.auth.models import AbstractUser
from django.db import models

SEXE_CHOICES = [
    ('masculin', 'Masculin'),
    ('feminin', 'Féminin'),
    ('autre', 'Autre'),
]


class CustomUser(AbstractUser):
    sex = models.CharField(max_length=15, choices=SEXE_CHOICES, null=True)
    phone = models.CharField(max_length=35, null=True)


class Profil(models.Model):
    IDProfil = models.AutoField(db_column='IDProfil', primary_key=True)
    CodeProfil = models.CharField(db_column='CodeProfil', unique=True, max_length=50)
    DescriptionPro = models.CharField(db_column='DescriptionPro', max_length=50, blank=True,
                                      null=True)

    class Meta:
        managed = False
        db_table = 'profil'


class Utilisateur(models.Model):
    IDUtilisateur = models.AutoField(db_column='IDUtilisateur', primary_key=True)
    CodeUser = models.CharField(db_column='CodeUser', unique=True, max_length=10)
    NomUser = models.CharField(db_column='NomUser', max_length=50, blank=True, null=True)
    UserActif = models.IntegerField(db_column='UserActif', blank=True, null=True)
    CodeProfil = models.ForeignKey(Profil, models.DO_NOTHING, db_column='CodeProfil', to_field='CodeProfil', blank=True,
                                   null=True)

    class Meta:
        managed = False
        db_table = 'utilisateur'
