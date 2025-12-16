from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, DemoRequestForm

SITE_PASSWORD = "data"

def home(request):
    if not request.session.get('site_authenticated'):
        return redirect('site_login')
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

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

def customer_detail(request, customer_data):
    return render(request, 'website/customer_detail.html', {'customer': customer_data})

def capability_detail(request, capability_data):
    return render(request, 'website/capability_detail.html', {'capability': capability_data})

# Customer Data
GROWERS_DATA = {
    'name': 'Growers',
    'badge': 'Intelligence for Producers',
    'headline': 'Know what to plant, when to sell, and who to sell to',
    'description': 'Demand forecasting, price optimization, and buyer matching powered by real market data. Stop planting blind.',
    'decisions': [
        'What should I plant this season given my soil, climate, and local demand?',
        'Where is demand headed in the next 30/60/90 days?',
        'Am I getting fair prices compared to the market?',
        'Which buyers should I build relationships with?',
        'Should I expand acreage or diversify crops?',
    ],
    'capabilities': [
        {
            'title': 'Planning & Forecasting',
            'items': [
                'Crop recommendation engine based on location, soil type, microclimate, and real-time demand',
                'Seasonal demand forecasting by crop and region',
                'Historical yield benchmarking against similar operations',
                'Climate risk modeling: frost dates, precipitation trends, growing degree days',
            ]
        },
        {
            'title': 'Market Intelligence',
            'items': [
                'Real-time pricing across local buyers (processors, restaurants, marketplaces)',
                'Demand alerts when buyers are looking for what you grow',
                'Price trend analysis: spot rising demand before competitors',
                'Buyer quality scoring: payment reliability, volume consistency',
            ]
        },
        {
            'title': 'Operations',
            'items': [
                'Inventory and harvest tracking',
                'Simple logistics coordination',
                'Yield recording and season-over-season comparison',
                'Cash flow forecasting based on expected harvest and pricing',
            ]
        },
        {
            'title': 'Sales & Relationships',
            'items': [
                'Buyer matching based on crop mix and capacity',
                'Contract opportunity alerts',
                'Negotiation support: know the market rate before you quote',
            ]
        },
    ],
    'questions': [
        "I have 50 acres in Kent County - what's the highest-margin crop mix for next season?",
        "Tomato prices are dropping - should I hold inventory or sell now?",
        "Which restaurants within 100 miles are actively sourcing local peppers?",
        "How does my yield per acre compare to similar farms in my region?",
        "What's the 3-year demand trend for organic leafy greens in my area?",
    ],
    'problems': [
        {
            'title': 'Planting blind',
            'description': "Decisions based on last year's prices and gut instinct. No visibility into what buyers actually need until it's too late.",
        },
        {
            'title': 'Price discovery is broken',
            'description': "You don't know if you're getting fair value. Buyers have more information than you do.",
        },
        {
            'title': 'Missed opportunities',
            'description': "Demand exists for what you grow, but you don't know who's buying or when they need it.",
        },
    ],
}

