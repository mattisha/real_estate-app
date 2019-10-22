from django.shortcuts import render
from .models import Listing



def index(requests):
    listings = Listing.objects.all()

    context = {
        'listings' : listings
    }
    return render(requests, 'listings/listings.html',context)

def listing(requests,listing_id):
    return render(requests, 'listings/listing.html')

def search(requests):
    return render(requests, 'listings/search.html')