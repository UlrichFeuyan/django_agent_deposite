from django.db import models


class Agent(models.Model):
    IDAgent = models.AutoField(db_column='IDAgent', primary_key=True)
    CodeAgent = models.CharField(db_column='CodeAgent', max_length=50, blank=True,
                                 null=True)
    msisdn = models.CharField(unique=True, max_length=50)
    NomAgent = models.CharField(db_column='NomAgent', max_length=50, blank=True,
                                null=True)
    AgentActif = models.IntegerField(db_column='AgentActif', blank=True, null=True)
    CodeOperateur = models.ForeignKey('Operateur', models.DO_NOTHING, db_column='CodeOperateur',
                                      to_field='CodeOperateur', blank=True, null=True)

    def __str__(self):
        return self.NomAgent

    class Meta:
        managed = False
        db_table = 'agent'
        verbose_name = "Agent"
        verbose_name_plural = "Agents"


class Codebank(models.Model):
    IDCodeBank = models.AutoField(db_column='IDCodeBank', primary_key=True)
    CodeBank = models.CharField(db_column='CodeBank', unique=True, max_length=50)
    CodeSwift = models.CharField(db_column='CodeSwift', max_length=50, blank=True,
                                 null=True)
    NomBank = models.CharField(db_column='NomBank', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.NomBank

    class Meta:
        managed = False
        db_table = 'codebank'
        verbose_name = "Code bank"
        verbose_name_plural = "Codes bank"


class Comptes(models.Model):
    IDComptes = models.AutoField(db_column='IDComptes', primary_key=True)
    Codeage = models.CharField(db_column='Codeage', max_length=6, blank=True, null=True)
    ncp = models.CharField(max_length=15, blank=True, null=True)
    typ = models.CharField(max_length=7, blank=True, null=True)
    Solde = models.DecimalField(db_column='Solde', max_digits=24, decimal_places=6, blank=True,
                                null=True)
    CodeBank = models.ForeignKey(Codebank, models.DO_NOTHING, db_column='CodeBank', to_field='CodeBank', blank=True,
                                 null=True)

    def __str__(self):
        return self.ncp

    class Meta:
        managed = False
        db_table = 'comptes'
        verbose_name = "Compte"
        verbose_name_plural = "Comptes"


class Evenements(models.Model):
    IDevenements = models.BigAutoField(db_column='IDevenements', primary_key=True)
    montant = models.DecimalField(max_digits=24, decimal_places=6, blank=True, null=True)
    refOrig = models.CharField(db_column='refOrig', max_length=50, blank=True, null=True)
    natOrig = models.ForeignKey('Typetransaction', models.DO_NOTHING, db_column='natOrig', to_field='CodeType',
                                blank=True, null=True)
    DoOrig = models.CharField(db_column='DoOrig', max_length=50, blank=True, null=True)
    BenOrig = models.CharField(db_column='BenOrig', max_length=50, blank=True, null=True)
    refFin = models.CharField(db_column='refFin', max_length=50, blank=True, null=True)
    etaOrig = models.CharField(db_column='etaOrig', max_length=2, blank=True, null=True)
    userOrig = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='userOrig', to_field='CodeUser',
                                 blank=True, null=True)
    caisseorig = models.CharField(db_column='Caisseorig', max_length=10, blank=True,
                                  null=True)
    chqOrig = models.CharField(db_column='chqOrig', max_length=50, blank=True, null=True)
    DoFin = models.CharField(db_column='DoFin', max_length=50, blank=True, null=True)
    BenFIn = models.CharField(db_column='BenFIn', max_length=50, blank=True, null=True)
    sensOrig = models.ForeignKey('Sens', models.DO_NOTHING, db_column='sensOrig', to_field='CodeSens', blank=True,
                                 null=True)
    natFin = models.CharField(db_column='natFin', max_length=10, blank=True, null=True)
    dcoOrig = models.CharField(db_column='dcoOrig', max_length=50, blank=True, null=True)
    hsaiOrig = models.CharField(db_column='hsaiOrig', max_length=50, blank=True,
                                null=True)
    etaFin = models.CharField(db_column='etaFin', max_length=5, blank=True, null=True)
    statutTrt = models.CharField(db_column='statutTrt', max_length=2, blank=True,
                                 null=True)
    statutCreation = models.CharField(db_column='statutCreation', max_length=10, blank=True,
                                      null=True)
    refMTN = models.CharField(db_column='refMTN', max_length=50, blank=True, null=True)
    CodeOperateur = models.ForeignKey('Operateur', models.DO_NOTHING, db_column='CodeOperateur',
                                      to_field='CodeOperateur', blank=True, null=True)
    Msisdn = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Msisdn', to_field='msisdn', blank=True,
                               null=True)
    cptMTNSide = models.CharField(db_column='cptMTNSide', max_length=50, blank=True,
                                  null=True)

    def __str__(self):
        return f"{self.refOrig} -> {self.refFin}"

    class Meta:
        managed = False
        db_table = 'evenements'
        verbose_name = "Evenement"
        verbose_name_plural = "Evenements"


