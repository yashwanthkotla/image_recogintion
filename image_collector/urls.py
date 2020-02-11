from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='image-home'),
    path('about/',views.about, name='image-about'),
    path('test/',views.test, name='image-test'),
    path('image_upload/', views.image_upload, name = 'image_upload'),
    path('success/', views.success, name = 'success'),
    path('view_images/', views.view_images, name = 'view_images'),
]

