from django.contrib.auth.models import Group
from .models import Profil

side_bar_admin = {
    # permet d'afficher le menu de la vue Dashboard
    'dashbord': 'True',

    # permet d'afficher le menu des vues des différentes transactions
    'transaction': 'True',

    # permet d'afficher le menu des vues des des transactions sur la journée et l'historique des opérations
    'retracement': 'True',
}

side_bar_back_office = {
    # permet d'afficher le menu de la vue Dashboard
    'dashbord': 'True',

    # permet d'afficher le menu des vues des des transactions sur la journée et l'historique des opérations
    'retracement': 'True',
}

side_bar_controleur = {
    # permet d'afficher le menu des vues des des transactions sur la journée et l'historique des opérations
    'retracement': 'True',
}

side_bar_caissier = {
    # permet d'afficher le menu des vues des différentes transactions
    'transaction': 'True',

    # permet d'afficher le menu des vues des des transactions sur la journée et l'historique des opérations
    'retracement': 'True',
}


def profil_context_processor(request):
    # Récupérer le profil de l'utilisateur courant
    profil = None
    if request.user.is_authenticated:
        profil = request.user.CodeProfil

    # Ajouter les informations pertinentes pour ce profil au contexte
    context = {}
    if profil:
        context['profil'] = profil.to_dict()
        if profil.CodeProfil == 'ADMIN':
            context.update(side_bar_admin)
        elif profil.CodeProfil == 'BACK':
            context.update(side_bar_back_office)
        elif profil.CodeProfil == 'CONTROL':
            context.update(side_bar_controleur)
        elif profil.CodeProfil == 'CAISSIER':
            context.update(side_bar_caissier)

    return context

