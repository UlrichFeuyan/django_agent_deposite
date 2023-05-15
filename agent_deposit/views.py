from datetime import datetime
import random

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


@method_decorator(login_required, name='dispatch')
class CassierDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'agent_deposit/dashboards/caissier_dashboard.html'

    @method_decorator(user_passes_test(is_caissier, login_url='account:login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'agent_deposit/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # permet d'afficher le menu de la vue Dashboard
        context['dashbord'] = 'True'
        context['dashbord_active'] = 'True'
        return context


@method_decorator(login_required, name='dispatch')
class VersementEspece(TemplateView, UserPassesTestMixin):
    template_name = 'agent_deposit/versement_espece.html'

    @method_decorator(user_passes_test(is_caissier, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Récupérer les données du formulaire
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
            agent, agent_exist = Agent.objects.get_or_create(CodeOperateur=operateur_code, msisdn="+229" + telephone)
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
            return redirect('agent_deposit:evenement')
        # Si la réponse de l'API est invalide, afficher une erreur
        else:
            error_msg = 'Erreur lors de l\'appel à l\'API'
            return render(request, self.template_name, {'error_msg': error_msg})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dropdown_depots'] = 'True'
        context['active_liquide'] = 'True'
        return context


@method_decorator(login_required, name='dispatch')
class Virement(TemplateView):
    template_name = 'agent_deposit/virement.html'

    @method_decorator(user_passes_test(is_caissier, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Récupérer les données du formulaire
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
            agent, agent_exist = Agent.objects.get_or_create(CodeOperateur=operateur_code, msisdn="+229" + telephone)
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
            return redirect('agent_deposit:evenement')
        # Si la réponse de l'API est invalide, afficher une erreur
        else:
            error_msg = 'Erreur lors de l\'appel à l\'API'
            return render(request, self.template_name, {'error_msg': error_msg})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dropdown_depots'] = 'True'
        context['active_virement'] = 'True'
        return context


@method_decorator(login_required, name='dispatch')
class RemiseCheque(TemplateView):
    template_name = 'agent_deposit/remise_cheque.html'

    @method_decorator(user_passes_test(is_caissier, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dropdown_depots'] = 'True'
        context['active_cheque'] = 'True'
        return context

    def post(self, request, *args, **kwargs):
        # Récupérer les données du formulaire
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
            agent, agent_exist = Agent.objects.get_or_create(CodeOperateur=operateur_code, msisdn="+229" + telephone)
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

            # Rediriger vers une page de confirmation
            return redirect('agent_deposit:evenement')
        # Si la réponse de l'API est invalide, afficher une erreur
        else:
            error_msg = 'Erreur lors de l\'appel à l\'API'
            return render(request, self.template_name, {'error_msg': error_msg})


@method_decorator(login_required, name='dispatch')
class Retrait(TemplateView):
    template_name = 'agent_deposit/retrait.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['retrait_active'] = 'True'
        return context


@method_decorator(login_required, name='dispatch')
class Evenement(ListView):
    model = Evenements
    template_name = 'agent_deposit/evenement.html'  # le template pour afficher la liste des Évènements
    context_object_name = 'evenements'  # le nom de la variable contenant la liste des Évènements dans le contexte

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['evenement_active'] = 'True'
        return context


@method_decorator(login_required, name='dispatch')
class Historique(TemplateView):
    template_name = 'agent_deposit/historique.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historique_active'] = 'True'
        return context


@method_decorator(login_required, name='dispatch')
class Error404(TemplateView):
    template_name = 'agent_deposit/404.html'


@method_decorator(login_required, name='dispatch')
class Error500(TemplateView):
    template_name = 'agent_deposit/500.html'
