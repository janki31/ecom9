from django.db import models

# Create your models here.

class Blogpost(models.Model):
    blogid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    desc=models.TextField(default="")
    head0=models.CharField(max_length=20,default="")
    chead0=models.CharField(max_length=1500,default="")
    head1=models.CharField(max_length=20,default="")
    chead1=models.CharField(max_length=1500,default="")
    head2=models.CharField(max_length=20,default="")
    chead2=models.CharField(max_length=1500,default="")
    pub_date=models.DateField(default="")
    image_file=models.ImageField(upload_to='blog/images',default="")

    def __str__(self):
        return self.title
