from django.contrib import admin
from .models import BlogPost, LikesPost, CommentsPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('titre','extrait','auteur')
    list_filter =('tags',)   

class CommentsPostAdmin(admin.ModelAdmin):
    list_display = ('user','blogPost','comment')
    list_filter =('blogPost',) 

# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(LikesPost)
admin.site.register(CommentsPost, CommentsPostAdmin)
