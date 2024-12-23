from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from viewer.models import Offer, Comment
from viewer.views.forms.add_offer_form import OfferForm

# Zobrazení seznamu inzerátů
class OfferListView(ListView):
    model = Offer
    template_name = 'offers/offer_list.html'
    context_object_name = 'offers'
    ordering = ['-offer_date']

# Detail inzerátu
class OfferDetailView(DetailView):
    model = Offer
    template_name = 'offers/offer_detail.html'
    context_object_name = 'offer'

    def get_context_data(self, **kwargs):
        # Získání komentářů a jejich počtu pro detail inzerátu
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(offer=self.object).order_by('-commented_date')
        context['comments_count'] = context['comments'].count()

        # Zvýšení počtu zobrazení (view_count)
        self.object.view_count += 1
        self.object.save()

        return context

# Vytvoření nového inzerátu
class OfferCreateView(CreateView):
    model = Offer
    form_class = OfferForm
    template_name = 'navbar_menu/add_offer.html'
    success_url = reverse_lazy('offer_list')  # Přesměrování po úspěšném uložení

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Přidat inzerát"
        return context

# Úprava existujícího inzerátu
class OfferUpdateView(UpdateView):
    model = Offer
    form_class = OfferForm
    template_name = 'offers/offer_form.html'
    success_url = reverse_lazy('search')  # Přesměrování po úspěšné aktualizaci

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Upravit inzerát"
        return context

# Smazání inzerátu
class OfferDeleteView(DeleteView):
    model = Offer
    template_name = 'offers/offer_confirm_delete.html'
    success_url = reverse_lazy('offer_list')  # Přesměrování po úspěšném smazání
