from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'human_resource'
urlpatterns = [
    path('', views.index, name='index'),
    path('staff_money/', views.staff_money, name='staff_money'),
    path('squad_money/', views.squad_money, name='squad_money'),
    path('project_money/', views.project_money, name='project_money'),
    path('available_hr/', views.available_hr, name='available_hr'),
    path('project_timeline/', views.project_timeline, name='project_timeline'),
]
