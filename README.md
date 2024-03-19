Define models for managing tables and bookings in the bookings/models.py file
Create views for handling table bookings in the bookings/views.py file.
Configure URLs to map requests to views in the bookings/urls.py file.
unit tests for testing the booking functionality in the bookings/tests.py file.

Install Django using pip if you haven't already. -- pip install django
Create a Django Project: Create a Django project using the following command. --   django-admin startproject little_lemon_project
Create a Django App: Create a Django app for managing table bookings. 
  cd little_lemon_project
  python manage.py startapp bookings
Configure settings.py to connect to your MySQL database.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
