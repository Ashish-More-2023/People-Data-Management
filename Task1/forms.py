from django.forms import forms,ModelForm
from .models import Profiles

class AddProfileForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['name','username','email','id']


class ProfileUpdate(ModelForm):
      class Meta:
        model = Profiles
        fields = ['name','username','email','id']  

