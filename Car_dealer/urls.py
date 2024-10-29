"""Car_dealer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from viewer.views import search, add_offer, offer, add_comment, LandingTemplateView
from viewer.models import Brand, Comment, Offer, VehicleType
from django.shortcuts import render

admin.site.register(Brand)
admin.site.register(Comment)
admin.site.register(Offer)
admin.site.register(VehicleType)

from viewer.example_form import BrandView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', LandingView.as_view(), name="landing_page"),
    path('', LandingTemplateView.as_view(), name="landing_page"),
    path('search/', search),
    path('add_offer/', add_offer, name="add_offer"),
    path('add_comment/', add_comment),
    path('offer/<pk_offer>', offer, name='offer'),
    # path('cars_view', CarsView.as_view() ),
    path('brand_form/', BrandView.as_view() ),
    path('brand_create/', BrandView.as_view()),


]
