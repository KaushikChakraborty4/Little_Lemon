from django.test import TestCase
from django.urls import reverse

class BookingTestCase(TestCase):
    def test_book_table(self):
        response = self.client.post(reverse('book-table'), {'table_number': 1, 'date': '2024-04-01', 'time': '18:00'})
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_cancel_booking(self):
        response = self.client.delete(reverse('cancel-booking', args=[1]))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed
