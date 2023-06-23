from django.urls import path
from .views import viewLogin, viewSigup, viewLogout

app_name = 'CustomerUser'
urlpatterns = [
    path('', viewLogin.as_view(), name='login'),
    path('login/', viewLogin.as_view(), name='login'),
    path('signup/', viewSigup.as_view(), name='signup'),
    path('logout/', viewLogout.as_view(), name='logout'),
]