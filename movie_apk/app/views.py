from django.shortcuts import render

# Create your views here.




def booking(request):
    return render(request,'booking.html')

def seat(request):
    return render(request,'seat.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')