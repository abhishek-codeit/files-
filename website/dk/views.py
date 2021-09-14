from django.shortcuts import render
from dk.models import Contact


# Create your views here.
def index(request):
   return render(request, 'index.html')



def cont(request):
   if request.method == 'POST':
      cont=Contact()
      cont.name= request.POST.get('name')
      cont.email= request.POST.get('email')
      cont.branch= request.POST.get('branch')
      cont.usn= request.POST.get('usn')
      cont.year= request.POST.get('year')
      cont.save()
   return render(request, 'contact.html')



def events(request):
   return render(request, 'events.html')

def about(request):
   return render(request, 'about.html')

def contact(request):
   return render(request, 'contact.html')