class Historique(models.Model):
    IDhistorique = models.BigAutoField(db_column='IDhistorique', primary_key=True)
    montant = models.DecimalField(max_digits=24, decimal_places=6, blank=True, null=True)
    refOrig = models.CharField(db_column='refOrig', max_length=50, blank=True, null=True)
    natOrig = models.CharField(db_column='natOrig', max_length=5, blank=True, null=True)
    DoOrig = models.CharField(db_column='DoOrig', max_length=50, blank=True, null=True)
    BenOrig = models.CharField(db_column='BenOrig', max_length=50, blank=True, null=True)
    refFin = models.CharField(db_column='refFin', max_length=50, blank=True, null=True)
    etaOrig = models.CharField(db_column='etaOrig', max_length=2, blank=True, null=True)
    userOrig = models.CharField(db_column='userOrig', max_length=10, blank=True,
                                null=True)
    Caisseorig = models.CharField(db_column='Caisseorig', max_length=10, blank=True,
                                  null=True)
    chqOrig = models.CharField(db_column='chqOrig', max_length=50, blank=True, null=True)
    DoFin = models.CharField(db_column='DoFin', max_length=50, blank=True, null=True)
    BenFIn = models.CharField(db_column='BenFIn', max_length=50, blank=True, null=True)
    sensOrig = models.CharField(db_column='sensOrig', max_length=1, blank=True, null=True)
    natFin = models.CharField(db_column='natFin', max_length=10, blank=True, null=True)
    dcoOrig = models.CharField(db_column='dcoOrig', max_length=50, blank=True, null=True)
    hsaiOrig = models.CharField(db_column='hsaiOrig', max_length=50, blank=True,
                                null=True)
    etaFin = models.CharField(db_column='etaFin', max_length=5, blank=True, null=True)
    statutTrt = models.CharField(db_column='statutTrt', max_length=2, blank=True,
                                 null=True)
    statutCreation = models.CharField(db_column='statutCreation', max_length=10, blank=True,
                                      null=True)
    refMTN = models.CharField(db_column='refMTN', max_length=50, blank=True, null=True)
    CodeOperateur = models.CharField(db_column='CodeOperateur', max_length=50, blank=True,
                                     null=True)
    Msisdn = models.CharField(db_column='Msisdn', max_length=50, blank=True, null=True)
    cptMTNSide = models.CharField(db_column='cptMTNSide', max_length=50, blank=True,
                                  null=True)

    def __str__(self):
        return f"{self.refOrig} -> {self.refFin}"

    class Meta:
        managed = False
        db_table = 'historique'
        verbose_name = "Historique"
        verbose_name_plural = "Historique"


class Operateur(models.Model):
    IDOperateur = models.AutoField(db_column='IDOperateur', primary_key=True)
    CodeOperateur = models.CharField(db_column='CodeOperateur', unique=True,
                                     max_length=50)
    DescriptionOP = models.CharField(db_column='DescriptionOP', max_length=50, blank=True,
                                     null=True)
    CodePays = models.ForeignKey('Pays', models.DO_NOTHING, db_column='CodePays', to_field='CodePays', blank=True,
                                 null=True)

    def __str__(self):
        return self.DescriptionOP

    class Meta:
        managed = False
        db_table = 'operateur'
        verbose_name = "Operateur"
        verbose_name_plural = "Operateurs"


class Pays(models.Model):
    IDPays = models.AutoField(db_column='IDPays', primary_key=True)
    CodePays = models.CharField(db_column='CodePays', unique=True, max_length=5)
    LibPays = models.CharField(db_column='LibPays', max_length=50, blank=True, null=True)
    indicatif = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.LibPays

    class Meta:
        managed = False
        db_table = 'pays'
        verbose_name = "Pays"
        verbose_name_plural = "Pays"


class Profil(models.Model):
    IDProfil = models.AutoField(db_column='IDProfil', primary_key=True)
    CodeProfil = models.CharField(db_column='CodeProfil', unique=True, max_length=50)
    DescriptionPro = models.CharField(db_column='DescriptionPro', max_length=50, blank=True,
                                      null=True)

    def __str__(self):
        return self.DescriptionPro

    class Meta:
        managed = False
        db_table = 'profil'
        verbose_name = "Profil"
        verbose_name_plural = "Profils"


class Sens(models.Model):
    IDSens = models.AutoField(db_column='IDSens', primary_key=True)
    CodeSens = models.CharField(db_column='CodeSens', unique=True, max_length=1)
    LibelleSens = models.CharField(db_column='LibelleSens', max_length=50, blank=True,
                                   null=True)

    def __str__(self):
        return self.LibelleSens

    class Meta:
        managed = False
        db_table = 'sens'
        verbose_name = "Sens"
        verbose_name_plural = "Sens"


class Typetransaction(models.Model):
    IDTypeTransaction = models.AutoField(db_column='IDTypeTransaction', primary_key=True)
    CodeType = models.CharField(db_column='CodeType', unique=True, max_length=5)
    LibelleType = models.CharField(db_column='LibelleType', max_length=50, blank=True,
                                   null=True)

    def __str__(self):
        return self.LibelleType

    class Meta:
        managed = False
        db_table = 'typetransaction'
        verbose_name = "Type de transaction"
        verbose_name_plural = "Types de transaction"


class Utilisateur(models.Model):
    IDUtilisateur = models.AutoField(db_column='IDUtilisateur', primary_key=True)
    CodeUser = models.CharField(db_column='CodeUser', unique=True, max_length=10)
    NomUser = models.CharField(db_column='NomUser', max_length=50, blank=True, null=True)
    UserActif = models.IntegerField(db_column='UserActif', blank=True, null=True)
    CodeProfil = models.ForeignKey(Profil, models.DO_NOTHING, db_column='CodeProfil', to_field='CodeProfil', blank=True,
                                   null=True)

    def __str__(self):
        return self.NomUser

    class Meta:
        managed = False
        db_table = 'utilisateur'
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
