from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('card/<int:card_id>/', views.card, name='card')
    ]
