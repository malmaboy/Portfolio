import datetime
import time
from statistics import mode
import urllib.request
from django.db import models
from django.core.files import File
import os

# Create your models here.
from django.utils import timezone


class Topics(models.Model):
    topicsName = models.CharField(max_length=40)
    topicsSubject = models.CharField(max_length=30, default="default")

    def __str__(self):
        return self.topicsName

    @classmethod
    def filter(cls, topicsSubject):
        pass


class Projects(models.Model):
    projectName = models.CharField(max_length=50)
    projectLink = models.TextField(max_length=200)
    projectImage = models.ImageField(upload_to='ProjectImages/')
    projectDescription = models.TextField(max_length=500, default=2)

    def __str__(self):
        return self.projectName


class Subject(models.Model):
    subjectName = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    semester = models.IntegerField(default=1)
    ects = models.IntegerField(default=4)
    lective_Year = models.CharField(max_length=10)
    topics = Topics.objects.all()
    rank = models.IntegerField(default=1)
    professor = models.CharField(max_length=50)
    project = Projects.objects.all()

    def __str__(self):
        return self.subjectName


class ProgrammingLanguages(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class NonProgrammingLanguages(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Description(models.Model):
    description = models.TextField(max_length=4000)
    number = models.IntegerField(default=1)


class Tech(models.Model):
    name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=5)
    creatorName = models.CharField(max_length=30)
    link = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='TechImages/')
    year = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class labs(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField(default="Description")

    def __str__(self):
        return self.name


class news(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="Text")
    image = models.ImageField(upload_to='newsImages/')
    newsLink = models.URLField(default="URl")

    def __str__(self):
        return self.title


class BlogsAnswers(models.Model):
    titulo = models.CharField(max_length=10)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    data = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.titulo


class tfcs(models.Model):
    author = models.CharField(max_length=50)
    advisor = models.CharField(max_length=50)
    year = models.CharField(max_length=4, default="2022")
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='tfcsImages/')
    reportLink = models.CharField(max_length=500)
    gitLink = models.CharField(max_length=500)
    resume = models.TextField(max_length=2000, default="Resume")
