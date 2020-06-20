from django.shortcuts import render

from .models import Listing #bringin in the Listing model



def index(request):
    listings = Listing.objects.all() #brings in all of the Listings in this one variable.

    context = {
        'listings' : listings
    }
    
    return render(request, 'listings/listings.html', context) #this line actually returns the listings, as the 'context' variable holds the listings.

    
def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')


