from django.db import models

# Create your models here.
# The image model 
class Location(models.Model):
  location_name = models.CharField(max_length = 20)
  
  def __str__(self):
    return self.location_name

  def save_locations(self):
    self.save()

  def delete_locations(self):
    Location.objects.filter(id = self.id).delete()


class Category(models.Model):
  category_name = models.CharField(max_length = 10)
  
  def __str__(self):
    return self.category_name

  # saving a category
  def save_category(self):
    self.save()

  #deleting a category
  def delete_category(self):
    Category.objects.filter(id = self.id).delete()
 

class Image(models.Model):
  image = models.ImageField(upload_to ='images/')
  image_name = models.CharField(max_length= 30)
  image_description = models.CharField(max_length = 300)
  category = models.ForeignKey(Category, on_delete= models.CASCADE)
  location = models.ForeignKey(Location, on_delete= models.CASCADE)

  def __str__(self):
    return self.image_name
   
  #  Saving image
  def save_image(self):
    self.save()

  # deleting an image 
  def delete_image(self):
    Image.objects.filter( id = self.id).delete()
  
   # getting image by id

  #filter image by location
  @classmethod
  def filter_by_location(cls,location):
    location_found = cls.objects.filter(location = Location.objects.filter(location_name__contains = location).first()).all()
    print(location)
    return location_found

  @classmethod
  def filter_by_category(cls,category):
    category_gotten = cls.objects.filter(category = Category.objects.filter(category_name__contains = category).first()).all()
    return category_gotten

  @classmethod
  def get_image(cls,id):
    image = cls.objects.get( id = id)
    return image

class Meta:
  ordering = ['location']





