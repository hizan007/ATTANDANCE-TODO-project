from django.db import models

# Create your models here.
class attandance(models.Model):
    studentdept=models.CharField(max_length=100)
    studentbatch=models.CharField(max_length=100)
    studentyear=models.DateField()
    attandance=models.CharField(max_length=100)


    def __str__(self):
        return self.studentbatch