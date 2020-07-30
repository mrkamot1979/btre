from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Listing #bringin in the Listing model



def index(request):
    listings = Listing.objects.order_by('-lst_date').filter(is_published=True) #brings in all of the Listings in this one variable.

    #code for pagination, where we set the per page at 3.
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings #we are passing the paged listing
    }
    
    return render(request, 'listings/listings.html', context) #this line actually returns the listings, as the 'context' variable holds the listings.

    
def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')


