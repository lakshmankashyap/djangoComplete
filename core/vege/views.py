from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def recipe(request):
    if request.method == 'POST':
        data=request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')

        # print(name)
        # print(description)
        # print(image)
        Recipe.objects.create(
            name=name,
            description=description,
            image=image,
        )
        
        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()
    context = {'recipes':queryset}
    return render(request,'recipes.html',context)

def delete_recipe(request,id):
    print(id)
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')
