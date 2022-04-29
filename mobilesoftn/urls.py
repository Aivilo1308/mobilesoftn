from django.contrib import admin
from django.urls import path, include
from requests import Session    
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from mstart import views as mstart_view
# from blog import views as blog_view

urlpatterns = [ 
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns ( 
    path('',mstart_view.index, name='accueil'),
    path('blogs/', mstart_view.blogList, name='blog-articles'),                                   
    path('requete1/',mstart_view.requete1, name='requete11'),    
    path('infoparution1/',mstart_view.infoparution1, name='infoparution1'),
    path('infoparution2/',mstart_view.infoparution2, name='infoparution2'),
    path('infoparution3/',mstart_view.infoparution3, name='infoparution3'),

)