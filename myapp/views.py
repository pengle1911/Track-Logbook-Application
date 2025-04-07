from django.shortcuts import render, get_object_or_404
from datetime import date, timedelta
from .models import Entry

def home(request):
    return render(request, 'myapp/home.html')

def new_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html') 
    else:
        form = EntryForm()
    return render(request, 'myapp/new_entry.html', {'form': form})

def all_entries(request):
    today = date.today()
    first_day = today.replace(day=1)
    last_day = (first_day.replace(month=(first_day.month % 12) + 1, day=1) - timedelta(days=1))
    days = [{'date': first_day + timedelta(days=i)} for i in range((last_day - first_day).days + 1)]
    return render(request, 'myapp/all_entries.html', {'days': days})

def view_entry(request):
    selected_date = request.GET.get('date')
    if selected_date:
        entry = get_object_or_404(Entry, date=selected_date)
        return render(request, 'myapp/view_entry.html', {'entry': entry})
    return render(request, 'myapp/no_entry.html')  

def progression(request):
    return render(request, 'myapp/progression.html')  

def pictures_videos(request):
    return render(request, 'myapp/pictures_videos.html')  
