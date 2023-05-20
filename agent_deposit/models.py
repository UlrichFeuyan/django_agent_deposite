# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the True
# Feel free to rename the models, but don't rename db_table values or field names.
import secrets
import string
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models.signals import post_save
from django.db.transaction import commit
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.utils.text import slugify
from django.core.mail import send_mail


class Agent(models.Model):
    IDAgent = models.AutoField(db_column='IDAgent', primary_key=True)
    CodeAgent = models.CharField(db_column='CodeAgent', max_length=50, blank=True, null=True)
    msisdn = models.CharField(unique=True, max_length=50)
    NomAgent = models.CharField(db_column='NomAgent', max_length=50, blank=True, null=True)
    AgentActif = models.IntegerField(db_column='AgentActif', blank=True, null=True)
    CodeOperateur = models.ForeignKey('Operateur', models.DO_NOTHING, db_column='CodeOperateur',
                                      to_field='CodeOperateur', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'agent'
        verbose_name = "Agent"
        verbose_name_plural = "Agents"

    def __str__(self):
        return f"{self.NomAgent}({self.AgentActif})"


class Codebank(models.Model):
    IDCodeBank = models.AutoField(db_column='IDCodeBank', primary_key=True)
    CodeBank = models.CharField(db_column='CodeBank', unique=True, max_length=50)
    CodeSwift = models.CharField(db_column='CodeSwift', max_length=50, blank=True, null=True)
    NomBank = models.CharField(db_column='NomBank', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'codebank'
        verbose_name = "Code Bank"
        verbose_name_plural = "Codes Bank"

    def __str__(self):
        return f"{self.NomBank}({self.CodeBank})"


class Comptes(models.Model):
    IDComptes = models.AutoField(db_column='IDComptes', primary_key=True)
    Codeage = models.CharField(db_column='Codeage', max_length=6, blank=True, null=True)
    ncp = models.CharField(max_length=15, blank=True, null=True)
    typ = models.CharField(max_length=7, blank=True, null=True)
    Solde = models.DecimalField(db_column='Solde', max_digits=24, decimal_places=6, blank=True, null=True)
    CodeBank = models.ForeignKey(Codebank, models.DO_NOTHING, db_column='CodeBank', to_field='CodeBank', blank=True,
                                 null=True)

    class Meta:
        managed = True
        db_table = 'comptes'
        verbose_name = "Compte"
        verbose_name_plural = "Comptes"

    def __str__(self):
        return f"{self.typ}({self.CodeBank.NomBank})"


class Evenements(models.Model):
    IDevenements = models.BigAutoField(db_column='IDevenements', primary_key=True)
    montant = models.DecimalField(max_digits=24, decimal_places=6, blank=True, null=True)
    refOrig = models.CharField(db_column='refOrig', max_length=50, blank=True, null=True)  # voucher
    natOrig = models.ForeignKey('Typetransaction', models.DO_NOTHING, db_column='natOrig', to_field='CodeType',
                                blank=True, null=True)
    DoOrig = models.CharField(db_column='DoOrig', max_length=50, blank=True, null=True)
    BenOrig = models.CharField(db_column='BenOrig', max_length=50, blank=True, null=True)
    refFin = models.CharField(db_column='refFin', max_length=50, blank=True, null=True)
    etaOrig = models.CharField(db_column='etaOrig', max_length=2, blank=True, null=True)
    userOrig = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='userOrig', to_field='CodeUser',
                                 blank=True, null=True)
    Caisseorig = models.CharField(db_column='Caisseorig', max_length=10, blank=True, null=True)
    chqOrig = models.CharField(db_column='chqOrig', max_length=50, blank=True, null=True)
    DoFin = models.CharField(db_column='DoFin', max_length=50, blank=True, null=True)
    BenFIn = models.CharField(db_column='BenFIn', max_length=50, blank=True, null=True)
    sensOrig = models.ForeignKey('Sens', models.DO_NOTHING, db_column='sensOrig', to_field='CodeSens', blank=True,
                                 null=True)
    natFin = models.CharField(db_column='natFin', max_length=10, blank=True, null=True)
    dcoOrig = models.CharField(db_column='dcoOrig', max_length=50, blank=True, null=True)
    hsaiOrig = models.CharField(db_column='hsaiOrig', max_length=50, blank=True, null=True)
    etaFin = models.CharField(db_column='etaFin', max_length=5, blank=True, null=True)
    statutTrt = models.CharField(db_column='statutTrt', max_length=2, blank=True, null=True)
    statutCreation = models.CharField(db_column='statutCreation', max_length=10, blank=True, null=True)
    refOPER = models.CharField(db_column='refOPER', max_length=50, blank=True, null=True)
    CodeOperateur = models.ForeignKey('Operateur', models.DO_NOTHING, db_column='CodeOperateur',
                                      to_field='CodeOperateur', blank=True, null=True)
    Msisdn = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Msisdn', to_field='msisdn', blank=True, null=True)
    cptOPERSide = models.CharField(db_column='cptOPERSide', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'evenements'
        verbose_name = "Evenement"
        verbose_name_plural = "Evenements"

    def __str__(self):
        return f"{self.refOrig} ({self.natOrig.LibelleType}) --> {self.etaOrig}"


class Historique(models.Model):
    IDhistorique = models.BigAutoField(db_column='IDhistorique', primary_key=True)
    montant = models.DecimalField(max_digits=24, decimal_places=6, blank=True, null=True)
    refOrig = models.CharField(db_column='refOrig', max_length=50, blank=True, null=True)
    natOrig = models.CharField(db_column='natOrig', max_length=5, blank=True, null=True)
    DoOrig = models.CharField(db_column='DoOrig', max_length=50, blank=True, null=True)
    BenOrig = models.CharField(db_column='BenOrig', max_length=50, blank=True, null=True)
    refFin = models.CharField(db_column='refFin', max_length=50, blank=True, null=True)
    etaOrig = models.CharField(db_column='etaOrig', max_length=2, blank=True, null=True)
    userOrig = models.CharField(db_column='userOrig', max_length=10, blank=True, null=True)
    Caisseorig = models.CharField(db_column='Caisseorig', max_length=10, blank=True, null=True)
    chqOrig = models.CharField(db_column='chqOrig', max_length=50, blank=True, null=True)
    DoFin = models.CharField(db_column='DoFin', max_length=50, blank=True, null=True)
    BenFIn = models.CharField(db_column='BenFIn', max_length=50, blank=True, null=True)
    sensOrig = models.CharField(db_column='sensOrig', max_length=1, blank=True, null=True)
    natFin = models.CharField(db_column='natFin', max_length=10, blank=True, null=True)
    dcoOrig = models.CharField(db_column='dcoOrig', max_length=50, blank=True, null=True)
    hsaiOrig = models.CharField(db_column='hsaiOrig', max_length=50, blank=True, null=True)
    etaFin = models.CharField(db_column='etaFin', max_length=5, blank=True, null=True)
    statutTrt = models.CharField(db_column='statutTrt', max_length=2, blank=True, null=True)
    statutCreation = models.CharField(db_column='statutCreation', max_length=10, blank=True, null=True)
    refOPER = models.CharField(db_column='refOPER', max_length=50, blank=True, null=True)
    CodeOperateur = models.CharField(db_column='CodeOperateur', max_length=50, blank=True, null=True)
    Msisdn = models.CharField(db_column='Msisdn', max_length=50, blank=True, null=True)
    cptOPERSide = models.CharField(db_column='cptOPERSide', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'historique'
        verbose_name = "Historique"
        verbose_name_plural = "Historique"

    def __str__(self):
        return f"{self.refOrig}({self.natOrig})"


class Operateur(models.Model):
    IDOperateur = models.AutoField(db_column='IDOperateur', primary_key=True)
    CodeOperateur = models.CharField(db_column='CodeOperateur', unique=True, max_length=50)
    DescriptionOP = models.CharField(db_column='DescriptionOP', max_length=50, blank=True, null=True)
    CodePays = models.ForeignKey('Pays', models.DO_NOTHING, db_column='CodePays', to_field='CodePays', blank=True,
                                 null=True)
    endpointOper = models.CharField(db_column='endpointOper', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'operateur'
        verbose_name = "Operateur"
        verbose_name_plural = "Operateurs"

    def __str__(self):
        return f"{self.CodeOperateur}({self.CodePays})"


class Pays(models.Model):
    IDPays = models.AutoField(db_column='IDPays', primary_key=True)
    CodePays = models.CharField(db_column='CodePays', unique=True, max_length=5)
    LibPays = models.CharField(db_column='LibPays', max_length=50, blank=True, null=True)
    indicatif = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pays'
        verbose_name = "Pays"
        verbose_name_plural = "Pays"

    def __str__(self):
        return f"{self.LibPays}({self.CodePays})"


class Sens(models.Model):
    IDSens = models.AutoField(db_column='IDSens', primary_key=True)
    CodeSens = models.CharField(db_column='CodeSens', unique=True, max_length=1)
    LibelleSens = models.CharField(db_column='LibelleSens', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sens'
        verbose_name = "Sens"
        verbose_name_plural = "Sens"

    def __str__(self):
        return self.LibelleSens


class Typetransaction(models.Model):
    IDTypeTransaction = models.AutoField(db_column='IDTypeTransaction', primary_key=True)
    CodeType = models.CharField(db_column='CodeType', unique=True, max_length=5)
    LibelleType = models.CharField(db_column='LibelleType', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'typetransaction'
        verbose_name = "Type de transaction"
        verbose_name_plural = "Types de transaction"

    def __str__(self):
        return self.LibelleType


class Profil(models.Model):
    IDProfil = models.AutoField(db_column='IDProfil', primary_key=True)
    CodeProfil = models.CharField(db_column='CodeProfil', unique=True, max_length=50)
    DescriptionPro = models.CharField(db_column='DescriptionPro', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'profil'
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.CodeProfil

    def to_dict(self):
        return {
            'IDProfil': self.IDProfil,
            'CodeProfil': self.CodeProfil,
            'DescriptionPro': self.DescriptionPro,
        }


class Utilisateur(AbstractUser):
    IDUtilisateur = models.AutoField(db_column='IDUtilisateur', primary_key=True)
    CodeUser = models.CharField(db_column='CodeUser', unique=True, max_length=100, blank=True, null=True)
    NomUser = models.CharField(db_column='NomUser', max_length=50, blank=True, null=True)
    UserActif = models.BooleanField(db_column='UserActif', default=True)
    CodeProfil = models.ForeignKey(Profil, models.DO_NOTHING, db_column='CodeProfil', to_field='CodeProfil', blank=True,
                                   null=True)

    class Meta:
        managed = True
        db_table = 'utilisateur'
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return f"{self.NomUser}({self.UserActif})"

    def save(self, *args, **kwargs):
        self.groups.clear()  # retire l'utilisateur de tous les groupes
        if not self.username:
            # fonction slugify pour transformer les espaces en tirets et les caractères accentués en caractères non-accentués
            self.username = slugify(self.NomUser)
        if not self.password:  # crée un nouveau mot de passe pour l'utilisateur s'il n'est pas définit
            password = ''.join(secrets.choice(string.ascii_letters) for i in range(20))
            self.set_password(password)
            if self.email:  # envoie le mot de passe par mail à l'utilisateur
                send_mail(
                    "Création de compte utilisateur sur --Agent Deposit--",
                    f"Votre mot de passe est : {password}.",
                    "djofangulrich05@gmail.com",
                    ["ulrich.feuyan@gmail.com"],  # adresse mail de l'utilisateur
                    fail_silently=False,
                )
            print(password)
        self.is_active = self.UserActif
        if self.CodeProfil.CodeProfil == "ADMIN":  # accorder l'accès à l'admin django pour les profils ADMIN
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False

        super(Utilisateur, self).save(*args, **kwargs)

        # Récupérer le groupe correspondant au profil de l'utilisateur
        groupe, created = Group.objects.get_or_create(name=self.CodeProfil.CodeProfil)

        # Ajouter l'utilisateur au groupe correspondant à son profil
        self.groups.add(groupe)

        # Appeler la méthode save de la classe parente pour enregistrer l'utilisateur dans la base de données
        super().save(*args, **kwargs)
