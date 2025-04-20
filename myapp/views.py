from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Entry
from .forms import NewEntryForm
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, "myapp/home.html")

def new_entry(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success") 
    else:
        form = NewEntryForm()
    return render(request, "myapp/new_entry.html", {"form": form})

def success(request):
    return render(request, "myapp/success.html")

def all_entries(request):
    entries = Entry.objects.all().order_by("-date")
    return render(request, "myapp/all_entries.html", {"entries": entries})

def view_entry(request):
    selected_date = request.GET.get("date")
    entry = Entry.objects.filter(date=selected_date).first() 

    if not entry:
        return render(request, "myapp/no_entries.html", {"date": selected_date})

    return render(request, "myapp/view_entry.html", {"entry": entry})

    
def progression(request):
    return render(request, "myapp/progression.html")

def pictures_videos(request):
    entries_with_attachments = Entry.objects.filter(attachment__isnull=False)

    filtered_entries = [entry for entry in entries_with_attachments if entry.attachment and entry.attachment.name]

    return render(request, "myapp/pictures_videos.html", {"entries": filtered_entries})
