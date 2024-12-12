from django import forms
from .models import Appointment
from .models import ImageModel

class AppointmentForm(forms.ModelForm):
    class Meta:
        #gives additional information about the form

        model = Appointment
        #fields = ['name', 'email', 'phone', 'date', 'time', 'department', 'doctor']
        fields = '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        #fields = ['image','title','price']

        fields = '__all__'
