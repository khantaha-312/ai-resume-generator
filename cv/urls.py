# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('template1/', views.template1, name='template1'),
    path('template2/', views.template2, name='template2'),
    path('template3/', views.template3, name='template3'),
    path('update_objective/', views.update_objective, name='update_objective'),

]