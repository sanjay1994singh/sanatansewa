from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def sewa(request):
    return render(request, 'sewa.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')
