from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import redirect
from django.dispatch import receiver
from django.urls import reverse_lazy
from django.contrib.auth.models import Group

from .models import Utilisateur, Profil


@receiver(post_save, sender=Profil)
def create_group(sender, instance, created, **kwargs):
    if created:
        group, created = Group.objects.get_or_create(name=instance.CodeProfil)


@receiver(post_save, sender=Utilisateur)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name=instance.CodeProfil.CodeProfil)
        group.user_set.add(instance)


@receiver(post_save, sender=Utilisateur)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        profile = instance.CodeProfil
        group, created = Group.objects.get_or_create(name=profile.CodeProfil)
        instance.groups.add(group)
