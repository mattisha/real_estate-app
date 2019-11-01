from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import bedroom_choices, price_choices, state_choices





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
    listings = get_object_or_404(Listing, pk=listing_id)
    
    context = {
        'listings' : listings,
    }
    return render(requests, 'listings/listing.html', context)







def search(requests):
    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in requests.GET:
        keywords = requests.GET['keywords']
        if keywords:
          queryset_list = queryset_list.filter(description__icontains=keywords)
 
    if 'city' in requests.GET:
        city = requests.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in requests.GET:
        state = requests.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__exact=state)

    if 'bedrooms' in requests.GET:
        bedrooms = requests.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__exact=bedrooms)

    if 'price' in requests.GET:
        price = requests.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings' : queryset_list ,
        'values': requests.GET,
    }
    return render(requests, 'listings/search.html', context)
