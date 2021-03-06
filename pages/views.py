from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices,price_choices,state_choices




def home(requests):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
        
    }
    return render(requests, 'pages/home.html', context)

def about(requests):
    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)

    context = {
        'mvp_realtors' : mvp_realtors,
        'realtors' : realtors
    }
    return render(requests, 'pages/about.html', context)
