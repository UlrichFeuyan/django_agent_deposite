from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import Utilisateur, Profil


class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'agent_deposit/dashboards/admin_dashboard.html'


class ControllerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'agent_deposit/dashboards/controller_dashboard.html'


class BackOfficeDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'agent_deposit/dashboards/back_office_dashboard.html'


class CassierDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'agent_deposit/dashboards/caissier_dashboard.html'


class Home(TemplateView):
    template_name = 'agent_deposit/home.html'


class Liquide(TemplateView):
    template_name = 'agent_deposit/liquide.html'


class Virement(TemplateView):
    template_name = 'agent_deposit/virement.html'


class Cheque(TemplateView):
    template_name = 'agent_deposit/cheque.html'


class Retrait(TemplateView):
    template_name = 'agent_deposit/retrait.html'


class Evenement(TemplateView):
    template_name = 'agent_deposit/evenement.html'


class Historique(TemplateView):
    template_name = 'agent_deposit/historique.html'


class Error404(TemplateView):
    template_name = 'agent_deposit/404.html'


class Error500(TemplateView):
    template_name = 'agent_deposit/500.html'
