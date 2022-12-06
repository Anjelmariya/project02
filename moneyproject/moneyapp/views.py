from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from.models import People

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=People.objects.all()
    return render(request, "index.html",{'result':obj,'result1':obj1})






#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #res1=x+y
    #res2=x-y
    #res3=x/y
    #res4=x*y
    #return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})

#def home(request):
    #return HttpResponse("am home")
#def about(request):
    #return render(request,"about.html")
#def contact(request):
    #return HttpResponse("hello am contact")
#def detail(request):
    #return render(request,"detail.html")
#def thankyou(request):
    #return HttpResponse("thanks")
