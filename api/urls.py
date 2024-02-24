from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Mytoken.as_view(), name='token_obtain_pair'),
    path('register/', RegisterAPI.as_view(), name='user-register'),
    
    path('get-flux-entrant/', GetAllFluxEntrantsView.as_view(), name='get_fluxentrant'),
    path('get-flux-sortant/', GetAllFluxSortantView.as_view(), name='get_fluxsortant'),
    path('get-balance-generale/', GetAllBalanceGeneraleView.as_view(), name='get_balancegenerale'),
    path('get-balance-detaile/', GetAllBalanceDetaileeView.as_view(), name='get_fluxsortant'),




]
