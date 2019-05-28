from django.shortcuts import render
from .models import Staff

# Create your views here.
def home(request):
    return render(request,'homepage.html',{})
def gallery(request):
    details = Staff.objects.all()
    return render(request,'gallerypage.html',{'Staff_list':details})
def about(request):
    return render(request,'aboutpage.html',{})
def contact(request):
    return render(request,'contactpage.html',{})
