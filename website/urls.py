from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('growers/', views.growers, name='growers'),
    path('food-processors/', views.food_processors, name='food_processors'),
    path('cpg-producers/', views.cpg_producers, name='cpg_producers'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('government/', views.government, name='government'),
    path('investors/', views.investors, name='investors'),
    path('ag-supply/', views.ag_supply, name='ag_supply'),
    path('contact/', views.contact, name='contact'),
]