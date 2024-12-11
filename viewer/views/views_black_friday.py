from django.views.generic import TemplateView

class BlackFridayView(TemplateView):
    template_name = 'top_six/black_friday.html'
