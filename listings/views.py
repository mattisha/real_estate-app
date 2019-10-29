from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





def index(requests):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)

    paginator = Paginator(listings,3)
    page = requests.GET.get('page')
    page_listing = paginator.get_page(page)

    context = {
        'listings' : page_listing
    }
    return render(requests, 'listings/listings.html',context)

def listing(requests,listing_id):
    return render(requests, 'listings/listing.html')

def search(requests):
    return render(requests, 'listings/search.html')
