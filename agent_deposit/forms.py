from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, DateInput, Select, TextInput, CharField

from agent_deposit.models import Agent


class VersementEspeceForm(ModelForm):
    model = Agent
    fields = ('CodeOperateur', 'msisdn')
    labels = {
        'CodeOperateur': _("Opérateur"),
        'msisdn': _("N° Téléphone"),
    }
    widgets = {
        'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'employe', 'type': 'text'}),
        'CodeOperateur': Select(
            attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'id_tel', 'autocomplete': 'off',
                   'data-intl-tel-input-id': '0'}),
    }
