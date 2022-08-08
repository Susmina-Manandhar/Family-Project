from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from Members.models import information,profession,overall

# Create your views here.
def response(request):
    #to create or add data to table
    #val = information.objects.create(name="Looja", age =20, gender = "Male")
    #to retrieve all objects
    #d1 = information.objects.all()
    #d2 = profession.objects.all()
    #d1.delete()
    #d2.delete()

    # to incorporate data into Httpresponse
    #for x in d1:
    #   return HttpResponse(f'Hi It worked!{x}')
    #to fetch a single data or specific data
    #d2 = information.objects.get(pk=2)
    #d2.name = "XYZ"
 #d2.delete()
    #return HttpResponse(f'You got it{d2}')
    return HttpResponse('You got it')

def nameform(request):
    if request.method == "POST":
        form = nameform(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = nameform()
    return render(request, 'name.html', {'form': form})    
    #d2.save()
    #to delete the specific data
   
