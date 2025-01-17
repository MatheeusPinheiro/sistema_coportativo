from django.urls import path,include
from contas import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('desconectado-inatividade/',  views.timeout_view, name='timeout'), 
    path('entrar/',  views.login_view, name='login'), 
    path('criar-conta/', views.register_view, name='register'), 
    path('sair/', views.logout_view, name='logout'),
    path('atualizar-usuario/', views.atualizar_meu_usuario, name='atualizar_meu_usuario'),
    path('atualizar-usuario/<slug:username>/', views.atualizar_usuario, name='atualizar_usuario'),
]