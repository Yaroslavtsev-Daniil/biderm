from django.shortcuts import render
from .models import OptionsCategory, Option, Element


def start(request):
    return render(request, 'calc/start.html')


def calc(request):
    categories = OptionsCategory.objects.all()
    options = Option.objects.all()
    elements = Element.objects.all()
    return render(request, 'calc/calc.html', {
        'categories': categories,
        'options': options,
        'elements': elements,
    })


def result(request):
    return render(request, 'calc/result.html')


def consultation(request):
    return render(request, 'calc/consultation.html')


def sendcalculation(request):
    return render(request, 'calc/sendcalculation.html')


def thanks(request):
    return render(request, 'calc/thanks.html')

