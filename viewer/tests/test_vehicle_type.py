from django.test import TestCase
from viewer.models import VehicleType


class VehicleTypeStrMethodTest(TestCase):
    def setUp(self):
        self.vehicletype =VehicleType.objects.create(name='Kombi')
    def test_brand_str(self):
        self.assertEqual(str(self.vehicletype), 'Typ: Kombi')
