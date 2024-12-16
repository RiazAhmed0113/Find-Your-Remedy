from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home/', views.home, name='home'),
    path('Physical Injury/', views.physical_injury, name='Physical Injury'),
    path('Gastric Problems/', views.gastric_problems, name='Gastric Problems'),
    path('Coughs/', views.coughs, name='Coughs'),
    path('Pain Relief/', views.pain_relief, name='Pain Relief'),
    path('NauseaVomiting/', views.nausea_vomiting, name='NauseaVomiting'),
    path('DiarrhoeaConstipation/', views.diarrhoea_constipation, name='DiarrhoeaConstipation'),

    path('<str:illness_name>/', views.illness_view, name='illness_view'),

]
