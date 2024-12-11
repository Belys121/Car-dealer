from django.test import TestCase
from viewer.models import Offer, Brand, VehicleType
from datetime import datetime


class OfferStrMethodTest(TestCase):
    def setUp(self):
        # Vytvoření instancí závislých modelů
        self.brand = Brand.objects.create(name='Volvo')
        self.vehicle_type = VehicleType.objects.create(name='SUV')

        # Vytvoření instance modelu Offer
        self.offer = Offer.objects.create(
            brand=self.brand,
            vehicle_type=self.vehicle_type,
            price=500000,
            nameoffer='Volvo XC60',
            power=200,
            year=2022,
            offer_date=datetime(2024, 12, 1, 10, 0),
            view_count=15,
            descriptionoffer='A premium SUV.'
        )

    def test_offer_str(self):
        expected_str = f"Nabídka: {self.brand}, {self.offer.view_count}, {self.offer.offer_date}"
        self.assertEqual(str(self.offer), expected_str)
