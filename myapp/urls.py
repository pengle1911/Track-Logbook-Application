from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('new-entry/', views.new_entry, name='new_entry'),  
    path('all-entries/', views.all_entries, name='all_entries'),  
    path('progression/', views.progression, name='progression'),  
    path('pictures-videos/', views.pictures_videos, name='pictures_videos'),  
]
