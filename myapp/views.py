from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NewEntryForm  

def home(request):
    return render(request, 'myapp/home.html')  

def new_entry(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('/')  
    else:
        form = NewEntryForm()  
    return render(request, 'myapp/new_entry.html', {'form': form})  

def all_entries(request):
    return render(request, 'myapp/all_entries.html') 

def progression(request):
    return render(request, 'myapp/progression.html')  

def pictures_videos(request):
    return render(request, 'myapp/pictures_videos.html')  
