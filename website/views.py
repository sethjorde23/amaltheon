from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, DemoRequestForm

SITE_PASSWORD = "data"

# ============================================
# Core Page Views
# ============================================

def home(request):
    if not request.session.get('site_authenticated'):
        return redirect('site_login')
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def customers(request):
    return render(request, 'website/customers.html')

# ============================================
# Modular Capabilities (One-Page Layout)
# ============================================

def capabilities(request):
    """
    Renders the unified modular capabilities page showing the 8 standalone modules.
    """
    CAPABILITY_SUITES = [
        {
            'name': 'Software Development',
            'tagline': 'The Engine of Operations',
            'capabilities': [
                {
                    'id': 'custom-software',
                    'title': 'Custom Software & Dashboards',
                    'desc': 'Purpose-built tools that fit how you actually work.',
                    'examples': [
                        'Native Mobile Apps',
                        'Custom IMS Dashboards',
                        'Aisle-by-Aisle Pickers'
                    ]
                },
                {
                    'id': 'ai-agents',
                    'title': 'AI Agents',
                    'desc': 'Practical AI integrated into your data fabric to automate logic.',
                    'examples': [
                        'Promotion Strategy Bots',
                        'Automated Reorder Logic',
                        'Labor Spend Analyzers'
                    ]
                }
            ]
        },
        {
            'name': 'Market Intelligence',
            'tagline': 'Total System Visibility',
            'capabilities': [
                {
                    'id': 'pricing-intel',
                    'title': 'Pricing Intelligence',
                    'desc': 'Real-time transaction data revealing true market pricing.',
                    'examples': [
                        'Price Benchmarking',
                        'Competitor Spot-Tracking',
                        'Margin Protection Alerts'
                    ]
                },
                {
                    'id': 'network',
                    'title': 'Buyer/Supplier Network',
                    'desc': 'Spatial mapping and CRM to discover and manage partners.',
                    'examples': [
                        'Interactive Supplier Maps',
                        'Zip-Code Delivery Zones',
                        'Spatial CRM Notes'
                    ]
                }
            ]
        },
        {
            'name': 'Predictive Analytics',
            'tagline': 'Anticipate Market Shifts',
            'capabilities': [
                {
                    'id': 'forecasting',
                    'title': 'Demand Forecasting',
                    'desc': 'Merging historical patterns with real-time supply signals to see where the market is headed.',
                    'examples': [
                        'Volume Surge Predictions',
                        'Regional Demand Heatmaps',
                        'Inventory Velocity Modeling'
                    ]
                },
                {
                    'id': 'seasonal',
                    'title': 'Seasonal Planning',
                    'desc': 'Synchronizing procurement and menus with regional availability and price cycles.',
                    'examples': [
                        'Availability Calendars',
                        'Yield Gap Analysis',
                        'Weather-Risk Modeling'
                    ]
                }
            ]
        },
        {
            'name': 'Strategic Planning',
            'tagline': 'Maximize Your Margin',
            'capabilities': [
                {
                    'id': 'crop-planning',
                    'title': 'Crop Planning',
                    'desc': 'Using market demand and pricing data to optimize planting decisions.',
                    'examples': [
                        'Market-Driven Sowing Rates',
                        'Harvest Timing Windows',
                        'Varietal Margin Projections'
                    ]
                },
                {
                    'id': 'profitability',
                    'title': 'Profitability Analysis',
                    'desc': 'Pinpointing exactly where margin is being lost across your supply chain.',
                    'examples': [
                        'Unit Economic Tracking',
                        'Route Efficiency Audits',
                        'Waste Reduction Analytics'
                    ]
                }
            ]
        }
    ]

    return render(request, 'website/capabilities.html', {'suites': CAPABILITY_SUITES})

# ============================================
# Case Study Data
# ============================================

LOCAVANA_DATA = {
    'name': 'Locavana',
    'subtitle': 'The Ghost Grocery OS: Pairing a Modern Consumer App with Automated Operational Efficiency',
    'industry': 'Ghost Grocery & Logistics',
    'location': 'West Michigan',
    'challenge': 'Locavana needed a modern consumer experience and custom software to automate operations, creating the maximum efficiency required to deliver the best price-to-value on the market.',
    'features': [
        {
            'title': 'Native Full-Basket Commerce',
            'desc': 'We built a custom, modern ecommerce experience through a native mobile app designed for high-velocity shopping. The UI digitizes a structured "Aisle-by-Aisle" flow, allowing users to build complex grocery baskets faster than traditional web-responsive tools.',
            'img_id': 'img_storefront'
        },
        {
            'title': 'Intelligence Core: Autonomous Agents',
            'desc': 'Our AI agents are integrated into the entire company’s data fabric. Management uses conversational intelligence to ask: "Which slow-moving products should we run promotions on to maximize shelf velocity?" or "Analyze city-level pickup clusters relative to labor spend".',
            'img_id': 'img_ai_agent'
        },
        {
            'title': 'Interactive Supplier CRM',
            'desc': 'We replaced fragmented lists with a spatial data layer. This interactive map visualizes the supplier network as dynamic nodes where managers click to view real-time CRM history and input field notes directly on the map.',
            'img_id': 'img_map'
        },
        {
            'title': 'Automated Inventory & Barcoding',
            'desc': 'To drive down working capital and ensure availability, we built a custom IMS with native scanning. Every SKU is tracked from intake to picking, featuring fully automated alerts and reorder triggers based on real-time velocity thresholds.',
            'img_id': 'img_ims'
        }
    ],
    'results': [
        {
            'metric': 'Top 1%',
            'title': 'Market Price-to-Value',
            'description': 'Achieved through extreme operational efficiency.'
        },
        {
            'metric': '40%',
            'title': 'Lower Working Capital',
            'description': 'Automated reorder logic minimized overstock.'
        },
        {
            'metric': 'Zero',
            'title': 'Inventory Variance',
            'description': 'Barcode precision eliminated stock-outs.'
        },
        {
            'metric': '3x',
            'title': 'Checkout Velocity',
            'description': 'Aisle-by-aisle UX increased basket build speed.'
        }
    ],
    'quote': {
        'text': 'Amaltheon didn’t just give us a tool; they gave us a digital nervous system. We now operate with a precision that allows us to beat the market on price and the nationals on technology.',
        'author': 'Sarah Chen',
        'role': 'CEO, Locavana',
    },
}

# ============================================
# Helper Views
# ============================================

def locavana(request):
    return render(request, 'website/case_study_detail.html', {'case_study': LOCAVANA_DATA})

def site_login(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == SITE_PASSWORD:
            request.session['site_authenticated'] = True
            return redirect('home')
        else:
            messages.error(request, 'Incorrect password')
    return render(request, 'website/site_login.html')

def site_logout(request):
    request.session['site_authenticated'] = False
    return redirect('site_login')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! We'll be in touch soon.")
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'website/contact_success.html')

def demo(request):
    if request.method == 'POST':
        form = DemoRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! We'll reach out within 1 business day.")
            return redirect('demo_success')
    else:
        form = DemoRequestForm()
    return render(request, 'website/demo.html', {'form': form})

def demo_success(request):
    return render(request, 'website/demo_success.html')