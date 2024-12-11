from django.test import TestCase
from viewer.models import Comment, Offer, Brand, VehicleType
from datetime import datetime

class CommentStrMethodTest(TestCase):

    def setUp(self):
        self.brand = Brand.objects.create(name='Volvo')
        self.vehicle_type = VehicleType.objects.create(name='SUV')

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

        self.comment = Comment.objects.create(
            username = "Belys",
            offer = self.offer,
            text = 'This is a test comment',
            commented_date = datetime(2024, 12, 3, 10, 0 )
        )


    def test_comment_str(self):
        expected_str = f"User: {self.comment.username},comment: {self.comment.text}"
        self.assertEqual(str(self.comment), expected_str)
