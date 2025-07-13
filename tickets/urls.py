from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/new/', views.ticket_create, name='ticket_create'),
    path('tickets/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/<int:pk>/update_status/', views.ticket_update_status, name='ticket_update_status'),
]