FOOD_PROCESSORS_DATA = {
    'name': 'Food Processors',
    'badge': 'Intelligence for Processing',
    'headline': 'Match capacity to real demand',
    'description': 'Sourcing intelligence, production scheduling, and downstream visibility to optimize every run. Stop guessing at capacity.',
    'decisions': [
        'What capacity should I reserve for which products this quarter?',
        'Which growers should I contract with, and at what volumes?',
        'Am I paying competitive rates for raw inputs?',
        'When will supply shortages hit, and how do I get ahead of them?',
        'Where is downstream demand heading - should I expand a product line?',
    ],
    'capabilities': [
        {
            'title': 'Capacity Planning',
            'items': [
                'Production scheduling aligned to real upstream supply and downstream orders',
                'Seasonal capacity modeling: know your bottlenecks before they hit',
                'Scenario planning: what if tomato supply drops 20%?',
                'Utilization benchmarking against similar operations',
            ]
        },
        {
            'title': 'Sourcing Intelligence',
            'items': [
                'Real-time visibility into grower availability by crop, region, and quality tier',
                'Supplier discovery: find new growers before your competitors do',
                'Price benchmarking across your supplier base and the broader market',
                'Supplier reliability scoring: delivery consistency, quality variance',
            ]
        },
        {
            'title': 'Demand Visibility',
            'items': [
                'Order trend analysis from CPG, restaurant, and retail buyers',
                'Demand forecasting by product category',
                'Customer concentration risk alerts',
                'New buyer identification: who is scaling and needs a processor?',
            ]
        },
        {
            'title': 'Operations',
            'items': [
                'Inventory management across raw inputs and finished goods',
                'Waste reduction analytics: identify patterns in spoilage',
                'ERP integration or lightweight replacement for smaller operations',
                'Traceability and lot tracking',
            ]
        },
    ],
    'questions': [
        "I have 30% excess capacity in Q3 - which products should I push?",
        "Three of my tomato suppliers are at risk - who else can I source from?",
        "Am I paying more for apples than other processors in the region?",
        "Which restaurant groups are growing fastest and need processing partners?",
        "What's the demand outlook for frozen local vegetables over the next 12 months?",
    ],
    'problems': [
        {
            'title': 'Capacity guesswork',
            'description': 'Over-commit or under-utilize. No real-time signal on upstream supply or downstream demand to plan production.',
        },
        {
            'title': 'Supplier blind spots',
            'description': "You don't know what's available until you call around. Competitors are locking up supply while you're still sourcing.",
        },
        {
            'title': 'Demand opacity',
            'description': "You see orders, not trends. No early warning on which buyers are scaling or which product lines are declining.",
        },
    ],
}

CPG_PRODUCERS_DATA = {
    'name': 'CPG Producers',
    'badge': 'Intelligence for Brands',
    'headline': 'Secure supply before your competitors',
    'description': 'Ingredient monitoring, supplier diversification, and cost structure intelligence. Stop scrambling for supply.',
    'decisions': [
        'Where should I source ingredients to balance cost, quality, and reliability?',
        'How do I reduce supply chain risk without bloating inventory?',
        "What's happening to input costs, and when should I lock in contracts?",
        'Which local/regional suppliers can scale with me?',
        "Where are my competitors sourcing, and what's their cost structure?",
    ],
    'capabilities': [
        {
            'title': 'Supply Chain Intelligence',
            'items': [
                'Ingredient availability tracking across regions and seasons',
                'Price trend monitoring with forward-looking indicators',
                'Supplier diversification recommendations: reduce single-source risk',
                'Disruption alerts: weather events, logistics issues, capacity constraints',
            ]
        },
        {
            'title': 'Sourcing & Procurement',
            'items': [
                'Supplier discovery and qualification: find local producers who meet your specs',
                'RFQ optimization: know the market before you negotiate',
                'Contract timing intelligence: when to lock in vs. stay spot',
                'Quality and reliability scoring across your supplier base',
            ]
        },
        {
            'title': 'Competitive Intelligence',
            'items': [
                'Sourcing pattern analysis: where are competitors buying?',
                'Cost structure benchmarking',
                'New product trend identification based on emerging supply',
                'Regional supply advantage mapping',
            ]
        },
        {
            'title': 'Product Development',
            'items': [
                'Ingredient availability analysis for new product concepts',
                'Local/regional sourcing feasibility studies',
                'Seasonal product planning based on supply cycles',
                'Specialty ingredient sourcing (organic, non-GMO, etc.)',
            ]
        },
    ],
    'questions': [
        "Which farms can supply 50,000 lbs of organic blueberries annually?",
        "Honey prices are spiking - is this temporary or structural?",
        "My main tomato supplier is at capacity - who else meets my quality specs?",
        "What local ingredients are underutilized and could differentiate a new product?",
        "How does my ingredient cost basis compare to regional competitors?",
    ],
    'problems': [
        {
            'title': 'Supply surprises',
            'description': "You discover shortages after they've hit. No early warning, no alternative sourcing intelligence.",
        },
        {
            'title': 'Single-source risk',
            'description': "Your supply chain is concentrated. You know it's a problem but don't have visibility into alternatives.",
        },
        {
            'title': 'Cost disadvantage',
            'description': "Competitors are getting better pricing or locking up supply. You're always a step behind.",
        },
    ],
}

