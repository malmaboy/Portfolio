from django.db import models


# Create your models here.


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
    projectDescription = models.TextField(max_length=500, default=2)

    def __str__(self):
        return self.projectName, self.projectLink


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


