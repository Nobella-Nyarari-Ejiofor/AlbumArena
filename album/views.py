from django.http import Http404
from django.shortcuts import render
from .models import Category , Image , Location


# Create your views here.
def homepage(request):
  image = Image.objects.all()
  print(image)
  return render(request, 'homepage.html',{"images":image})

def search_location(request):
  if 'location' in request.GET and request.GET["location"]:

    location_list = Location.objects.all()

    try:
      location_term = request.GET.get("location")
      location_results = Image.filter_by_location(location_term)
      message = f"{location_term}"
      context = {
        "message": message,
        "images":location_results,
        "location_list": location_list
      }

      return render(request , 'location.html' , context)

    except ValueError:
      Http404()

  else:
    message="You haven't searched for any term"
    return render(request,'location.html',{"message":message})

    
    
def search_results(request):
  if 'category' in  request.GET and request.GET["category"]:

    category_list = Category.objects.all()

    try:
      search_term = request.GET.get("category")
      search_results = Image.filter_by_category(search_term)
      message = f"{search_term}"
      context = {
        "message":message,
        "images":search_results,
        "category_list":category_list,
      }
      print(search_results) 
      return render(request,'search.html',context)
    
    except ValueError:
      raise Http404()
  
  else:
    message="You haven't searched for any term"
    return render(request,'search.html',{"message":message})
      


def view_location(request,location):


    try:
      location_list = Location.objects.all()
      input_results = Image.filter_by_location(location)
      message = f"results for{input_results}"
      context = {
        "message":message,
        "images":input_results,
        "location_list": location_list,
      }
      return render(request,'location.html', context)

    except ValueError:
      Http404()

    return render(request, 'location.html',context)


# def location_list(request):
#   location_list = Location.objects.all()

#   return (request , 'navbar.html' ,{"location_list":location_list})
