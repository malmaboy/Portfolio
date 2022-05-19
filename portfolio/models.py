from django.db import models


# Create your models here.


class subjects(models.Model):
    def __init__(self, name, year, semester, etcs, lective_year, topics, rank,
                 prof, projects, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.year = year
        self.semester = semester
        self.etcs = etcs
        self.lective_year = lective_year
        self.topics = topics
        self.rank = rank
        self.prof = prof
        self.projects = projects


class ProgrammingLanguages(models.Model):
    name = models.CharField(max_length=40)