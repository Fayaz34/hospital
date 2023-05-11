from django.shortcuts import render
from django.http import HttpResponse
from.models import Departments,Doctors,Booking
from.forms import Bookingform

def index(request):
    return render(request, 'index.html')

def about(request):
     return render(request, 'about.html')

def booking(request):
     if(request.method=='POST'):
          booking_form = Bookingform(request.POST)
          if booking_form.is_valid():
               booking_form.save()
     booking_form = Bookingform()
     dict_form = {
          'booking_form':booking_form
     }          

     return render(request, 'booking.html',dict_form)

def doctors(request):
     dict_Doc={
          'doct': Doctors.objects.all()
     }
     return render(request, 'doctors.html',dict_Doc)

def contact(request):
     return render(request, 'contact.html')

def department(request):
     dict_dep={
          'dept': Departments.objects.all()
     }
     return render(request, 'department.html',dict_dep)
