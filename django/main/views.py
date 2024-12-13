from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import Illness


def home(request):

    illnesses = Illness.objects.all()

    context = {
        'illnesses' : illnesses,
    }

    return render(request, 'main/Home.html', context)


def physical_injury(request):
    return render(request, 'main/Physical_Injury.html')


def gastric_problems(request):
    return render(request, 'main/Gastric_Problems.html')


def coughs(request):
    return render(request, 'main/Coughs.html')


def pain_relief(request):
    return render(request, 'main/Pain_Relief.html')


def nausea_vomiting(request):
    return render(request, 'main/NauseaVomiting.html')


def diarrhoea_constipation(request):
    return render(request, 'main/DiarrhoeaConstipation.html')