from django.db import models

"""
    posts = post.object.all() == SELECT * FROM posts
    posts = post.object.get(id=1)
    posts = post.object.filter(name="a")
    posts = post.object.create()
    
"""

class Catigory(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title


class Post(models.Model):
    Catigory=models.ForeignKey(Catigory,on_delete=models.CASCADE,null=True,blank=True)
    tags=models.ManyToManyField(Tag,null=True,blank=True)
    title=models.CharField(max_length=56)
    discription=models.CharField(max_length=256)
    rate=models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at =models.DateTimeField(auto_now=True, null=True)
    image=models.ImageField(null=True, blank=True)
    def __str__(self):
        return f"{self.title}: {self.discription}"
# Create your models here.