RESTAURANTS_DATA = {
    'name': 'Restaurants',
    'badge': 'Intelligence for Foodservice',
    'headline': "Build menus around what's actually available",
    'description': 'Seasonal planning, supplier discovery, and procurement optimization. Stop scrambling for ingredients.',
    'decisions': [
        "What should be on my menu this season based on what's actually available?",
        'Which local suppliers are reliable and fairly priced?',
        'When should I buy, and how much, to minimize waste and cost?',
        'How do I tell a compelling local sourcing story to customers?',
        'Where can I find specialty or hard-to-source local ingredients?',
    ],
    'capabilities': [
        {
            'title': 'Menu Planning',
            'items': [
                'Seasonal availability calendars by ingredient and region',
                'Menu optimization based on price, availability, and margin',
                'Ingredient substitution recommendations when supply is tight',
                'Trend analysis: what local ingredients are gaining popularity?',
            ]
        },
        {
            'title': 'Supplier Management',
            'items': [
                'Local supplier discovery and qualification',
                'Price benchmarking across vendors',
                'Reliability and quality scoring',
                'Consolidated ordering across multiple farms and producers',
            ]
        },
        {
            'title': 'Procurement Intelligence',
            'items': [
                'Price alerts: buy when costs dip',
                "Availability forecasting: know what's coming and what's ending",
                'Volume discount opportunities through aggregated demand',
                'Waste reduction analytics: align ordering to actual usage',
            ]
        },
        {
            'title': 'Marketing & Storytelling',
            'items': [
                'Sourcing documentation for menu transparency',
                'Farm and producer profiles for customer-facing content',
                'Local sourcing certification and tracking',
                'Sustainability metrics and reporting',
            ]
        },
    ],
    'questions': [
        "What local proteins are available within 50 miles at under $8/lb?",
        "Heirloom tomato season is ending - what should I pivot to?",
        "Am I paying market rate for my microgreens?",
        "Which farms can reliably supply a 3-location restaurant group?",
        "What's the story behind the farm supplying my pork?",
    ],
    'problems': [
        {
            'title': 'Menu misalignment',
            'description': "Your menu doesn't match what's actually available. You're 86ing dishes or compromising on quality.",
        },
        {
            'title': 'Supplier chaos',
            'description': 'Too many calls, too many invoices, no way to compare pricing or reliability.',
        },
        {
            'title': 'Story gaps',
            'description': "Customers want local. You're sourcing local. But you can't tell the story because you don't have the data.",
        },
    ],
}

