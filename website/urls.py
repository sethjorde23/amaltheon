from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Contact & Demo
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('demo/', views.demo, name='demo'),
    path('demo/success/', views.demo_success, name='demo_success'),
    path('about/', views.about, name='about'),
    path('login/', views.site_login, name='site_login'),
    path('logout/', views.site_logout, name='site_logout'),

    # Customer segments
    path('growers/', views.growers, name='growers'),
    path('food-processors/', views.food_processors, name='food_processors'),
    path('cpg-producers/', views.cpg_producers, name='cpg_producers'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('government/', views.government, name='government'),
    path('investors/', views.investors, name='investors'),
    path('ag-supply/', views.ag_supply, name='ag_supply'),
]