from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home/', views.home, name='home'),
    path('Physical_Injury/', views.physical_injury, name='Physical_Injury'),
    path('Gastric_Problems/', views.gastric_problems, name='Gastric_Problems'),
    path('Coughs/', views.coughs, name='Coughs'),
    path('Pain_Relief/', views.pain_relief, name='Pain_Relief'),
    path('NauseaVomiting/', views.nausea_vomiting, name='NauseaVomiting'),
    path('DiarrhoeaConstipation/', views.diarrhoea_constipation, name='DiarrhoeaConstipation'),

]
