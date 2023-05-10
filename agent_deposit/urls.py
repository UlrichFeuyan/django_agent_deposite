from django.urls import path

from .views import *


app_name = 'agent_deposit'
urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('dashboard/admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('dashboard/controller_dashboard/', ControllerDashboardView.as_view(), name='controller_dashboard'),
    path('dashboard/back_office_dashboard/', BackOfficeDashboardView.as_view(), name='back_office_dashboard'),
    path('dashboard/cashier_dashboard/', CassierDashboardView.as_view(), name='cashier_dashboard'),

    path('liquide/', Liquide.as_view(), name='liquide'),
    path('virement/', Virement.as_view(), name='virement'),
    path('cheque/', Cheque.as_view(), name='cheque'),
    path('retrait/', Retrait.as_view(), name='retrait'),
    path('evenement/', Evenement.as_view(), name='evenement'),
    path('historique/', Historique.as_view(), name='historique'),
    path('404/', Error404.as_view(), name='404'),
    path('500/', Error500.as_view(), name='500'),
]
