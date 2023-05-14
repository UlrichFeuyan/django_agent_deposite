from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView

from SoapAPI.test_soap_api_call import callApi
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import Utilisateur, Profil


def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='ADMIN').exists()


def is_control(user):
    return user.is_authenticated and user.groups.filter(name='CONTROL').exists()


def is_back(user):
    return user.is_authenticated and user.groups.filter(name='BACK').exists()


def is_caissier(user):
    return user.is_authenticated and user.groups.filter(name='CAISSIER').exists()


@method_decorator(login_required, name='dispatch')
class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'agent_deposit/dashboards/admin_dashboard.html'

    @method_decorator(user_passes_test(is_admin, login_url='account:login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class ControllerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'agent_deposit/dashboards/controller_dashboard.html'

    @method_decorator(user_passes_test(is_control, login_url='account:login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class BackOfficeDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'agent_deposit/dashboards/back_office_dashboard.html'

    @method_decorator(user_passes_test(is_back, login_url='account:login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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
class VersementEspece(TemplateView):
    template_name = 'agent_deposit/versement_espece.html'

    def post(self, request, *args, **kwargs):
        # Récupérer les données du formulaire
        operateur = request.POST.get('operateur')
        telephone = request.POST.get('telephone')

        # Appeler l'API SOAP
        parametre = telephone[:3]  # valeur d'entrée; température en Fahrenheit
        print(parametre)
        url = 'https://www.w3schools.com/xml/tempconvert.asmx'  # URL de l'endpoint
        namespace = 'https://www.w3schools.com/xml/'  # namespace
        action = 'FahrenheitToCelsius'  # fonction à appeler

        response = callApi(url, namespace, action, parametre)
        print(response)

    #        Vérifier que la réponse de l'API est valide
    #        if response.status_code == 200:
    #            # Créer une instance du modèle Evenement avec les données de la réponse
    #            data = response.json()
    #            evenement = Evenement.objects.create(
    #                champ1=data['champ1'],
    #                champ2=data['champ2'],
    #                champ3=data['champ3'],
    #            )
    #            evenement.save()
    #
    #            # Rediriger vers une page de confirmation
    #            return render(request, 'confirmation.html', {'evenement': evenement})
    #
    #        # Si la réponse de l'API est invalide, afficher une erreur
    #        else:
    #            error_msg = 'Erreur lors de l\'appel à l\'API'
    #            return render(request, self.template_name, {'error_msg': error_msg})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dropdown_depots'] = 'True'
        context['active_liquide'] = 'True'
        return context


@method_decorator(login_required, name='dispatch')
class Virement(TemplateView):
    template_name = 'agent_deposit/virement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dropdown_depots'] = 'True'
        context['active_virement'] = 'True'
        return context


@method_decorator(login_required, name='dispatch')
class RemiseCheque(TemplateView):
    template_name = 'agent_deposit/remise_cheque.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dropdown_depots'] = 'True'
        context['active_cheque'] = 'True'
        return context


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