GOVERNMENT_DATA = {
    'name': 'Government & Institutions',
    'badge': 'Intelligence for Policy',
    'headline': 'See the food system clearly',
    'description': 'Policy modeling, food access mapping, and infrastructure investment optimization. Make decisions with real data.',
    'decisions': [
        'Where are the gaps in local food access, and how do we close them?',
        'Which subsidies and programs are actually moving the needle?',
        'How do we measure the health of our regional food system?',
        'Where should we invest infrastructure dollars for maximum impact?',
        'How do we prepare for supply disruptions or food security risks?',
    ],
    'capabilities': [
        {
            'title': 'Policy Analysis & Modeling',
            'items': [
                'Impact modeling for subsidy and incentive programs',
                'SNAP and food assistance program optimization',
                'Trade flow analysis: imports, exports, and regional self-sufficiency',
                'Scenario planning for policy changes',
            ]
        },
        {
            'title': 'Food System Mapping',
            'items': [
                'Supply and demand visualization by region, crop, and channel',
                'Food desert and access gap identification',
                'Infrastructure gap analysis: cold storage, processing, logistics',
                'Producer and buyer density mapping',
            ]
        },
        {
            'title': 'Program Administration',
            'items': [
                'Grant allocation optimization: where will dollars have most impact?',
                'Farm-to-institution program tracking and reporting',
                'Compliance and reporting automation',
                'Outcome measurement and benchmarking',
            ]
        },
        {
            'title': 'Food Security & Resilience',
            'items': [
                'Supply chain vulnerability assessments',
                'Disruption early warning systems',
                'Strategic reserve planning',
                'Emergency response coordination data',
            ]
        },
    ],
    'questions': [
        "Which counties have processor capacity gaps that limit local food growth?",
        "How much of our state's produce could be met by local growers?",
        "Which SNAP incentive programs are driving the most local purchasing?",
        "Where should we prioritize cold storage infrastructure investment?",
        "What's our regional food system's vulnerability to a major weather event?",
    ],
    'problems': [
        {
            'title': 'Data fragmentation',
            'description': "You're making policy with incomplete data. USDA, state agencies, and local reports don't connect.",
        },
        {
            'title': 'Impact opacity',
            'description': "Programs are funded but you can't measure what's working. Dollars flow without accountability.",
        },
        {
            'title': 'Reactive posture',
            'description': 'You respond to crises instead of preventing them. No early warning system for food security risks.',
        },
    ],
}

INVESTORS_DATA = {
    'name': 'Investors',
    'badge': 'Intelligence for Due Diligence',
    'headline': 'Trust, but verify',
    'description': 'Independent verification of supplier relationships, customer concentration, and market position. De-risk your ag and food deals with real transaction data.',
    'decisions': [
        "Are this company's supplier relationships real and defensible?",
        'Does the customer list match actual transaction data?',
        "What's the real market size - not the pitch deck TAM?",
        "How concentrated is revenue, and what's the churn risk?",
        "What operational or regulatory risks aren't in the data room?",
    ],
    'capabilities': [
        {
            'title': 'Supply Chain Verification',
            'items': [
                'Validate claimed supplier relationships against real transaction data',
                'Assess supplier concentration and switching risk',
                'Verify volume claims and pricing terms',
                'Identify undisclosed supply chain dependencies',
            ]
        },
        {
            'title': 'Customer Due Diligence',
            'items': [
                'Cross-reference customer lists with actual market activity',
                'Analyze revenue concentration and retention patterns',
                'Identify customer overlap with competitors',
                'Validate growth claims with independent demand signals',
            ]
        },
        {
            'title': 'Market Validation',
            'items': [
                'Size markets using transaction-level data, not top-down estimates',
                'Benchmark target against regional competitors',
                'Assess pricing power and margin sustainability',
                'Identify regulatory and policy risks specific to the segment',
            ]
        },
        {
            'title': 'Operational Benchmarking',
            'items': [
                'Compare capacity utilization to industry peers',
                'Evaluate operational efficiency metrics',
                'Identify post-acquisition value creation opportunities',
                'Assess integration complexity for M&A',
            ]
        },
    ],
    'questions': [
        "Does this processor's claimed throughput match what we see in supplier data?",
        "Are the top 5 customers actually buying at the volumes management claims?",
        "What's the real market share for this distributor in their core region?",
        "How does this target's supplier pricing compare to competitors?",
        "What customer concentration risk isn't showing up in the financials?",
    ],
    'problems': [
        {
            'title': 'Unverifiable claims',
            'description': 'Management says they have 200 suppliers and 50 key customers. You have no way to check. Until now.',
        },
        {
            'title': 'Pitch deck TAMs',
            'description': 'Every deck shows a $10B market. Real market size? Real share? Real growth? Nobody knows.',
        },
        {
            'title': 'Hidden concentration risk',
            'description': 'Revenue looks diversified until you realize three customers are owned by the same parent company.',
        },
    ],
}

