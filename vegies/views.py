from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    return redirect('f_recepies')

def f_recepies(request):
    # Handle form submission for adding a new recepie INTO the database
    # If the request method is POST, it means the form has been submitted
    if request.method=='POST':
        data=request.POST
        print(data)
        recepie_name=data.get('recepie_name')
        recepie_description=data.get('recepie_description')
        recepie_image=request.FILES.get('recepie_image')

        Recepies.objects.create(
            recepies_name=recepie_name,
            recepies_description=recepie_description,
            recepies_image=recepie_image
        )
        # Redirect to the same page to show the updated list of recepies
        return redirect('f_recepies')  
    # Fetch all recepies from the database
    # and pass them to the template
    
    if request.GET.get('search'):
        search=request.GET.get('search')
        data=Recepies.objects.filter(recepies_name__icontains=search)
        context={
            'recepies':data
        }
        return render(request,'f_recepies.html',context)
    
    queryset=Recepies.objects.all()
    context = {
        'recepies': queryset,
    }
    return render(request,'f_recepies.html',context)

def delete_recepies(request,id):
    #fetch the recepie by id and use it to delete the recepie
    queryset=Recepies.objects.get(id=id)
    
    queryset.delete()
    # Redirect to the f_recepies page after deletion
    return redirect('f_recepies')

def update_recepies(request, id):
    # Fetch the recipe by ID
    recepie= Recepies.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        recepie.recepies_name = data.get('recepies_name')
        recepie.recepies_description = data.get('recepies_description')

        if 'recepie_image' in request.FILES:
            recepie.recepies_image = request.FILES['recepie_image']

        recepie.save()
        return redirect('f_recepies')  # Redirect after successful update

    context = {
        'recepie': recepie # passing single object (not iterable)
    }
    return render(request, 'update_f_recepies.html', context)



    