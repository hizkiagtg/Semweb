from django.db import models

# Create your models here.
class Provider(models.Model):
    name        = models.CharField(max_length=255)  
    description = models.TextField()  

    def __str__(self):
        return self.name

class Course(models.Model):
    price       = models.TextField() 
    course_by   = models.ForeignKey(Provider, on_delete=models.CASCADE)  
    title       = models.TextField()  
    skills      = models.TextField() 
    ratings     = models.FloatField()  
    reviews     = models.TextField()  
    level       = models.TextField()  
    type        = models.TextField() 
    duration    = models.TextField() 

    def __str__(self):
        return self.title
