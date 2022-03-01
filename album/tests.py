from email.mime import image
from django.test import TestCase
from .models import Category, Image , Location
# Create your tests here.


class CategoryTestClass(TestCase):

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
    self.food.delete_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories)== 0)

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

  def test_delete_method(self):
    self.Nairobi.delete_locations()
    locations = Location.objects.all()
    self.assertTrue(len(locations)==0)

class ImageTestClass(TestCase):

  # creating a new category and saving it
  
  def setUp(self):
    self.food = Category(category_name = "Food")
    self.food.save()

  # creating a new location and saving it 
    self.Nairobi = Location(location_name = "Nairobi")
    self.Nairobi.save()

    self.photo = Image(image ='images/onions1-removebg-preview.png', image_name ='some onions', image_description = 'A photo of an onion',category = self.food,location = self.Nairobi)
    

  def test_instance(self):
      self.assertTrue(isinstance(self.photo,Image))
  
  # test for deleting method
  def test_delete_image(self):
    self.photo.delete_image()
    image = Image.objects.all()
    self.assertTrue(len(image)==0)

  # test for saving an image 
  def test_save_image(self):
    self.photo.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images) > 0)


  # test for getting an image by id 
  def test_get_image(self):
    self.photo.save_image()
    image = Image.get_image(self.photo.id)
    self.assertEqual(image,self.photo)

  # filter by location

  def test_by_location(self):
    self.photo.save_image()
    location = Image.filter_by_location(self.photo.location)
    self.assertTrue(len(location) > 0)

  #filter by category
  def test_by_category(self):
    self.photo.save_image()
    categorys = Image.filter_by_category(self.photo.category)
    self.assertTrue(len(categorys) > 0)


  




  # Deletion of all instances from our model from database after every test
  def tearDown(self):
    Category.objects.all().delete()
    Location.objects.all().delete()
    Image.objects.all().delete()



  


   