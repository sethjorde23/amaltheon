from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def growers(request):
    return render(request, 'website/growers.html')

def food_processors(request):
    return render(request, 'website/food_processors.html')

def cpg_producers(request):
    return render(request, 'website/cpg_producers.html')

def restaurants(request):
    return render(request, 'website/restaurants.html')

def government(request):
    return render(request, 'website/government.html')

def investors(request):
    return render(request, 'website/investors.html')

def ag_supply(request):
    return render(request, 'website/ag_supply.html')

def contact(request):
    return render(request, 'website/contact.html')