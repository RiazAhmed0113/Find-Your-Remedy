from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home/', views.home, name='home'),
    path('Physical_Injury/', views.physical_injury, name='Physical_Injury'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
