from django.contrib import admin
# from embed_video import AdminVideoMixin
from .models import Video, ReqUser, Traduc, Langue

admin.site.register(Video)

class RequeteAdmin(admin.ModelAdmin):
    list_display = ('nom','objetreq')
    list_filter =('objetreq',)   

admin.site.register(ReqUser, RequeteAdmin)

class TraducAdmin(admin.ModelAdmin):
    list_display = ('texte','formulaire', 'ordre')
    list_filter =('formulaire',)   

# Register your models here.
admin.site.register(Traduc, TraducAdmin)

admin.site.register(Langue)