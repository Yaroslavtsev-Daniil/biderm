from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('parameters', views.parameters, name='parameters'),
    path('options', views.options, name='options'),
    path('result', views.result, name='result'),
    path('consultation', views.consultation, name='consultation'),
    path('sendcalculation', views.sendcalculation, name='sendcalculation'),
    path('thanks', views.thanks, name='thanks'),
]
