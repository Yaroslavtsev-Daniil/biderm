from django.shortcuts import render


def start(request):
    return render(request, 'calc/start.html')


def calc(request):
    return render(request, 'calc/calc.html')


def result(request):
    return render(request, 'calc/result.html')


def consultation(request):
    return render(request, 'calc/consultation.html')


def sendcalculation(request):
    return render(request, 'calc/sendcalculation.html')


def thanks(request):
    return render(request, 'calc/thanks.html')

