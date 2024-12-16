from django.http import Http404
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import Illness


def home(request):
    illnesses = Illness.objects.all()

    context = {
        'illnesses': illnesses,
    }

    return render(request, 'main/Home.html', context)


def physical_injury(request):
    illnesses = Illness.objects.all()

    context = {
        'illnesses': illnesses,
    }

    return render(request, 'main/Physical Injury.html', context)


def gastric_problems(request):
    illnesses = Illness.objects.all()

    context = {
        'illnesses': illnesses,
    }

    return render(request, 'main/Gastric Problems.html', context)


def coughs(request):
    illnesses = Illness.objects.all()

    context = {
        'illnesses': illnesses,
    }

    return render(request, 'main/Coughs.html', context)


def pain_relief(request):
    illnesses = Illness.objects.all()

    context = {
        'illnesses': illnesses,
    }

    return render(request, 'main/Pain Relief.html', context)


def nausea_vomiting(request):
    illnesses = Illness.objects.all()

    context = {
        'illnesses': illnesses,
    }

    return render(request, 'main/NauseaVomiting.html', context)


def diarrhoea_constipation(request):
    illnesses = Illness.objects.all()

    context = {
        'illnesses': illnesses,
    }

    return render(request, 'main/DiarrhoeaConstipation.html', context)


def illness_view(request, illness_name):
    try:
        illness = Illness.objects.get(name=illness_name)
    except Illness.DoesNotExist:
        raise Http404(f"Illness '{illness_name}' not found")

    context = {
        'illness': illness,
    }

    return render(request, f'main/{illness_name}.html', context)
