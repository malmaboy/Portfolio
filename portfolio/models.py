from django.db import models


# Create your models here.


class Topics(models.Model):
    topicsName = models.CharField(max_length=40)

    def __str__(self):
        return self.topicsName


class Projects(models.Model):
    projectName = models.CharField(max_length=50)
    projectLink = models.TextField(max_length=100)

    def __str__(self):
        return self.projectName, self.projectLink


class Subject(models.Model):
    subjectName = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    semester = models.IntegerField(default=1)
    ects = models.IntegerField(default=4)
    lective_Year = models.CharField(max_length=10)
    # topics = models.ForeignKey('Topics', default=1, on_delete=models.CASCADE)
    rank = models.IntegerField(default=1)
    professor = models.CharField(max_length=50)
    project = Projects.projectName
    projectLink = Projects.projectLink

    def __str__(self):
        return self.subjectName


class ProgrammingLanguages(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
