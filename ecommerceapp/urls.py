from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('checkout/', views.checkout, name="Checkout"),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    path('delete_booking/<int:order_id>/', views.delete_booking, name='delete_booking'),
    path('update_appointment_date/<int:order_id>/', views.update_appointment_date, name='update_appointment_date'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    
]