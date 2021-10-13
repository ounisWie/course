from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return self.name

    

class Course(models.Model):
    title = models.CharField(max_length=50,blank=True,null=True)
    category = models.ForeignKey(Categories,on_delete=models.PROTECT,blank=True,null=True)
    course_level = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    image = models.ImageField(upload_to="courses/images")
    video_link = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.title

class Unit(models.Model):
    article = models.CharField(max_length=100,blank=True,null=True)
    desc = models.TextField(max_length=5000,blank=True,null=True)
    belongs = models.ForeignKey(Course,on_delete=models.PROTECT,blank=True,null=True)