AG_SUPPLY_DATA = {
    'name': 'Ag Supply',
    'badge': 'Intelligence for Input Suppliers',
    'headline': 'Get ahead of demand',
    'description': 'Grower-level forecasting, competitive positioning, and inventory optimization. Stop reacting to the season.',
    'decisions': [
        'Where is demand for inputs heading, and how should I position inventory?',
        'Which growers are scaling and need more supply?',
        'How do I get ahead of seasonal demand spikes?',
        'Where are my competitors winning, and why?',
        'Which new products or categories should I add?',
    ],
    'capabilities': [
        {
            'title': 'Demand Forecasting',
            'items': [
                'Grower-level demand signals by input category',
                'Seasonal demand modeling based on planting intentions',
                'Regional trend analysis: which areas are expanding production?',
                'New customer identification: who is scaling and underserved?',
            ]
        },
        {
            'title': 'Market Intelligence',
            'items': [
                'Competitive pricing and positioning analysis',
                'Share of wallet analysis: where are growers buying elsewhere?',
                'Product gap identification: what are growers asking for?',
                'Emerging practice trends (organic, regenerative) and input implications',
            ]
        },
        {
            'title': 'Sales Optimization',
            'items': [
                'Customer segmentation and targeting',
                'Pricing optimization by segment and season',
                'Credit risk assessment using farm financial signals',
                'Cross-sell and upsell recommendations',
            ]
        },
        {
            'title': 'Inventory & Logistics',
            'items': [
                'Demand-driven inventory positioning',
                'Regional distribution optimization',
                'Pre-season order forecasting',
                'Stockout risk alerts',
            ]
        },
    ],
    'questions': [
        "Which growers in my territory are expanding acreage and need more seed?",
        "Am I priced competitively on fertilizer compared to the co-op?",
        "What's the demand outlook for organic inputs in the Great Lakes region?",
        "Which of my customers are at risk of switching to a competitor?",
        "When should I pre-position inventory for spring planting season?",
    ],
    'problems': [
        {
            'title': 'Demand lag',
            'description': "You see demand when orders come in, not when growers are planning. Always a season behind.",
        },
        {
            'title': 'Customer churn',
            'description': "Growers switch suppliers and you don't know why. No visibility into competitive positioning.",
        },
        {
            'title': 'Inventory mismatch',
            'description': 'Wrong products in the wrong places. Stockouts during peak season, overstock after.',
        },
    ],
}

# Capability Data
PRICING_INTELLIGENCE_DATA = {
    'name': 'Pricing Intelligence',
    'badge': 'Market Data',
    'headline': 'Know what the market is actually paying',
    'description': "We aggregate pricing data from across the food system - transactions, contracts, spot markets, and private sales - so you can see what things actually cost, not what someone tells you they cost.",
    'why_us': [
        'Proprietary data from thousands of transactions across growers, processors, distributors, and buyers',
        'Real prices, not list prices - we capture what actually changes hands',
        'Regional granularity down to the county level',
        'Historical trends so you can spot patterns and time decisions',
    ],
    'who_its_for': ['Growers', 'Food Processors', 'CPG Producers', 'Restaurants', 'Investors'],
    'questions': [
        "What are tomatoes actually going for in the Hudson Valley right now?",
        "Am I paying more for organic eggs than other buyers in my region?",
        "How have apple prices trended over the last three seasons?",
        "When do prices typically dip for local beef?",
        "What's the price spread between conventional and organic for leafy greens?",
    ],
}

DEMAND_FORECASTING_DATA = {
    'name': 'Demand Forecasting',
    'badge': 'Predictive Analytics',
    'headline': 'See where demand is headed before it gets there',
    'description': "We combine historical patterns, real-time signals, and proprietary data to forecast demand across crops, products, and regions. Plan production, inventory, and sales around what's coming - not what already happened.",
    'why_us': [
        'Models trained on actual transaction data, not surveys or estimates',
        'Incorporates weather, seasonality, buyer behavior, and market trends',
        'Forecasts at the granularity you need - by crop, region, channel, or customer segment',
        'Continuously updated as new data flows in',
    ],
    'who_its_for': ['Growers', 'Food Processors', 'CPG Producers', 'Ag Supply'],
    'questions': [
        "What's the 90-day demand outlook for local tomatoes in the Mid-Atlantic?",
        "Which crops are seeing rising demand from restaurant buyers?",
        "Should I expect a demand spike for pumpkins earlier this year?",
        "How is demand for organic produce trending vs. conventional?",
        "Which product categories are growing fastest with CPG buyers?",
    ],
}

