'''
Created on Mar. 25, 2022

@author: Louis-Philippe
'''
# System libraries
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.get_url, name='get_url'),
    path('test', views.not_in_systeme, name='not_in_systeme'),
]

