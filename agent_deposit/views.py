from datetime import datetime
import random
import string

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView

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

    @method_decorator(user_passes_test(is_caissier, login_url=''))
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
            - on vérifie que l'agent est bien actif

            - on vérifie si l'agent est déjà enregistrer dans la base de donnnées

                - si celui-ci est déjà enregistrer dans la base de donnnées, on recupère son instance pour réaliser l'opération
                - sinon, on l'enregistre au préalable

            - après avoir récupérer l'agent depuis la base de données on donne la possibilité de rappeller la vue du formulaire principal pour recupérer les autres informations

            - Ayant collecter toutes les données, on fait appel à l'api pour générer le voucher 
        """

        # Cas du versement en espèce
        if not (request.POST.get('identifiant_receveur') or request.POST.get('num_cheque')):  # vérifit que le formulaire correspond bien à celui du versement espece
            operateur = request.POST.get('operateur')
            telephone = request.POST.get('telephone')

            # Appeler l'API SOAP
            parametre = random.randrange(999)  # valeur d'entrée; température en Fahrenheit
            print(parametre)
            url = 'https://www.w3schools.com/xml/tempconvert.asmx'  # URL de l'endpoint
            namespace = 'https://www.w3schools.com/xml/'  # namespace
            action = 'FahrenheitToCelsius'  # fonction à appeler

            response = callApi(url, namespace, action, parametre)
            if response:
                transaction_type = Typetransaction.objects.get(CodeType="VERSP")
                sens = Sens.objects.get(CodeSens="C")
                operateur_code = Operateur.objects.get(CodeOperateur=operateur)
                agent, agent_exist = Agent.objects.get_or_create(CodeOperateur=operateur_code,
                                                                 msisdn="+229" + telephone)
                voucher = operateur + telephone + datetime.now().strftime('%d%m%Y%H%M')
                # Créer une instance du modèle Evenement avec les données de la réponse
                evenement = Evenements.objects.create(
                    montant=int(float(response)) * 742,
                    refOrig=voucher,
                    natOrig=transaction_type,
                    BenOrig='999999898',
                    userOrig=request.user,
                    DoFin='',
                    dcoOrig=datetime.now().strftime('%d-%m-%Y'),
                    hsaiOrig=datetime.now().strftime('%H:%M:%S'),
                    sensOrig=sens,
                    statutTrt='0',
                    CodeOperateur=operateur_code,
                    Msisdn=agent,
                    cptOPERSide=int(float(response)),
                )
                evenement.save()

                # Rediriger vers une page de confirmation
            return render(request, 'agent_deposit/voucher.html', {'voucher': voucher})

        # Cas du virement
        if request.POST.get('identifiant_receveur'):
            operateur = request.POST.get('operateur')
            telephone = request.POST.get('telephone')
            code_banque = request.POST.get('code_banque')
            code_agence = request.POST.get('code_agence')
            montant = request.POST.get('montant')
            identifiant_receveur = request.POST.get('identifiant_receveur')

            # Appeler l'API SOAP
            parametre = random.randrange(999)  # valeur d'entrée; température en Fahrenheit
            print(parametre)
            url = 'https://www.w3schools.com/xml/tempconvert.asmx'  # URL de l'endpoint
            namespace = 'https://www.w3schools.com/xml/'  # namespace
            action = 'FahrenheitToCelsius'  # fonction à appeler

            response = callApi(url, namespace, action, parametre)
            if response:
                transaction_type = Typetransaction.objects.get(CodeType="VRT")
                sens = Sens.objects.get(CodeSens="C")
                operateur_code = Operateur.objects.get(CodeOperateur=operateur)
                agent, agent_exist = Agent.objects.get_or_create(CodeOperateur=operateur_code,
                                                                 msisdn="+229" + telephone)
                voucher = operateur + telephone + datetime.now().strftime('%d%m%Y%H%M')
                # Créer une instance du modèle Evenement avec les données de la réponse
                evenement = Evenements.objects.create(
                    montant=montant,
                    refOrig=voucher,
                    natOrig=transaction_type,
                    BenOrig='999999898',
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
                    cptOPERSide=int(float(response)),
                )
                evenement.save()

                # Rediriger vers une page de confirmation
                return render(request, 'agent_deposit/voucher.html', {'voucher': voucher})

        # Cas depot de la remise de cheque
        if request.POST.get('num_cheque'):
            operateur = request.POST.get('operateur')
            telephone = request.POST.get('telephone')
            num_cheque = request.POST.get('num_cheque')

            # Appeler l'API SOAP
            parametre = random.randrange(999)  # valeur d'entrée; température en Fahrenheit
            print(parametre)
            url = 'https://www.w3schools.com/xml/tempconvert.asmx'  # URL de l'endpoint
            namespace = 'https://www.w3schools.com/xml/'  # namespace
            action = 'FahrenheitToCelsius'  # fonction à appeler

            response = callApi(url, namespace, action, parametre)
            if response:
                transaction_type = Typetransaction.objects.get(CodeType="CHQ")
                sens = Sens.objects.get(CodeSens="C")
                operateur_code = Operateur.objects.get(CodeOperateur=operateur)
                agent, agent_exist = Agent.objects.get_or_create(CodeOperateur=operateur_code,
                                                                 msisdn="+229" + telephone)
                voucher = operateur + telephone + datetime.now().strftime('%d%m%Y%H%M')
                # Créer une instance du modèle Evenement avec les données de la réponse
                evenement = Evenements.objects.create(
                    montant=int(float(response)) * 742,
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
                    cptOPERSide=int(float(response)),
                )
                evenement.save()

                # Rediriger vers une page de listing
                return render(request, 'agent_deposit/voucher.html', {'voucher': voucher})


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
