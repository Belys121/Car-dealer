from datetime import datetime

from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField
)


class Brand(Model):
    name = CharField(max_length=64)


    def __str__(self):
        return f"Značka auta: {self.name}"


class VehicleType(Model):
    name = CharField(max_length=64)


    def __str__(self):
        return f"Typ: {self.name}"


class FuelType(Model):
    name = CharField(max_length=64)


    def __str__(self):
        return f"Palivo: {self.name}"

class Offer(Model):
    fuel_type = ForeignKey(FuelType, on_delete=DO_NOTHING, null=True, default=None)
    brand = ForeignKey(Brand, on_delete=DO_NOTHING)
    vehicle_type = ForeignKey(VehicleType, on_delete=DO_NOTHING)
    price = IntegerField()
    nameoffer = TextField()
    power = IntegerField()
    year = IntegerField()
    offer_date = DateTimeField(default=datetime.now)
    view_count = IntegerField(default=0)
    descriptionoffer = TextField()
    km = IntegerField(default=0)


    def __str__(self):
        return f"Nabídka: {self.brand}, {self.view_count}, {self.offer_date}"


class Comment(Model):
    username = CharField(max_length=64)
    offer = ForeignKey(Offer, on_delete=DO_NOTHING)
    text = TextField()
    commented_date = DateTimeField(default=datetime.now)


    def __str__(self):
        return f"User: {self.username},comment: {self.text}"
