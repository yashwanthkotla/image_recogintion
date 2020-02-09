from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, Hotel
from .forms import *

posts = [
    {
        'author':'Kotla',
        'title'  : 'Post1',
        'content'  : 'My first post',
        'date_posted' : '29th feb 2020'
    },
    {
        'author':'Kotla2',
        'title'  : 'Post2',
        'content'  : 'My second post',
        'date_posted' : '29th feb 2020'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'image_collector/home.html', context)

def about(request):
    return render(request,'image_collector/about.html')   
    
def test(request):
    return HttpResponse('<h1>About test</h1>')

def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
    return render(request, 'image_collector/hotel_image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 

def view_images(request):
    context = {
        'hotels' : Hotel.objects.all()
    }
    return render(request, 'image_collector/view_images.html', context)