BUYER_SUPPLIER_NETWORK_DATA = {
    'name': 'Buyer/Supplier Network',
    'badge': 'Network Intelligence',
    'headline': "Find the buyers and suppliers you don't know exist",
    'description': "We've mapped the food system - who's buying, who's selling, what they need, and what they offer. Whether you're looking for new customers or new sources of supply, we can show you who's out there and help you connect.",
    'why_us': [
        'Database of growers, processors, distributors, restaurants, and CPG brands across the country',
        'Filterable by crop, volume, region, certifications, and more',
        'Relationship data - who is already buying from whom',
        'Insights on reliability, scale, and fit before you make the first call',
    ],
    'who_its_for': ['Growers', 'Food Processors', 'CPG Producers', 'Restaurants'],
    'questions': [
        "Which restaurants within 100 miles are actively sourcing local produce?",
        "Who can supply 20,000 lbs of organic blueberries in the Northeast?",
        "What processors in my region work with small-scale growers?",
        "Which distributors specialize in local and regional products?",
        "Are there buyers looking for the specific crops I grow?",
    ],
}

CROP_PLANNING_DATA = {
    'name': 'Crop Planning',
    'badge': 'Decision Support',
    'headline': 'Plant what the market actually wants',
    'description': "We help growers decide what to plant based on real demand signals, pricing trends, regional dynamics, and their own operation's strengths. Stop guessing based on last year's prices - plan with data.",
    'why_us': [
        'Demand forecasts by crop and region so you know what buyers will need',
        'Pricing intelligence to identify high-margin opportunities',
        'Competitive landscape - what other growers in your area are planting',
        'Tailored to your soil, climate, equipment, and buyer relationships',
    ],
    'who_its_for': ['Growers'],
    'questions': [
        "What's the highest-margin crop mix for my 50 acres next season?",
        "Is there unmet demand for specialty peppers in my region?",
        "Should I diversify into herbs given current market trends?",
        "What are other growers in my county planning to plant?",
        "Which crops have the best demand outlook for the next 2-3 years?",
    ],
}

SEASONAL_PLANNING_DATA = {
    'name': 'Seasonal Planning',
    'badge': 'Decision Support',
    'headline': 'Align your business to the rhythms of the food system',
    'description': "We help processors, buyers, and food businesses plan around seasonal availability, pricing cycles, and demand patterns. Know what's coming, when it's coming, and how to position for it.",
    'why_us': [
        'Seasonal availability calendars by crop, region, and quality tier',
        'Price cycle analysis - when to buy, when to sell, when to hold',
        'Demand pattern mapping across channels and customer segments',
        'Early warning on seasonal shifts driven by weather or market changes',
    ],
    'who_its_for': ['Food Processors', 'CPG Producers', 'Restaurants'],
    'questions': [
        "When should I lock in contracts for next season's tomato supply?",
        "What's the optimal time to launch a seasonal menu around local produce?",
        "How early do I need to secure stone fruit for summer production?",
        "Which ingredients are coming into season that I should plan around?",
        "When do prices typically bottom out for winter squash?",
    ],
}

