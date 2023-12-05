from django import forms
from .models import User,Post

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','bio','age']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post','visibility']