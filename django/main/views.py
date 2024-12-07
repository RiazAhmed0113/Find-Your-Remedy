from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def home(request):
    return render(request, 'main/Home.html')


def physical_injury(request):
    return render(request, 'main/Physical_Injury.html')
