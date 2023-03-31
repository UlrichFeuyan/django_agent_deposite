from django.shortcuts import render
from django.views.generic import TemplateView


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
