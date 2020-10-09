"""URL configuration for checkoutcalculator"""
from django.urls import path

from . import views

urlpatterns = [
    path('product-database', views.ListItem.as_view()),
    path('product-database/<int:pk>/', views.DetailItem.as_view()),
]
