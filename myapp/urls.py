# coding: UTF-8
from . import views
from django.urls import path
from django.conf.urls import include
 
urlpatterns = [
    path('', views.index_template, name='index'),
    path('/generic', views.generic_template, name='generic'),
    path('/elements', views.elements_template, name='elements'),
    path('/landing', views.landing_template, name='landing'),
    path('/predict_kork', views.predict_kork, name='predict_kork'),
]