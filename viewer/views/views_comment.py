from viewer.models import Offer, Comment
from viewer.views.views_offer import offer


def add_comment(request):
    pk_offer = request.POST.get("pk_offer")
    new_comment = Comment()
    new_comment.offer = Offer.objects.get(pk=pk_offer)
    new_comment.username = request.POST.get("username", "Nikdo")
    new_comment.text = request.POST.get("text", "Bez textu")
    new_comment.save()
    return offer(request, pk_offer)