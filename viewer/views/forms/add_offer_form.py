from django import forms
from viewer.models import Offer

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ["nameoffer", "brand", "vehicle_type", "price", "year", "power", "descriptionoffer", "fuel_type", "km"]
        labels = {
            'nameoffer': 'Název inzerátu',
            'brand': 'Vyber zančku',
            'fuel_type': 'Vyber typ paliva',
            'vehicle_type': 'Typ karoserie',
            "price": "Cena",
            "year": "Rok výroby",
            "power": "Výkon (kW)",
            "descriptionoffer": "Popis auta",
            "km": "Najeto"

        }
        # widgets = {
        #             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Název nabídky'}),
        #             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Popis nabídky'}),
        #             'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cena'}),
        #         }
