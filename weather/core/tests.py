from django.test import TestCase
from .models import City
# Create your tests here.
city =City.objects.all()
print(city)