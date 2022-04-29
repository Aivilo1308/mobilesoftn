
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.db.models.deletion import SET_NULL
from mobilesoftn import settings
from django.conf.global_settings import AUTH_USER_MODEL

# Create your models here.

upload_location = FileSystemStorage(location=settings.MEDIA_ROOT)


class BlogPost(models.Model):
    titre = models.CharField(max_length=150, null=True, blank=True)
    auteur = models.ForeignKey(AUTH_USER_MODEL, default=1, null=True, on_delete=SET_NULL)
    dateBlog = models.DateField(auto_now=False, auto_now_add=True, null=True)
    contenu = models.TextField(null=True)
    extrait = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(default='avatar.png', upload_to = 'Blog_Images')
    dateExpire = models.DateField(null=True,blank=True)

    def __str__(self):        
        return self.titre

class LikesPost(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, default=1, null=True, on_delete=SET_NULL)
    blogPost = models.ForeignKey(BlogPost, verbose_name='Post', null=True, on_delete=models.SET_NULL) 
    dateLike = models.DateField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):        
        return self.dateLike

class CommentsPost(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, default=1, null=True, on_delete=SET_NULL)
    blogPost = models.ForeignKey(BlogPost, verbose_name='Post', null=True, on_delete=models.SET_NULL) 
    comment = models.TextField(null=True, blank=True)
    dateComment = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):        
        return self.dateComment
