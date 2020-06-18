from django.shortcuts import render

from .models import Listing #bringin in the Listing model



def index(request):
    return render(request, 'listings/listings.html')

    listings = Listing.objects.all() 

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')


