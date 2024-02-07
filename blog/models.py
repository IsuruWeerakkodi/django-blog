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



#create models
#flush database
#make migrations
#migrate
#complete admin.py
#create super user
#populate databse script run
#schools.html  -> create other htmls
#COMPLETE URL.PY WITH OTHER HTML (BLOG/URL.PY)
#complete views