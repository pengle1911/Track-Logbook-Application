from django import forms
from .models import Entry

class NewEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'date', 'location', 'workout', 'attachment', 'rest_day', 'race_day']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'workout': forms.Textarea(attrs={'placeholder': 'Workout details'}),
        }
