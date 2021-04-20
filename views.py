from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Admission
from .models import Contact
from .forms import AdmissionForm
from .forms import ContactForm
#from django.contrib import messages

def home(request):

   return render(request, 'index.html', {})

def admission(request):
   #all_Admissions = Admission.objects.all()
   #return render(request, 'admission.html', {"allAdmissions" : all_Admissions})
   #print(all_Admissions)

   #context = { "allAdmissions" : allAdmissions}
   if request.method == 'POST':
      form = AdmissionForm(request.POST)
      if form.is_valid():

         name = request.POST.get('name', '')
         email = request.POST.get('email', '')
         dob = request.POST.get('dob', '')
         city = request.POST.get('city', '')
         mobile_number = request.POST.get('mobile_number', '')
         gender = request.POST.get('gender', '')
         appiled_for = request.POST.get('appiled_for', '')
         admission_obj = Admission(name = name, email = email, dob = dob, city = city, mobile_number = mobile_number, gender = gender, appiled_for = appiled_for)
         admission_obj.save()

         return redirect('home')

   else:
      form = AdmissionForm()
   return render(request, 'admission.html', {'form' : AdmissionForm})


def about(request):
   return render(request,'about.html',{})

def contact(request):
   if request.method == 'POST':
      form = AdmissionForm(request.POST)
      if form.is_valid():
         name = request.POST.get('name', '')
         email = request.POST.get('email', '')
         message = request.POST.get('message', '')
         contact_obj = Contact(name=name, email=email, message = message)
         contact_obj.save()

         return redirect('home')

   else:
      form = ContactForm()
   return render(request, 'contact.html', {'form': ContactForm})
