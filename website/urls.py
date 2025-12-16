from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.site_login, name='site_login'),
    path('logout/', views.site_logout, name='site_logout'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('demo/', views.demo, name='demo'),
    path('demo/success/', views.demo_success, name='demo_success'),

    # Customer pages
    path('growers/', views.growers, name='growers'),
    path('food-processors/', views.food_processors, name='food_processors'),
    path('cpg-producers/', views.cpg_producers, name='cpg_producers'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('government/', views.government, name='government'),
    path('investors/', views.investors, name='investors'),
    path('ag-supply/', views.ag_supply, name='ag_supply'),

    # Capability pages
    path('capabilities/custom-software/', views.custom_software, name='custom_software'),
    path('capabilities/ai-integration/', views.ai_integration, name='ai_integration'),
    path('capabilities/pricing-intelligence/', views.pricing_intelligence, name='pricing_intelligence'),
    path('capabilities/demand-forecasting/', views.demand_forecasting, name='demand_forecasting'),
    path('capabilities/buyer-supplier-network/', views.buyer_supplier_network, name='connections'),
    path('capabilities/crop-planning/', views.crop_planning, name='crop_planning'),
    path('capabilities/seasonal-planning/', views.seasonal_planning, name='seasonal_planning'),
    path('capabilities/profitability-analysis/', views.profitability_analysis, name='profitability_analysis'),
]