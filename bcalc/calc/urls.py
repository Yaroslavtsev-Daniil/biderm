from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('calc', views.calc, name='calc'),
    path('result', views.result, name='result'),
    path('consultation', views.consultation, name='consultation'),
    path('sendcalculation', views.sendcalculation, name='sendcalculation'),
    path('thanks', views.thanks, name='thanks'),
]
