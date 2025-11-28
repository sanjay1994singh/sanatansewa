from django.shortcuts import render

from sewa.models import SevaActivity


# Create your views here.
def homepage(request):
    seva = SevaActivity.objects.all()
    context = {
        'seva': seva
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def sewa(request):
    return render(request, 'sewa.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')
