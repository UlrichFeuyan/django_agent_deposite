from django.contrib import messages
from django.conf import settings as django_settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, CreateView

from account.forms import LoginForm
from agent_deposit.models import Utilisateur


@login_required
def redirect_user(request):
    user_profile = request.user.CodeProfil.CodeProfil
    try:
        if user_profile == 'ADMIN':
            return redirect('agent_deposit:admin_dashboard')
        elif user_profile == 'CONTROL':
            return redirect('agent_deposit:controller_dashboard')
        elif user_profile == 'BACK':
            return redirect('agent_deposit:back_office_dashboard')
        elif user_profile == 'CAISSIER':
            return redirect('agent_deposit:cashier_dashboard')
        else:
            return redirect('agent_deposit:home')
    except:
        pass


class Login(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        messages.success(self.request, f'Connexion réussie !')
        context.update(
            {
                self.redirect_field_name: self.get_redirect_url(),
                "site": current_site,
                "site_name": current_site.name,
                **(self.extra_context or {}),
                "messages": messages,
            }
        )
        return context


class Register(View):

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'account/register.html', locals())

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')


class ChangePassword(PasswordChangeView):
    template_name = "account/change-password.html"
    title = _("Modifier le mot de passe")
    success_url = reverse_lazy("account:profil")


class Profil(DetailView):
    model = Utilisateur
    template_name_field = "account/profil.html"
