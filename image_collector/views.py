from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, Images
from .forms import *
from django.views.decorators.csrf import csrf_exempt
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import os

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

@csrf_exempt
def image_upload(request): 
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
            image_path = os.getcwd()+'/media/images/'+form.cleaned_data['name']
            saved =  detect_faces(image_path) 
            return redirect('success') 
    else: 
        form = ImageForm() 
    return render(request, 'image_collector/class_image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 

def view_images(request):
    context = {
        'images' : Images.objects.all()
    }
    return render(request, 'image_collector/view_images.html', context)

def process_images():
    return True

def detect_faces(img_name):
    known_face_encodings = np.load(os.getcwd()+'/image_collector/face_encodings.npy', allow_pickle=True)
    known_face_names = np.load(os.getcwd()+'/image_collector/names.npy', allow_pickle=True)

    # Load an image with an unknown face
    unknown_image = face_recognition.load_image_file(img_name)

    # Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    pil_image = Image.fromarray(unknown_image)
    # Create a Pillow ImageDraw Draw instance to draw with
    draw = ImageDraw.Draw(pil_image)

    students_present = []
    # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = str(known_face_names[best_match_index])
            students_present.append(name)

        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        # Draw a label with a name below the face
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
        pil_image.save('C:/Users/yashw/web_project/image_project/image_collector/output1.jpg')
    return True