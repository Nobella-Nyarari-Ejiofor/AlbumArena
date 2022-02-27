from django.db import models

# Create your models here.
# The image model 
class Location(models.Model):
  id = models.CharField(max_length = 100 , primary_key = True)
  location_name = models.CharField(max_length = 20)
  
  def __str__(self):
    return self.location_name

  def save_locations(self):
    self.save()


class Category(models.Model):
  id = models.CharField(max_length = 100 , primary_key = True)
  category_name = models.CharField(max_length = 10)
  
  def __str__(self):
    return self.category_name

  # saving a category
  def save_category(self):
    self.save()

  #deleting a category
  def delete_category(self):
    self.delete()




class Image(models.Model):
  image = models.ImageField(upload_to ='album/')
  image_name = models.CharField(max_length= 30)
  image_description=models.CharField(max_length = 300)
  category = models.ForeignKey(Category, on_delete= models.CASCADE)
  location = models.ForeignKey(Location, on_delete= models.CASCADE)

  def __str__(self):
    return self.image_name

  class Meta:
    ordering = ['location']


