from django import forms
from django.forms import ModelForm
from .models import BlogsAnswers


class BlogForm(ModelForm):
    class Meta:
        model = BlogsAnswers
        fields = ['titulo', 'firstName', 'lastName', 'description']

        labels = {
            'titulo': 'Title',
            'firstName': 'First Name',
            'lastName': 'Last Name',
            'description': 'Description',


        }

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }

