from django.views.generic import TemplateView


class EconomicalCarsView(TemplateView):
    template_name = 'top_six/economical_cars.html'
