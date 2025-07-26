from django.shortcuts import render,redirect
from.models import *
from django.http import HttpResponse

def recepies(request):
    if request.method == 'POST':
        data= request.POST
        recepie_name = data.get('recepie_name')
        recepie_description = data.get('recepie_description') 
        recepie_image= request.FILES.get('recepie_image')
        
        Recepie.objects.create(
            recepie_name=recepie_name,
            recepie_description=recepie_description,
            recepie_image=recepie_image
        )
        return redirect('/recepies')

    querySet=Recepie.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        print(search)
        querySet=querySet.filter(recepie_name__icontains=search)
    context={
        'recepies':querySet
    }
    return render(request,'recepies.html',context)


def delete_recepie(request,id):
    
    queryset=Recepie.objects.get(id=id)
    queryset.delete()
    return redirect('/recepies')
   
def update_recepie(request,id):
    
    queryset=Recepie.objects.get(id=id)
    
    if request.method == 'POST':
        data=request.POST
        queryset.recepie_name=data.get('recepie_name')
        queryset.recepie_description=data.get('recepie_description')
        queryset.recepie_image=request.FILES.get('recepie_image')
        
        queryset.save()
        return redirect('/recepies')
    context={
        "recepie":queryset
    }
    return render(request,'update_recepie.html',context)
   