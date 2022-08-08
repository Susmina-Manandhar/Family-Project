from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

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


    #d2.save()
    #to delete the specific data
   
def userform(request):
    sum=0
    try:
        n1 = request.GET['num1']
        n2 = request.GET['num2']
        sum = n1+n2
    except:
        pass
    return render(request,"name.html",{'output':sum})
