from django import forms
from django.forms import ModelForm

import portfolio.models
from .models import BlogsAnswers
from .models import tfcs


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


class TfcsForm(ModelForm):
    class Meta:
        model = tfcs
        fields = ['author', 'advisor', 'image', 'year', 'title', 'gitLink', 'reportLink', 'resume']

        labels = {
            'title': 'Title',
            'author': 'Author',
            'advisor': 'Advisor',
            'image': 'Insert Image',
            'gitLink': 'Git Hub Link',
            'reportLink': 'Report Link',
            'resume': 'Resume',

        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Silva'}),
            'advisor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nuno Mendes'}),
            'year': forms.TextInput(),
            'gitLink': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Git Hub Link'}),
            'reportLink': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Report Link'}),
            'resume': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Resume'}),

        }
