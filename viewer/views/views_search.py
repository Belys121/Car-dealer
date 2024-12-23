from django.shortcuts import render
from django.db.models import Q
from viewer.models import Brand, Offer, VehicleType, FuelType


def search(request):
    # Vytvoření prázdného Q objektu (žádné filtry na začátku)
    query = Q()

    # Zpracování filtrů z POST dat
    if description := request.POST.get("search_description", ""):
        query &= Q(nameoffer__icontains=description)

    if brand := request.POST.get("search_brand", ""):
        query &= Q(brand__pk=brand)

    if price_from := request.POST.get("search_price_from", ""):
        query &= Q(price__gte=int(price_from))

    if price_to := request.POST.get("search_price_to", ""):
        query &= Q(price__lte=int(price_to))

    if vehicle_type := request.POST.get("search_type", ""):
        query &= Q(vehicle_type__pk=vehicle_type)

    if year_from := request.POST.get("search_year_from", ""):
        query &= Q(year__gt=year_from)

    if year_to := request.POST.get("search_year_to", ""):
        query &= Q(year__lt=year_to)

    if fuel_type := request.POST.get("search_fuel_type", ""):
        query &= Q(fuel_type__pk=fuel_type)

    # Aplikace filtrů na záznamy
    filtered_offers = Offer.objects.filter(query)

    return render(
        request,
        template_name='navbar_menu/search.html',
        context={
            "offers": filtered_offers,
            "all_brands": Brand.objects.all(),
            "all_types": VehicleType.objects.all(),
            "all_fuel": FuelType.objects.all(),
        }
    )
