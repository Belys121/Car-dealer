from django.shortcuts import render, redirect
from viewer.models import Brand, Offer, Comment, VehicleType
from viewer.views.forms import OfferForm


def offer(request, pk_offer):
    offer = Offer.objects.get(pk=pk_offer)
    offer.view_count += 1
    offer.save()
    return render(
        request, template_name='offers/offer.html',
        context={
            "title": "Autobazar Belda",
            "offer": offer,
            "comments": Comment.objects.filter(offer__pk=pk_offer).order_by("-commented_date").all(),
            "comments_count": Comment.objects.filter(offer__pk=pk_offer).order_by("-commented_date").all().count()
            }
    )


def add_offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_offer')  # Přesměrování po úspěšném uložení
    else:
        form = OfferForm()

    return render(
        request,
        'navbar_menu/add_offer.html',
        {
            "title": "Přidat inzerát",
            "form": form,
        }
    )