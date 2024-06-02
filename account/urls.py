from django.urls import path
from . import views

app_name='account_app'
urlpatterns = [
    path('login', views.User_login,name='login'),
    path('logout', views.User_logout,name='logout'),
]
