from django.db import models



class Course(models.Model):
    price       = models.TextField() 
    course_by   = models.TextField()  
    title       = models.TextField()  
    skills      = models.TextField() 
    ratings     = models.FloatField()  
    reviews     = models.TextField()  
    level       = models.TextField()  
    type        = models.TextField() 
    duration    = models.TextField() 

    def __str__(self):
        return self.title