CUSTOM_SOFTWARE_DATA = {
    'name': 'Custom Software & Dashboards',
    'badge': 'Technology',
    'headline': 'Software that fits how you actually work',
    'description': "We build custom tools - dashboards, workflows, integrations, and applications - tailored to your operation. No bloated ERPs, no forcing your business into someone else's box. Just software that solves your specific problems.",
    'why_us': [
        'Deep food system expertise - we understand your business before we write code',
        'AI-native development - we build with modern tools that let us move fast',
        'Integration with your existing systems and data sources',
        'Ongoing iteration - we build, you use it, we improve it',
    ],
    'who_its_for': ['Growers', 'Food Processors', 'CPG Producers', 'Restaurants', 'Ag Supply'],
    'questions': [
        "Can you build a dashboard that shows my supply chain in real time?",
        "I need a tool to manage orders across 30 different farms - can you help?",
        "How do I get my production data connected to demand signals?",
        "Can you replace my spreadsheet chaos with something that actually works?",
        "I want my team to have visibility into pricing and inventory in one place.",
    ],
}

PROFITABILITY_ANALYSIS_DATA = {
    'name': 'Profitability Analysis',
    'badge': 'Advisory',
    'headline': "Find where you're making money and where you're not",
    'description': "We dig into your data - costs, pricing, operations, customers - and show you where margin is hiding and where it's leaking. Concrete analysis, not generic advice.",
    'why_us': [
        'We combine your internal data with market benchmarks for context',
        'Food system expertise - we know where to look for margin in this industry',
        'Actionable findings, not just charts - we tell you what to do about it',
        'Confidential and independent - your data stays yours',
    ],
    'who_its_for': ['Growers', 'Food Processors', 'CPG Producers', 'Restaurants'],
    'questions': [
        "Which of my products are actually making money after all costs?",
        "Am I paying too much for inputs compared to similar operations?",
        "Where am I losing margin in my supply chain?",
        "Which customer relationships are profitable and which are not?",
        "What would it take to improve my margins by 5%?",
    ],
}

AI_INTEGRATION_DATA = {
    'name': 'AI Integration',
    'badge': 'Technology',
    'headline': 'Put AI to work in your operation',
    'description': "We help food businesses implement AI in practical ways - automating workflows, improving forecasts, extracting insights from messy data, and building intelligent tools. Not hype, just useful applications that make your team more effective.",
    'why_us': [
        'We know AI and we know food systems - rare combination',
        'Focus on practical applications with clear ROI, not science projects',
        'Integration with your existing tools and workflows',
        'Training and support so your team can actually use what we build',
    ],
    'who_its_for': ['Growers', 'Food Processors', 'CPG Producers', 'Restaurants', 'Ag Supply'],
    'questions': [
        "How can AI help me forecast demand more accurately?",
        "Can I use AI to automate my invoice processing and data entry?",
        "Is there a way to use AI to monitor my supply chain for risks?",
        "How do I get insights out of all the unstructured data I have?",
        "What AI tools would actually be useful for a business like mine?",
    ],
}

# Customer View functions
def growers(request):
    return customer_detail(request, GROWERS_DATA)

def food_processors(request):
    return customer_detail(request, FOOD_PROCESSORS_DATA)

def cpg_producers(request):
    return customer_detail(request, CPG_PRODUCERS_DATA)

def restaurants(request):
    return customer_detail(request, RESTAURANTS_DATA)

def government(request):
    return customer_detail(request, GOVERNMENT_DATA)

def investors(request):
    return customer_detail(request, INVESTORS_DATA)

def ag_supply(request):
    return customer_detail(request, AG_SUPPLY_DATA)

# Capability View functions
def pricing_intelligence(request):
    return capability_detail(request, PRICING_INTELLIGENCE_DATA)

def demand_forecasting(request):
    return capability_detail(request, DEMAND_FORECASTING_DATA)

def buyer_supplier_network(request):
    return capability_detail(request, BUYER_SUPPLIER_NETWORK_DATA)

def crop_planning(request):
    return capability_detail(request, CROP_PLANNING_DATA)

def seasonal_planning(request):
    return capability_detail(request, SEASONAL_PLANNING_DATA)

def custom_software(request):
    return capability_detail(request, CUSTOM_SOFTWARE_DATA)

def profitability_analysis(request):
    return capability_detail(request, PROFITABILITY_ANALYSIS_DATA)

def ai_integration(request):
    return capability_detail(request, AI_INTEGRATION_DATA)