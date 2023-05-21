from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.forms import TextInput, PasswordInput, Select, CharField, EmailInput, ModelForm
from django.contrib.auth.forms import UsernameField, AuthenticationForm, PasswordChangeForm

from agent_deposit.models import Utilisateur


"""class LoginForm(ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['CodeUser', 'password']
        labels = {
            'CodeUser': _("Code Utilisateur"),
            'password': _("Mot de passe"),
        }

        widgets = {
            'CodeUser': TextInput(attrs={'class': 'form-control form-control-user', "autofocus": True}),
            'password': PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': '***********'}),
        }
"""


class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=255,
                             widget=TextInput(
                                 attrs={'name': 'user', 'id': 'user', 'placeholder': 'Nom d\'utilisateur',
                                        'class': 'form-control form-control-user', "autofocus": True}))
    password = CharField(max_length=100,
                               widget=PasswordInput(
                                   attrs={'name': 'password', 'id': 'password', 'placeholder': 'Mot de passe',
                                          'class': 'form-control form-control-user'}))


class RegisterForm(ModelForm):
    class Meta:
        model = Utilisateur
        fields = ["CodeUser", "NomUser", "email", "CodeProfil"]
        labels = {
            'CodeUser': _("Code Utilisateur"),
            'NomUser': _("Nom d'utilisateur"),
            'email': _("Adresse mail"),
            'CodeProfil': _("Profil"),
        }

        widgets = {
            'CodeUser': TextInput(attrs={'class': 'form-control form-control-user', "autofocus": True}),
            'NomUser': TextInput(attrs={'class': 'form-control form-control-user'}),
            'email': EmailInput(attrs={'placeholder': '@', 'class': 'form-control form-control-user'}),
            'CodeProfil': Select(attrs={'class': 'form-control form-control-user'}),
        }


class ChangePasswordForm(PasswordChangeForm):
    error_messages = {
        "password_mismatch": _("Les mots de passe ne correspondent pas."),
        "password_incorrect": _(
            "Votre ancien mot de passe est incorrect. Veillez réessayer."
        ),
    }
    old_password = CharField(
        label=_("Old password"),
        strip=False,
        widget=PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, "class": "form-control form-control-user"}
        ),
    )
    new_password1 = CharField(
        label=_("New password"),
        widget=PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control form-control-user"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control form-control-user"}),
    )

