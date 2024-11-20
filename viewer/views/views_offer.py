from django.shortcuts import render
from viewer.models import Brand, Offer, Comment, VehicleType


def offer(request, pk_offer):
    offer = Offer.objects.get(pk=pk_offer)
    offer.view_count += 1
    offer.save()
    return render(
        request, template_name='offer.html',
        context={
            "title": "Autobazar Belda",
            "offer": offer,
            "comments": Comment.objects.filter(offer__pk=pk_offer).order_by("-commented_date").all(),
            "comments_count": Comment.objects.filter(offer__pk=pk_offer).order_by("-commented_date").all().count()
            }
    )


def add_offer(request):
    status = ""
    if "description" in request.POST:
        brand = request.POST.get("brand", "")
        vehicle_type = request.POST.get("type", "")

        new_offer = Offer()
        new_offer.description = request.POST.get("description", "")
        new_offer.price = int(request.POST.get("price", 0))
        new_offer.year = int(request.POST.get("year", 0))
        new_offer.power = int(request.POST.get("power", 0))
        new_offer.brand = Brand.objects.get(pk=brand)
        new_offer.vehicle_type = VehicleType.objects.get(pk=vehicle_type)
        new_offer.save()
        status = "Přidáno"
        pass

    return render(
        request, template_name='add_offer.html',
        context={
            "title": "Přidat inzerát",
            "all_brands": Brand.objects.all(),
            "all_types": VehicleType.objects.all(),
            "status": status
        }
    )