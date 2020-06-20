from django.shortcuts import render , HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
#    return HttpResponse("this is my home page('/')")
    context={'name':'wicky','course':'python'}
    return render(request,'home.html',context)


def about(request):
#     return HttpResponse("This is my about page('/')t")   
    return render(request,'about.html')

def socialicon(request):
#     return HttpResponse("This is my about page('/')t")   
    return render(request,'socialicon.html')    


def projects(request):
#     return HttpResponse("this is my projects page('/')")   
    return render(request,'projects.html')


def contact(request):
#     return HttpResponse("this is my contact page('/')")
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
    #    print(name , email , phone , context) 
        ins= Contact(name=name, email= email, phone= phone, desc= desc)   
        ins.save();
        print("the data have been uploaded")
    return render(request,'contact.html')
