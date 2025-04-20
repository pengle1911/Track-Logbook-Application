from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new-entry/', views.new_entry, name='new_entry'),
    path('all-entries/', views.all_entries, name='all_entries'),
    path('entry/', views.view_entry, name='view_entry'),
    path('progression/', views.progression, name='progression'),
    path('pictures-videos/', views.pictures_videos, name='pictures_videos'),
    path('success/', views.success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
