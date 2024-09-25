from django.urls import path

from . import views

urlpatterns = [
    path('teszt', views.teszt, name='teszt'),
]