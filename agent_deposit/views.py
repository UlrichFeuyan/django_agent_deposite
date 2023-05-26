import json
from datetime import datetime
import random
from django.http import JsonResponse, HttpResponseBadRequest
import string

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView

from SoapAPI.call_getaccountholderinformations import getAccountHolderInformations
from SoapAPI.test_soap_api_call import callApi
from .models import *


def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='ADMIN').exists()


def is_control(user):
    return user.is_authenticated and user.groups.filter(name='CONTROL').exists()


def is_back(user):
    return user.is_authenticated and user.groups.filter(name='BACK').exists()


def is_caissier(user):
    return user.is_authenticated and user.groups.filter(name='CAISSIER').exists()


class Home(TemplateView, LoginRequiredMixin):
    template_name = 'agent_deposit/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # permet d'afficher le menu de la vue Dashboard
        context['dashbord'] = 'True'
        context['dashbord_active'] = 'True'
        return context


class VersementEspece(TemplateView, UserPassesTestMixin, LoginRequiredMixin):
    template_name = 'agent_deposit/versement_espece.html'

    @method_decorator(user_passes_test(is_caissier, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dropdown_depots'] = 'True'
        context['active_liquide'] = 'True'
        return context


class Virement(TemplateView, LoginRequiredMixin):
    template_name = 'agent_deposit/virement.html'

    @method_decorator(user_passes_test(is_caissier, login_url='account:login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dropdown_depots'] = 'True'
        context['active_virement'] = 'True'
        return context


class RemiseCheque(TemplateView, LoginRequiredMixin):
    template_name = 'agent_deposit/remise_cheque.html'

    @method_decorator(user_passes_test(is_caissier, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dropdown_depots'] = 'True'
        context['active_cheque'] = 'True'
        return context


class Retrait(TemplateView, LoginRequiredMixin):
    template_name = 'agent_deposit/retrait.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['retrait_active'] = 'True'
        return context


@login_required
def voucher(request):
    if request.method == "POST":
        """
            - on vérifi que l'agent est bien actif

            - on vérifi si l'agent est déjà enregistrer dans la base de donnnées

                - si celui-ci est déjà enregistrer dans la base de donnnées, on recupère son instance pour réaliser l'opération
                - sinon, on l'enregistre au préalable

            - après avoir récupérer l'agent depuis la base de données on donne la possibilité de rappeller la vue du formulaire principal pour recupérer les autres informations

            - Ayant collecter toutes les données, on fait appel à l'api pour générer le voucher 
        """

        # Cas du VERSEMENT ESPECE
        if not (request.POST.get('identifiant_receveur') or request.POST.get('num_cheque')):
            operateur = request.POST.get('operateur')
            telephone = request.POST.get('telephone')
            CodeAgent = request.POST.get('code_agent'),

            transaction_type = Typetransaction.objects.get(CodeType="VERSP")
            sens = Sens.objects.get(CodeSens="C")
            operateur_code = Operateur.objects.get(CodeOperateur=operateur)
            agent = Agent.objects.get(CodeAgent=CodeAgent)

            voucher = operateur + telephone + datetime.now().strftime('%d%m%Y%H%M')
            # Créer une instance du modèle Evenement avec les données de la réponse
            evenement = Evenements.objects.create(
                refOrig=voucher,
                natOrig=transaction_type,
                BenOrig=CodeAgent,
                userOrig=request.user,
                DoFin='',
                dcoOrig=datetime.now().strftime('%d-%m-%Y'),
                hsaiOrig=datetime.now().strftime('%H:%M:%S'),
                sensOrig=sens,
                statutTrt='0',
                CodeOperateur=operateur_code,
                Msisdn=agent,
            )
            evenement.save()

            # Rediriger vers une page de confirmation
            return render(request, 'agent_deposit/modals/voucher.html', {'voucher': voucher})

        # Cas du virement
        if request.POST.get('identifiant_receveur'):
            operateur = request.POST.get('operateur')
            telephone = request.POST.get('telephone')
            code_banque = request.POST.get('code_banque')
            code_agence = request.POST.get('code_agence')
            montant = request.POST.get('montant')
            identifiant_receveur = request.POST.get('identifiant_receveur')
            CodeAgent = request.POST.get('code_agent'),

            # Appeler l'API SOAP

            transaction_type = Typetransaction.objects.get(CodeType="VRT")
            sens = Sens.objects.get(CodeSens="C")
            operateur_code = Operateur.objects.get(CodeOperateur=operateur)
            agent = Agent.objects.get(CodeAgent=CodeAgent)

            voucher = operateur + telephone + datetime.now().strftime('%d%m%Y%H%M')
            # Créer une instance du modèle Evenement avec les données de la réponse
            evenement = Evenements.objects.create(
                montant=montant,
                refOrig=voucher,
                natOrig=transaction_type,
                BenOrig=CodeAgent,
                userOrig=request.user,
                DoOrig=code_banque,
                Caisseorig=code_agence,
                DoFin='',
                dcoOrig=datetime.now().strftime('%d-%m-%Y'),
                hsaiOrig=datetime.now().strftime('%H:%M:%S'),
                sensOrig=sens,
                BenFIn=identifiant_receveur,
                statutTrt='0',
                CodeOperateur=operateur_code,
                Msisdn=agent,
            )
            evenement.save()

            # Rediriger vers une page de confirmation
            return render(request, 'agent_deposit/modals/voucher.html', {'voucher': voucher})

        # Cas depot de la remise de cheque
        if request.POST.get('num_cheque'):
            operateur = request.POST.get('operateur')
            telephone = request.POST.get('telephone')
            num_cheque = request.POST.get('num_cheque')
            CodeAgent = request.POST.get('code_agent'),

            transaction_type = Typetransaction.objects.get(CodeType="CHQ")
            sens = Sens.objects.get(CodeSens="C")
            operateur_code = Operateur.objects.get(CodeOperateur=operateur)
            agent = Agent.objects.get(CodeAgent=CodeAgent)

            voucher = operateur + telephone + datetime.now().strftime('%d%m%Y%H%M')
            # Créer une instance du modèle Evenement avec les données de la réponse
            evenement = Evenements.objects.create(
                refOrig=voucher,
                natOrig=transaction_type,
                BenOrig='999999898',
                userOrig=request.user,
                chqOrig=num_cheque,
                DoFin='',
                dcoOrig=datetime.now().strftime('%d-%m-%Y'),
                hsaiOrig=datetime.now().strftime('%H:%M:%S'),
                sensOrig=sens,
                statutTrt='0',
                CodeOperateur=operateur_code,
                Msisdn=agent,
            )
            evenement.save()

            # Rediriger vers une page de listing
            return render(request, 'agent_deposit/modals/voucher.html', {'voucher': voucher})
    return HttpResponseBadRequest()


def checkAgentAccount(request):
    """
    - Récupère les informations du compte par appel de l'api (getaccountholderinforamtions)
    - Vérifie si le compte est déjà présent dans la base de données afin de charger ses informations; l'enregistre dans le cas contraire
    - Vérifie si le compte agent associé au numéro est actif ou non.
        * si oui, le modal des informations du compte est appelé (succès)
        * si non, le modal signalant que le compte n'est pas valide pour réaliser l'opération est appelé (échec)
    """

    if request.method == 'POST':

        if not (request.POST.get('identifiant_receveur') or request.POST.get(
                'num_cheque')):  # vérifit que le formulaire correspond bien à celui du versement espece

            # recupère le numéro de téléphone de l'agent le nom de l'opérateur téléphonique
            telephone = request.POST.get('telephone')
            operateur = request.POST.get('operateur')

            # recupère ses informations
            agent_informations = getAccountHolderInformations(telephone)

            if agent_informations:
                # recupère et/ou ajoute l'agent dans la base de données

                agent, created = Agent.objects.get_or_create(
                    CodeAgent=agent_informations.code_agent,
                    msisdn=agent_informations.msisdn,
                    NomAgent=agent_informations.nom_agent,
                    AgentActif=agent_informations.status_agent,
                    CodeOperateur=Operateur.objects.get(CodeOperateur=operateur),
                )
                # Agent actif

                agent_data = {
                    'CodeAgent': agent_informations.code_agent,
                    'msisdn': agent_informations.msisdn,
                    'NomAgent': agent_informations.nom_agent,
                    'AgentActif': agent_informations.status_agent,
                    'typeTransaction': 'VERSP',
                }

                return request, 'agent_deposit/modals/agentIsActive.html', {'agent': agent_data}
            else:
                # Agent non actif
                return request, 'agent_deposit/modals/agentIsNotActive.html'

        if request.POST.get('identifiant_receveur'):  # Virement bancaire
            telephone = request.POST.get('telephone')
            operateur = request.POST.get('operateur')
            code_banque = request.POST.get('code_banque')
            code_agence = request.POST.get('code_agence')
            montant = request.POST.get('montant')
            identifiant_receveur = request.POST.get('identifiant_receveur')

            # recupère ses informations
            agent_informations = getAccountHolderInformations(telephone)

            if agent_informations:
                # recupère et/ou ajoute l'agent dans la base de données

                agent, created = Agent.objects.get_or_create(
                    CodeAgent=agent_informations.code_agent,
                    msisdn=agent_informations.msisdn,
                    NomAgent=agent_informations.nom_agent,
                    AgentActif=agent_informations.status_agent,
                    CodeOperateur=Operateur.objects.get(CodeOperateur=operateur),
                )
                # Agent actif

                agent_data = {
                    'CodeAgent': agent_informations.code_agent,
                    'msisdn': agent_informations.msisdn,
                    'NomAgent': agent_informations.nom_agent,
                    'AgentActif': agent_informations.status_agent,
                    'code_banque': code_banque,
                    'code_agence': code_agence,
                    'montant': montant,
                    'identifiant_receveur': identifiant_receveur,
                    'typeTransaction': 'VRT',
                }

                return request, 'agent_deposit/modals/agentIsActive.html', {'agent': agent_data}
            else:
                # Agent non actif
                return request, 'agent_deposit/modals/agentIsNotActive.html'

        if request.POST.get('num_cheque'):  # Remise cheque
            # recupère le numéro de téléphone de l'agent le nom de l'opérateur téléphonique
            telephone = request.POST.get('telephone')
            operateur = request.POST.get('operateur')
            num_cheque = request.POST.get('num_cheque')

            # recupère ses informations
            agent_informations = getAccountHolderInformations(telephone)

            if agent_informations:
                # recupère et/ou ajoute l'agent dans la base de données

                agent, created = Agent.objects.get_or_create(
                    CodeAgent=agent_informations.code_agent,
                    msisdn=agent_informations.msisdn,
                    NomAgent=agent_informations.nom_agent,
                    AgentActif=agent_informations.status_agent,
                    CodeOperateur=Operateur.objects.get(CodeOperateur=operateur),
                )

                # Agent actif
                agent_data = {
                    'CodeAgent': agent_informations.code_agent,
                    'msisdn': agent_informations.msisdn,
                    'NomAgent': agent_informations.nom_agent,
                    'AgentActif': agent_informations.status_agent,
                    'num_cheque': num_cheque,
                    'typeTransaction': 'CHQ',
                }

                return request, 'agent_deposit/modals/agentIsActive.html', {'agent': agent_data}
            else:
                # Agent non actif
                return request, 'agent_deposit/modals/agentIsNotActive.html'

    return HttpResponseBadRequest()


def agentIsActive(request):
    return (request, 'agent_deposit/modals/agentIsActive.html', locals())


def agentIsNotActive(request):
    return (request, 'agent_deposit/modals/agentIsNotActive.html', locals())


class Evenement(ListView, LoginRequiredMixin):
    model = Evenements
    template_name = 'agent_deposit/evenement.html'
    context_object_name = 'evenements'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['evenement_active'] = 'True'
        return context


class Historique(TemplateView, LoginRequiredMixin):
    template_name = 'agent_deposit/historique.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historique_active'] = 'True'
        return context


class Error404(TemplateView, LoginRequiredMixin):
    template_name = 'agent_deposit/404.html'


class Error500(TemplateView, LoginRequiredMixin):
    template_name = 'agent_deposit/500.html'
