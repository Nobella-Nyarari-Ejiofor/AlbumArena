from django.test import TestCase
from .models import Category, Image , Location
# Create your tests here.


class CategoryTestClass(TestCase):
  """
  
  """
  def setUp(self):
    self.food = Category(category_name = 'Food')

  # testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.food , Category))

  #test for the save functionality
  def test_save_method(self):
    self.food.save_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories)>0)

  # test for deleting functionality
  def test_delete_method(self):
    d = self.food.id
    self.food.delete_category()
    categories = Category.objects.get(id__exact=d)
    self.assertEqual(categories,(None))

class LocationTestClass(TestCase):
  def setUp(self):
    self.Nairobi = Location(location_name = "Nairobi")

  # testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.Nairobi , Location))
  
  #testing the save method

  def test_save_method(self):
    self.Nairobi.save_locations()
    locations = Location.objects.all()
    self.assertTrue(len(locations)>0)