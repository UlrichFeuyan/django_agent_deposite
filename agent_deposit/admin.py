from django.contrib import admin

from agent_deposit.models import *

admin.site.register(Agent)
admin.site.register(Codebank)
admin.site.register(Comptes)
admin.site.register(Evenements)
admin.site.register(Historique)
admin.site.register(Operateur)
admin.site.register(Pays)
admin.site.register(Sens)
admin.site.register(Typetransaction)
admin.site.register(Profil)


@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['NomUser', 'IDUtilisateur', 'CodeUser', 'UserActif', 'CodeProfil']
    list_filter = ['UserActif', 'CodeProfil']
    list_select_related = True
    prepopulated_fields = {"username": ("NomUser",)}
