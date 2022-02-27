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