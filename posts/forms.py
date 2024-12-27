from django import forms

class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    discription = forms.CharField()