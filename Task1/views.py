from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profiles
from django.contrib import messages

def EditProfile(request,pk):
    profile = Profiles.objects.get(id = pk)
    context = {
        'profile':profile
    }
    if request.POST:
        if request.POST.get('action') == 'confirm':
            profile.name = request.POST.get('name')
            profile.username = request.POST.get('username')
            profile.email= request.POST.get('email')
            profile.id = pk

            profile.save()
            messages.success(request, "Profile details updated.")
            return redirect('home-page')
        elif request.POST.get('action')=='cancel':
            return redirect('home-page')
    else:
     return render(request,'Task1/Update.html',context)

def HomePage(request):
    context = {
        'Profiles':Profiles.objects.all(),
    }




    return render(request,'Task1/index.html',context)

def AddProfile(request):
    if request.method == 'POST':
         if request.POST.get('action') == 'confirm':
            name = request.POST.get('name')
            username = request.POST.get('username')
            email= request.POST.get('email')
            id = Profiles.objects.last().id + 1

            profile=Profiles.objects.create(
                name = name,
                username = username,
                email = email,
                id = id,
            )
            profile.save()
            messages.success(request, "Profile Added Succesfully")
            return redirect('home-page')
         elif request.POST.get('action')=='cancel':
            return redirect('home-page')
        
    else:

      return render(request, 'Task1/AddUser.html',)
    
    
def DeleteProfile(request,pk):
   profile = Profiles.objects.get(id = pk)
   context = {
      'profile':profile
   }

   if request.POST:
      if request.POST.get('action') == 'confirm':
         profile.delete()
         messages.info(request, "Account Deleted")
         return redirect('home-page')
      elif request.POST.get('action')=='cancel':
         return redirect('home-page')
   else:
      
    return render(request,'Task1/Delete.html',context)
   

# Create your views here.
