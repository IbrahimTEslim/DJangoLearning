from django.db.models import fields
from .models import Apply,job
from django import forms

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','mail','website','cv','cover_letter']

class PostJob(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = 'slug','owner'