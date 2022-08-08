from pickle import TRUE
from django.db import models

# Create your models here.
class information(models.Model):
    genderchoice = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=TRUE)
    gender = models.TextField(blank=TRUE, choices = genderchoice)
  

    def __str__(self):
        return (self.name)
    
class profession(models.Model):
    namelist = models.OneToOneField(information,on_delete= models.CASCADE, default="1")
    #professionlist = models.OneToOneField(information, related_name = 'professionlist',on_delete=models.CASCADE)
    professions  = models.TextField()

class overall(models.Model):
    namelist = models.OneToOneField(information,on_delete= models.CASCADE, default = "1")
    project = models.TextField(blank = True)