from django.db import models
from mobilesoftn import settings
from django.conf.global_settings import AUTH_USER_MODEL
# from django.urls import reverse
from embed_video.fields import EmbedVideoField

class Video (models.Model) :
    title = models.CharField(max_length=150)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __unicode__(self):
        return self.title

    class Meta :
        ordering = ['-added']


class ReqUser(models.Model):
    nom = models.CharField(max_length=200, null=True, blank=True)
    objetreq = models.CharField(max_length=200, null=True, blank=True)
    datereq = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    tel = models.CharField(max_length=50, null=True, blank=True)
    whatsap = models.CharField(max_length=50, null=True, blank=True)
    faceb = models.CharField(max_length=150, null=True, blank=True)
    siteweb = models.CharField(max_length=100, null=True, blank=True)
    activite = models.CharField(max_length=200, null=True, blank=True)
    besoin= models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):        
        return self.nom


class Traduc(models.Model):

    texte = models.CharField(max_length=250, null=True, blank=True, unique=True)
    formulaire = models.CharField(max_length=250, null=True, blank=True)
    ordre = models.CharField(max_length=250, null=True, blank=True)
    texte_fr = models.TextField(null=True, blank=True)
    texte_eng = models.TextField(null=True, blank=True)
    
    def __str__(self):        
            return self.texte

class Langue(models.Model):

    enCours = models.CharField(max_length=25, null=True, blank=True, unique=True)
    
    def __str__(self):        
            return self.enCours
