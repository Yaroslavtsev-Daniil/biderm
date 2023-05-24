from django.shortcuts import render
from calc.models import OptionsCategory, Option, Element, BasicDimentions


def index(request):
    categories = OptionsCategory.objects.all()
    options = Option.objects.all()
    elements = Element.objects.all()
    default_dimentions = BasicDimentions.objects.get(pk=1)
    return render(request, 'calc/calc.html', {
        'categories': categories,
        'options': options,
        'elements': elements,
        'default_dimentions': default_dimentions,
    })


def contacts(request):
    return render(request, 'main/contacts.html')


def about(request):
    return render(request, 'main/about.html')
