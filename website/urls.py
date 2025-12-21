from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('customers/', views.customers, name='customers'),
    path('login/', views.site_login, name='site_login'),
    path('logout/', views.site_logout, name='site_logout'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('demo/', views.demo, name='demo'),
    path('demo/success/', views.demo_success, name='demo_success'),

    # Consolidated Single Page for all 8 modules
    path('capabilities/', views.capabilities, name='capabilities'),

    # Case study
    path('case-studies/locavana/', views.locavana, name='locavana'),
]