from django.shortcuts import render
from viewer.models import Brand, Offer, Comment, VehicleType


def search(request):

    filtered_offers = Offer.objects.all()

    filter_of_description = request.POST.get("search_description", "")
    if filter_of_description != "":
        filtered_offers = filtered_offers.filter(nameoffer__icontains=filter_of_description)

    filter_of_brand = request.POST.get("search_brand", "")
    if filter_of_brand != "":
        filtered_offers = filtered_offers.filter(brand__pk=filter_of_brand)

    filter_of_price_from = request.POST.get("search_price_from", "")
    if filter_of_price_from != "":
        filtered_offers = filtered_offers.filter(price__gt=filter_of_price_from)

    filter_of_price_to = request.POST.get("search_price_to", "")
    if filter_of_price_to != "":
        filtered_offers = filtered_offers.filter(price__lt=filter_of_price_to)

    filter_of_type= request.POST.get("search_type", "")
    if filter_of_type != "":
        filtered_offers = filtered_offers.filter(vehicle_type__pk=filter_of_type)

    filter_of_year_from = request.POST.get("search_year_from", "")
    if filter_of_year_from != "":
        filtered_offers = filtered_offers.filter(year__gt=filter_of_year_from)

    filter_of_year_to = request.POST.get("search_year_to", "")
    if filter_of_year_to != "":
        filtered_offers = filtered_offers.filter(year__lt=filter_of_year_to)


    return render(
        request, template_name='navbar_menu/search.html',
        context={
            "title": "Hledat",
            "offers": filtered_offers,
            "all_brands": Brand.objects.all(),
            "all_types": VehicleType.objects.all()
            }
    )
