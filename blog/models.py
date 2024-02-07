from django.db import models

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class ClassName(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.class_name}"

class AssessmentAreas(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.full_name}"

class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    answers = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.answers}"

class Awards(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    subject_score = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.subject, self.subject_score}"