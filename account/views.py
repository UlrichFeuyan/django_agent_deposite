from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.views import View
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from account.forms import RegisterForm, LoginForm
from agent_deposit.models import Utilisateur
from core.settings import LOGIN_REDIRECT_URL

"""
def login_user(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            CodeUser = form.cleaned_data['CodeUser']
            password = form.cleaned_data['password']
            print(f"{CodeUser} : {password}")
            try:
                print("before getting utilisateur")
                utilisateur = Utilisateur.objects.get(CodeUser=CodeUser)
                print(utilisateur)
                if utilisateur:
                    username = utilisateur.username
                    print(username)
                    print("before authentication")
                    user = authenticate(username=username, password=password)
                    print(user)
                    if user is not None:
                        if user.is_active:
                            login(request, user)
                            print("before redirection")
                            return redirect(LOGIN_REDIRECT_URL)
            except:
                print("Aucun utilisateur trouvé")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


class Login(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'account/login.html', locals())

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            CodeUser = form.cleaned_data['CodeUser']
            password = form.cleaned_data['password']
            print(f"{CodeUser} : {password}")
            try:
                utilisateur = Utilisateur.objects.get(CodeUser=CodeUser)
                print(utilisateur)
                if utilisateur:
                    username = utilisateur.username
                    print(username)
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        if user.is_active:
                            login(request, user)
                            return redirect('account:profil')
            except:
                print("Aucun utilisateur trouvé")
                return redirect('account:login')
        else:
            print('formulaire incorrect')
            return redirect('account:login')
"""


class Login(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"
    redirect_authenticated_user = True


class Register(View):

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'account/register.html', locals())

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')


@method_decorator(login_required, name='dispatch')
class ChangePassword(PasswordChangeView):
    template_name = "account/change-password.html"
    title = _("Modifier le mot de passe")
    success_url = reverse_lazy("account:profil")


@login_required
def profil(request):
    context = {'user': request.user}
    return render(request, 'account/profil.html', context)


@login_required
def users(request):
    return render(request, 'account/users.html')


@login_required
def user_list(request):
    return render(request, 'account/user_list.html', {
        'users': Utilisateur.objects.all(),
    })


@login_required
def add_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "movieListChanged": None,
                        "showMessage": f"{user.CodeUser} Ajouté."
                    })
                })
    else:
        form = RegisterForm()
    return render(request, 'account/user_form.html', {
        'form': form,
    })


@login_required
def edit_user(request, pk):
    user = get_object_or_404(Utilisateur, CodeUser=pk)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "movieListChanged": None,
                        "showMessage": f"{user.CodeUser} Modifié."
                    })
                }
            )
    else:
        form = RegisterForm(instance=user)
    return render(request, 'account/user_form.html', {
        'form': form,
        'utilisateur': user,
    })


@login_required
def remove_user(request, pk):
    user = get_object_or_404(Utilisateur, CodeUser=pk)
    user.UserActif = False
    user.save()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "movieListChanged": None,
                "showMessage": f"{user.CodeUser} Supprimé."
            })
        })
