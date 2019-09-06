from django.shortcuts import render, get_object_or_404
from .models import Card

# index view

def index(request):
    cards = Card.objects.all()
    context = {
        'data': zip(
            [card.name for card in cards],
            [card.id for card in cards]
            )}
    return render(request, 'ratings/index.html', context)
    
def card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    context = {
        'id': card.id,
        'name': card.name,
        'content': card.content,
        'rating': card.rating,
    }
    return render(request, 'ratings/card.html', context)
