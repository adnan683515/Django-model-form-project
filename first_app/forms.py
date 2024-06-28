from django import forms
from . import models

class studentFrom(forms.ModelForm):
    class Meta:
        model = models.studentModel
        fields = '__all__'
        # fields = ['name','roll']
        # exclude = []
        labels = {
            'name':'Student Name',
            'roll':'Student Roll',
            'address':'Student Address'
        }
        help_texts = {
            'name':'Enter Your full name',
            'roll':'Enter Your Roll'
        }
        widgets = {
            
            'name': forms.TextInput(attrs={'class':'btn-primary'}),
            
            
        }