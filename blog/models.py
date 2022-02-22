from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name=models.CharField( max_length=100,null=True)
    def __str__(self):
        return self.name
class Blog(models.Model):
    cat=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100,null=True)
    sdes=models.TextField(null=True)
    long_des = models.TextField(null=True)
    images=models.FileField(null=True)
    date = models.DateField(null=True)
    def __str__(self):
        return self.title
class user_detail(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    images=models.FileField(null=True)
    mobile_no=models.IntegerField(null=True)
    def __str__(self):
        return self.usr.username
class like_blog(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    blog_like = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.usr.username+"_"+self.blog_like.title

class user_comment(models.Model):
    blogdata=models.ForeignKey(Blog,on_delete=models.CASCADE)
    usr=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment=models.TextField(null=True)
    date=models.DateField(null=True)
    images=models.FileField(null=True)

    def __str__(self):
        return self.blogdata.title
class message(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    subject=models.CharField(max_length=100,null=True)
    message=models.TextField(null=True)
    def __str__(self):
        return self.name




