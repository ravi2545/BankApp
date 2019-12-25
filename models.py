from django.db import models

# Create your models here.

class project(models.Model):
    project_name=models.CharField(max_length=20, default=None, blank=True)

    def __str__(self):
        return str(self.project_name)


class kalyan(models.Model):
    gender = (("male", "male"), ("female", "female"))
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0, blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=6, choices=gender, default=gender[0][0], blank=True)
    real_project=models.ForeignKey('project', on_delete=models.CASCADE(), blank=True)


    def __str__(self):
        return str(self.name)
