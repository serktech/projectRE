from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Listing


def index(request):
    listings = Listing.objects.order_by('list_date')

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,

    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
        'listing_id': listing_id
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
