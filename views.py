from django.shortcuts import render
from django.http import JsonResponse

def book_table(request):
    # Implement logic to handle table booking
    return JsonResponse({'message': 'Table booked successfully'})

def cancel_booking(request, booking_id):
    # Implement logic to cancel booking
    return JsonResponse({'message': 'Booking canceled successfully'})
