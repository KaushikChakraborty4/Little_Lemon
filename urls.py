from django.urls import path
from . import views

urlpatterns = [
    path('book-table/', views.book_table, name='book-table'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel-booking'),
]