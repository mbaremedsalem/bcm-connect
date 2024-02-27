from django.urls import path
from .views import *
from . views_bcm import *

urlpatterns = [
    path('login/', Mytoken.as_view(), name='token_obtain_pair'),
    path('register/', RegisterAPI.as_view(), name='user-register'),
    path('password/', UpdatePassword.as_view(),name='update_password'),
    
    path('get-flux-entrant/', GetAllFluxEntrantsView.as_view(), name='get_fluxentrant'),
    path('get-flux-sortant/', GetAllFluxSortantView.as_view(), name='get_fluxsortant'),
    path('get-balance-generale/', GetAllBalanceGeneraleView.as_view(), name='get_balancegenerale'),
    path('get-balance-detaile/', GetAllBalanceDetaileeView.as_view(), name='get_fluxsortant'),

    ####-------------- balance generale -----------#### 
    path('envoye-balance-generale-hebdomodaire/', EnvoyeBalanceGeneraleHebdomodaireAPIView.as_view(), name='post-balance-hebdomodaire'),
    path('envoye-balance-generale-mensuelle/', EnvoyeBalanceGeneraleMensuelleAPIView.as_view(), name='post-balance-mensuelle'),
    path('envoye-balance-generale-anuelle/', EnvoyeBalanceGeneraleAnnuelleAPIView.as_view(), name='post-balance-anuelle'),

    #### ---------------- balance detaille ---------#####
    path('envoye-balance-detaile-mensuelle/', EnvoyeBalanceDetailleMenuelleAPIView.as_view(), name='post-balance-detaille-mensuelle'),
    path('envoye-balance-generale-anuelle/', EnvoyeBalanceDetailleAnnuelleAPIView.as_view(), name='post-balance-detaille-anuelle'),
    
    #### ------------------ flux ---------------#########
    path('envoye-flux-sortant/', EnvoyeFluxSortantAPIView.as_view(), name='post-flux-sortant'),
    path('envoye-flux-entrant/', EnvoyeFluxEntrantAPIView.as_view(), name='post-flux-entrant'),

    ####-----------------credit documentaire -----########
    path('envoye-credit-documentaire/', EnvoyeCreditDocumentaireAPIView.as_view(), name='post-credit-documentaire'),
    ####-----------------envoye echeance ---------########
    path('envoye-echeance/', EnvoyeecheanceAPIView.as_view(), name='post-echeance'),   
    ####-----------------envoye relevé du compte ---------########
    path('envoye-releve-compte/', EnvoyeecheanceAPIView.as_view(), name='post-releve-compte'),

]
