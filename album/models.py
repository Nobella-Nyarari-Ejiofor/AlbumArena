from django.db import models

# Create your models here.
# The image model 
class Location('models.Model'):
  location = models.CharField(max_length = 20)
  
  def __str__(self):
    return self.location


class Category(models.Model):
  category = models.CharField(max_length = 10)
  
  def __str__(self):
    return self.category



class Image(models.Model):
  image = models.ImageField(upload_to ='album/')
  image_name = models.CharField(max_length= 30)
  image_description=models.CharField(max_length = 300)
  category = models.ForeignKey(Category)
  location = models.ForeignKey(Location)

  def __str__(self):
    return self.image_name

  class Meta:
    ordering = ['location']


