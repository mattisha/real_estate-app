from django.shortcuts import render

def index(requests):
    return render(requests, 'listings/listings.html')

def listing(requests):
    return render(requests, 'listings/listing.html')

def search(requests):
    return render(requests, 'listings/search.html')