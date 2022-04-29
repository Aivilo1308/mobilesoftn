from django.http.response import HttpResponse
from django.shortcuts import render
from .models import ReqUser, Traduc, Video

# from django.utils.translation import gettext as _
# from django.utils.translation import activate, get_language, gettext


def index(request):    

    context={}
    videos=Video.objects.all()
#     traduc_Main = Traduc.objects.filter(formulaire__iexact =  'Main.html')
#     traduc_Index_Entete = Traduc.objects.filter(formulaire__iexact =  'Index.html-Entete')

#     # print(list(traduc))

    context['videos']=videos
#     context['traduc_Main']=traduc_Main
#     context['traduc_Index_Entete']=traduc_Index_Entete
    return render(request,'index.html', context)


def blogList(request):    
    return render(request,'blog.html')

def requete1(request): 
    print(request.POST['nom'])
    print(request.POST['email'])

    msg=""
    if request.method=='POST':
        if request.POST.get('nom') and request.POST.get('email'):
            
            # print('Je suis dans le if')
            
            nom = request.POST['nom']
            objetreq = request.POST['objetreq']
            email = request.POST['email']
            tel = request.POST['whatsapp']
            whatsap = request.POST['whatsapp']
            faceb = request.POST['facebook']
            siteweb = request.POST['siteweb']
            activite = request.POST['activite']
            besoin = request.POST['besoin']        
        
            ReqUser.objects.create(
                nom = nom,
                objetreq = objetreq,
                email = email,
                tel = tel,
                whatsap = whatsap,
                faceb = faceb,
                siteweb = siteweb,
                activite = activite,
                besoin = besoin
            ) 
              
            msg="Enregistrée avec succès!"
        else :
            msg="Erreur de données!"

        return HttpResponse(msg)


def infoparution1(request) :
    msgFr=""
    msgEn=""
    designationFr="Accompagnement digital de jeunes entreprises"
    designationEn="Digital support for start-ups"
    context={}
    context['designationFr']=designationFr
    context['designationEn']=designationEn


    if request.method=='POST' :
        
        if request.method=='POST':
            if request.POST.get('name-infoprochaineparution1') and request.POST.get('email-infoprochaineparution1'):
                nom = request.POST['name-infoprochaineparution1']
                objetreq = designationFr
                email = request.POST['email-infoprochaineparution1']
                tel = request.POST['whatsapp-infoprochaineparution1']
                whatsap = request.POST['whatsapp-infoprochaineparution1']
                faceb = request.POST['facebook-infoprochaineparution1']
                siteweb = request.POST['basic-url-infoprochaineparution1']
                activite = request.POST['activite-infoprochaineparution1']
                besoin = request.POST['besoin-infoprochaineparution1']
            
                ReqUser.objects.create (
                    nom = nom,
                    objetreq = objetreq,
                    email = email,
                    tel = tel,
                    whatsap = whatsap,
                    faceb = faceb,
                    siteweb = siteweb,
                    activite = activite,
                    besoin = besoin
                )   

                msgFr="Enregistrée avec succès!"
                msgEn="Saved successfully!"
            else :
                msgFr="Erreur de données!"
                msgEn="Data error!"

            context['msgFr']=msgFr
            context['msgEn']=msgEn

            return render(request,'infoparution.html', context)        

    return render(request,'infoparution.html', context)


def infoparution2(request) :
    designationFr="Atelier de formation en ligne aux métiers du digital"
    designationEn="Online workshop for digital professions"
    context={}
    context['designationFr']=designationFr
    context['designationEn']=designationEn

    if request.method=='POST' :
        msgFr=""
        msgEn=""
        if request.method=='POST':
            if request.POST.get('name-infoprochaineparution1') and request.POST.get('email-infoprochaineparution1'):
                nom = request.POST['name-infoprochaineparution1']
                objetreq = designationFr
                email = request.POST['email-infoprochaineparution1']
                tel = request.POST['whatsapp-infoprochaineparution1']
                whatsap = request.POST['whatsapp-infoprochaineparution1']
                faceb = request.POST['facebook-infoprochaineparution1']
                siteweb = request.POST['basic-url-infoprochaineparution1']
                activite = request.POST['activite-infoprochaineparution1']
                besoin = request.POST['besoin-infoprochaineparution1']
            
                ReqUser.objects.create (
                    nom = nom,
                    objetreq = objetreq,
                    email = email,
                    tel = tel,
                    whatsap = whatsap,
                    faceb = faceb,
                    siteweb = siteweb,
                    activite = activite,
                    besoin = besoin
                )   

                msgFr="Enregistrée avec succès!"
                msgEn="Saved successfully!"
            else :
                msgFr="Erreur de données!"
                msgEn="Data error!"

            context['msgFr']=msgFr
            context['msgEn']=msgEn
            return render(request,'infoparution.html', context)        

    return render(request,'infoparution.html', context)


def infoparution3(request) :
    designationFr="Applications web pour restaurants, hôpitaux, pharmacies, etc."
    designationEn="Web Application for restaurants, medical clinic, pharmacies, etc."
    context={}
    context['designationFr']=designationFr
    context['designationEn']=designationEn

    if request.method=='POST' :
        msgFr=""
        msgEn=""
        if request.method=='POST':
            if request.POST.get('name-infoprochaineparution1') and request.POST.get('email-infoprochaineparution1'):
                nom = request.POST['name-infoprochaineparution1']
                objetreq = designationFr
                email = request.POST['email-infoprochaineparution1']
                tel = request.POST['whatsapp-infoprochaineparution1']
                whatsap = request.POST['whatsapp-infoprochaineparution1']
                faceb = request.POST['facebook-infoprochaineparution1']
                siteweb = request.POST['basic-url-infoprochaineparution1']
                activite = request.POST['activite-infoprochaineparution1']
                besoin = request.POST['besoin-infoprochaineparution1']
            
                ReqUser.objects.create (
                    nom = nom,
                    objetreq = objetreq,
                    email = email,
                    tel = tel,
                    whatsap = whatsap,
                    faceb = faceb,
                    siteweb = siteweb,
                    activite = activite,
                    besoin = besoin
                )   

                msgFr="Enregistrée avec succès!"
                msgEn="Saved successfully!"
            else :
                msgFr="Erreur de données!"
                msgEn="Data error!"

            context['msgFr']=msgFr
            context['msgEn']=msgEn
            return render(request,'infoparution.html', context)        

    return render(request,'infoparution.html', context)
