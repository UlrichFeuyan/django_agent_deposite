# Generated by Django 4.1.7 on 2023-05-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Agent",
            fields=[
                (
                    "IDAgent",
                    models.AutoField(
                        db_column="IDAgent", primary_key=True, serialize=False
                    ),
                ),
                (
                    "CodeAgent",
                    models.CharField(
                        blank=True, db_column="CodeAgent", max_length=50, null=True
                    ),
                ),
                ("msisdn", models.CharField(max_length=50, unique=True)),
                (
                    "NomAgent",
                    models.CharField(
                        blank=True, db_column="NomAgent", max_length=50, null=True
                    ),
                ),
                (
                    "AgentActif",
                    models.IntegerField(blank=True, db_column="AgentActif", null=True),
                ),
            ],
            options={
                "verbose_name": "Agent",
                "verbose_name_plural": "Agents",
                "db_table": "agent",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Codebank",
            fields=[
                (
                    "IDCodeBank",
                    models.AutoField(
                        db_column="IDCodeBank", primary_key=True, serialize=False
                    ),
                ),
                (
                    "CodeBank",
                    models.CharField(db_column="CodeBank", max_length=50, unique=True),
                ),
                (
                    "CodeSwift",
                    models.CharField(
                        blank=True, db_column="CodeSwift", max_length=50, null=True
                    ),
                ),
                (
                    "NomBank",
                    models.CharField(
                        blank=True, db_column="NomBank", max_length=50, null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Code Bank",
                "verbose_name_plural": "Codes Bank",
                "db_table": "codebank",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Comptes",
            fields=[
                (
                    "IDComptes",
                    models.AutoField(
                        db_column="IDComptes", primary_key=True, serialize=False
                    ),
                ),
                (
                    "Codeage",
                    models.CharField(
                        blank=True, db_column="Codeage", max_length=6, null=True
                    ),
                ),
                ("ncp", models.CharField(blank=True, max_length=15, null=True)),
                ("typ", models.CharField(blank=True, max_length=7, null=True)),
                (
                    "Solde",
                    models.DecimalField(
                        blank=True,
                        db_column="Solde",
                        decimal_places=6,
                        max_digits=24,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Compte",
                "verbose_name_plural": "Comptes",
                "db_table": "comptes",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Evenements",
            fields=[
                (
                    "IDevenements",
                    models.BigAutoField(
                        db_column="IDevenements", primary_key=True, serialize=False
                    ),
                ),
                (
                    "montant",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=24, null=True
                    ),
                ),
                (
                    "refOrig",
                    models.CharField(
                        blank=True, db_column="refOrig", max_length=50, null=True
                    ),
                ),
                (
                    "DoOrig",
                    models.CharField(
                        blank=True, db_column="DoOrig", max_length=50, null=True
                    ),
                ),
                (
                    "BenOrig",
                    models.CharField(
                        blank=True, db_column="BenOrig", max_length=50, null=True
                    ),
                ),
                (
                    "refFin",
                    models.CharField(
                        blank=True, db_column="refFin", max_length=50, null=True
                    ),
                ),
                (
                    "etaOrig",
                    models.CharField(
                        blank=True, db_column="etaOrig", max_length=2, null=True
                    ),
                ),
                (
                    "Caisseorig",
                    models.CharField(
                        blank=True, db_column="Caisseorig", max_length=10, null=True
                    ),
                ),
                (
                    "chqOrig",
                    models.CharField(
                        blank=True, db_column="chqOrig", max_length=50, null=True
                    ),
                ),
                (
                    "DoFin",
                    models.CharField(
                        blank=True, db_column="DoFin", max_length=50, null=True
                    ),
                ),
                (
                    "BenFIn",
                    models.CharField(
                        blank=True, db_column="BenFIn", max_length=50, null=True
                    ),
                ),
                (
                    "natFin",
                    models.CharField(
                        blank=True, db_column="natFin", max_length=10, null=True
                    ),
                ),
                (
                    "dcoOrig",
                    models.CharField(
                        blank=True, db_column="dcoOrig", max_length=50, null=True
                    ),
                ),
                (
                    "hsaiOrig",
                    models.CharField(
                        blank=True, db_column="hsaiOrig", max_length=50, null=True
                    ),
                ),
                (
                    "etaFin",
                    models.CharField(
                        blank=True, db_column="etaFin", max_length=5, null=True
                    ),
                ),
                (
                    "statutTrt",
                    models.CharField(
                        blank=True, db_column="statutTrt", max_length=2, null=True
                    ),
                ),
                (
                    "statutCreation",
                    models.CharField(
                        blank=True, db_column="statutCreation", max_length=10, null=True
                    ),
                ),
                (
                    "refOPER",
                    models.CharField(
                        blank=True, db_column="refOPER", max_length=50, null=True
                    ),
                ),
                (
                    "cptOPERSide",
                    models.CharField(
                        blank=True, db_column="cptOPERSide", max_length=50, null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Evenement",
                "verbose_name_plural": "Evenements",
                "db_table": "evenements",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Historique",
            fields=[
                (
                    "IDhistorique",
                    models.BigAutoField(
                        db_column="IDhistorique", primary_key=True, serialize=False
                    ),
                ),
                (
                    "montant",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=24, null=True
                    ),
                ),
                (
                    "refOrig",
                    models.CharField(
                        blank=True, db_column="refOrig", max_length=50, null=True
                    ),
                ),
                (
                    "natOrig",
                    models.CharField(
                        blank=True, db_column="natOrig", max_length=5, null=True
                    ),
                ),
                (
                    "DoOrig",
                    models.CharField(
                        blank=True, db_column="DoOrig", max_length=50, null=True
                    ),
                ),
                (
                    "BenOrig",
                    models.CharField(
                        blank=True, db_column="BenOrig", max_length=50, null=True
                    ),
                ),
                (
                    "refFin",
                    models.CharField(
                        blank=True, db_column="refFin", max_length=50, null=True
                    ),
                ),
                (
                    "etaOrig",
                    models.CharField(
                        blank=True, db_column="etaOrig", max_length=2, null=True
                    ),
                ),
                (
                    "userOrig",
                    models.CharField(
                        blank=True, db_column="userOrig", max_length=10, null=True
                    ),
                ),
                (
                    "Caisseorig",
                    models.CharField(
                        blank=True, db_column="Caisseorig", max_length=10, null=True
                    ),
                ),
                (
                    "chqOrig",
                    models.CharField(
                        blank=True, db_column="chqOrig", max_length=50, null=True
                    ),
                ),
                (
                    "DoFin",
                    models.CharField(
                        blank=True, db_column="DoFin", max_length=50, null=True
                    ),
                ),
                (
                    "BenFIn",
                    models.CharField(
                        blank=True, db_column="BenFIn", max_length=50, null=True
                    ),
                ),
                (
                    "sensOrig",
                    models.CharField(
                        blank=True, db_column="sensOrig", max_length=1, null=True
                    ),
                ),
                (
                    "natFin",
                    models.CharField(
                        blank=True, db_column="natFin", max_length=10, null=True
                    ),
                ),
                (
                    "dcoOrig",
                    models.CharField(
                        blank=True, db_column="dcoOrig", max_length=50, null=True
                    ),
                ),
                (
                    "hsaiOrig",
                    models.CharField(
                        blank=True, db_column="hsaiOrig", max_length=50, null=True
                    ),
                ),
                (
                    "etaFin",
                    models.CharField(
                        blank=True, db_column="etaFin", max_length=5, null=True
                    ),
                ),
                (
                    "statutTrt",
                    models.CharField(
                        blank=True, db_column="statutTrt", max_length=2, null=True
                    ),
                ),
                (
                    "statutCreation",
                    models.CharField(
                        blank=True, db_column="statutCreation", max_length=10, null=True
                    ),
                ),
                (
                    "refOPER",
                    models.CharField(
                        blank=True, db_column="refOPER", max_length=50, null=True
                    ),
                ),
                (
                    "CodeOperateur",
                    models.CharField(
                        blank=True, db_column="CodeOperateur", max_length=50, null=True
                    ),
                ),
                (
                    "Msisdn",
                    models.CharField(
                        blank=True, db_column="Msisdn", max_length=50, null=True
                    ),
                ),
                (
                    "cptOPERSide",
                    models.CharField(
                        blank=True, db_column="cptOPERSide", max_length=50, null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Historique",
                "verbose_name_plural": "Historique",
                "db_table": "historique",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Operateur",
            fields=[
                (
                    "IDOperateur",
                    models.AutoField(
                        db_column="IDOperateur", primary_key=True, serialize=False
                    ),
                ),
                (
                    "CodeOperateur",
                    models.CharField(
                        db_column="CodeOperateur", max_length=50, unique=True
                    ),
                ),
                (
                    "DescriptionOP",
                    models.CharField(
                        blank=True, db_column="DescriptionOP", max_length=50, null=True
                    ),
                ),
                (
                    "endpointOper",
                    models.CharField(
                        blank=True, db_column="endpointOper", max_length=255, null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Operateur",
                "verbose_name_plural": "Operateurs",
                "db_table": "operateur",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Pays",
            fields=[
                (
                    "IDPays",
                    models.AutoField(
                        db_column="IDPays", primary_key=True, serialize=False
                    ),
                ),
                (
                    "CodePays",
                    models.CharField(db_column="CodePays", max_length=5, unique=True),
                ),
                (
                    "LibPays",
                    models.CharField(
                        blank=True, db_column="LibPays", max_length=50, null=True
                    ),
                ),
                ("indicatif", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "verbose_name": "Pays",
                "verbose_name_plural": "Pays",
                "db_table": "pays",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Profil",
            fields=[
                (
                    "IDProfil",
                    models.AutoField(
                        db_column="IDProfil", primary_key=True, serialize=False
                    ),
                ),
                (
                    "CodeProfil",
                    models.CharField(
                        db_column="CodeProfil", max_length=50, unique=True
                    ),
                ),
                (
                    "DescriptionPro",
                    models.CharField(
                        blank=True, db_column="DescriptionPro", max_length=50, null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Profil",
                "verbose_name_plural": "Profils",
                "db_table": "profil",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Sens",
            fields=[
                (
                    "IDSens",
                    models.AutoField(
                        db_column="IDSens", primary_key=True, serialize=False
                    ),
                ),
                (
                    "CodeSens",
                    models.CharField(db_column="CodeSens", max_length=1, unique=True),
                ),
                (
                    "LibelleSens",
                    models.CharField(
                        blank=True, db_column="LibelleSens", max_length=50, null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Sens",
                "verbose_name_plural": "Sens",
                "db_table": "sens",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Typetransaction",
            fields=[
                (
                    "IDTypeTransaction",
                    models.AutoField(
                        db_column="IDTypeTransaction", primary_key=True, serialize=False
                    ),
                ),
                (
                    "CodeType",
                    models.CharField(db_column="CodeType", max_length=5, unique=True),
                ),
                (
                    "LibelleType",
                    models.CharField(
                        blank=True, db_column="LibelleType", max_length=50, null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Type de transaction",
                "verbose_name_plural": "Types de transaction",
                "db_table": "typetransaction",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Utilisateur",
            fields=[
                (
                    "IDUtilisateur",
                    models.AutoField(
                        db_column="IDUtilisateur", primary_key=True, serialize=False
                    ),
                ),
                (
                    "CodeUser",
                    models.CharField(db_column="CodeUser", max_length=10, unique=True),
                ),
                (
                    "NomUser",
                    models.CharField(
                        blank=True, db_column="NomUser", max_length=50, null=True
                    ),
                ),
                (
                    "UserActif",
                    models.IntegerField(blank=True, db_column="UserActif", null=True),
                ),
            ],
            options={
                "verbose_name": "Utilisateur",
                "verbose_name_plural": "Utilisateurs",
                "db_table": "utilisateur",
                "managed": False,
            },
        ),
    ]