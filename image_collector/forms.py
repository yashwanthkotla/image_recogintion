from django import forms 
from .models import *
  
class ImageForm(forms.ModelForm): 
    class Meta: 
        model = Images 
        fields = ['name', 'class_img'] 