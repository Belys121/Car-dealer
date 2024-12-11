from django.views.generic import TemplateView

from viewer.models import Offer, Comment

class LandingTemplateView(TemplateView):
    template_name = 'base_homepage_landingpage/landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newest_offers"] = Offer.objects.order_by("-offer_date").all()[:5]
        context["popular_offers"] = Offer.objects.order_by("-view_count").all()[:5]
        context["newest_comments"] = Comment.objects.order_by("-commented_date").all()[:5]
        return context