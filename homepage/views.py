from django.shortcuts import render

from sewa.models import SevaActivity

from gallery.models import Gallery

from member.models import Member


# Create your views here.
def homepage(request):
    seva = SevaActivity.objects.all()
    member = Member.objects.all()
    gallery = Gallery.objects.all()
    context = {
        'seva': seva,
        'member': member,
        'gallery': gallery,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def sewa(request):
    seva = SevaActivity.objects.all()
    context = {
        'seva': seva,
    }
    return render(request, 'sewa.html', context)


def gallery(request):
    gallery = Gallery.objects.all()
    context = {
        'gallery': gallery,
    }
    return render(request, 'gallery.html', context)


def contact(request):
    return render(request, 'contact.html')
