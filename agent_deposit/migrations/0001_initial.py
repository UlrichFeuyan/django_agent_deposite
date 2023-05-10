# Generated by Django 4.1.7 on 2023-05-09 10:17

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Utilisateur",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
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
                "managed": True,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
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
                "managed": True,
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
                "managed": True,
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
                "managed": True,
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
                "managed": True,
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
                "verbose_name": "Profile",
                "verbose_name_plural": "Profiles",
                "db_table": "profil",
                "managed": True,
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
                "managed": True,
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
                "managed": True,
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
                (
                    "CodePays",
                    models.ForeignKey(
                        blank=True,
                        db_column="CodePays",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="agent_deposit.pays",
                        to_field="CodePays",
                    ),
                ),
            ],
            options={
                "verbose_name": "Operateur",
                "verbose_name_plural": "Operateurs",
                "db_table": "operateur",
                "managed": True,
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
                (
                    "CodeOperateur",
                    models.ForeignKey(
                        blank=True,
                        db_column="CodeOperateur",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="agent_deposit.operateur",
                        to_field="CodeOperateur",
                    ),
                ),
                (
                    "Msisdn",
                    models.ForeignKey(
                        blank=True,
                        db_column="Msisdn",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="agent_deposit.agent",
                        to_field="msisdn",
                    ),
                ),
                (
                    "natOrig",
                    models.ForeignKey(
                        blank=True,
                        db_column="natOrig",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="agent_deposit.typetransaction",
                        to_field="CodeType",
                    ),
                ),
                (
                    "sensOrig",
                    models.ForeignKey(
                        blank=True,
                        db_column="sensOrig",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="agent_deposit.sens",
                        to_field="CodeSens",
                    ),
                ),
                (
                    "userOrig",
                    models.ForeignKey(
                        blank=True,
                        db_column="userOrig",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                        to_field="CodeUser",
                    ),
                ),
            ],
            options={
                "verbose_name": "Evenement",
                "verbose_name_plural": "Evenements",
                "db_table": "evenements",
                "managed": True,
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
                (
                    "CodeBank",
                    models.ForeignKey(
                        blank=True,
                        db_column="CodeBank",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="agent_deposit.codebank",
                        to_field="CodeBank",
                    ),
                ),
            ],
            options={
                "verbose_name": "Compte",
                "verbose_name_plural": "Comptes",
                "db_table": "comptes",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="agent",
            name="CodeOperateur",
            field=models.ForeignKey(
                blank=True,
                db_column="CodeOperateur",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="agent_deposit.operateur",
                to_field="CodeOperateur",
            ),
        ),
        migrations.AddField(
            model_name="utilisateur",
            name="CodeProfil",
            field=models.ForeignKey(
                blank=True,
                db_column="CodeProfil",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="agent_deposit.profil",
                to_field="CodeProfil",
            ),
        ),
        migrations.AddField(
            model_name="utilisateur",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="utilisateur",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
