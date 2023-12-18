from django.shortcuts import redirect, render
from app.models import Categories

def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    context = {
        'category': category,
    }

    return render(request,'main/home.html')


def SINGLE_COURSE(request):
    return render(request, "main/single_course.html")


def CONTACT_US(request):
    return render(request,'main/contact_us.html')


def ABOUT_US(request):
    return render(request, 'main/about_us.html')