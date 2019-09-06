from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('card/<int:card_id>/', views.card, name='card'),
    path('accounts/', include('django.contrib.auth.urls')),
    ]
