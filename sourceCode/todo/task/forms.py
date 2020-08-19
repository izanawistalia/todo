from django.forms import ModelForm
from .models import task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class addForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(addForm, self).__init__(*args, **kwargs)
        #self.fields['author'].disabled = True
    class Meta:
        model = task
        fields = "__all__"


class createUserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"#['username', 'email', 'password', 'password_(again)']
