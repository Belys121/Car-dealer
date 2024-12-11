from django.test import TestCase
from viewer.models import Brand


class BrandStrMethodTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Volvo')
    def test_brand_str(self):
        self.assertEqual(str(self.brand), 'Značka auta: Volvo')