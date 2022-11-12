from django.urls import path
from . import views

urlpatterns = [
    path('payment_mag/', views.payment, name='payment_mag'),
    path('payment_edit/', views.payment_edit, name='payment_edit'),
    path('payment_del/', views.payment_delete, name='payment_delete'),
    path('appointment_mag/', views.appointment_mag, name='appointment_mag'),
]
