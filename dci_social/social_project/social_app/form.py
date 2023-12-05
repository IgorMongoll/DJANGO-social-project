from django import forms



class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea)
    age = forms.IntegerField()
    
class PostForm(forms.Form):
    post = forms.CharField(widget=forms.Textarea)
    PUBLIC = 'public'
    PRIVATE = 'private'
    VISIBILITY_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    ]
    visibility =forms.ChoiceField(choices=VISIBILITY_CHOICES)

