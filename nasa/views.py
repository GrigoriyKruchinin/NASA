from django.shortcuts import render
from nasa.slider.models import Slide


def home(request):
    slides = Slide.objects.all()
    context = {'slides': slides}
    return render(request, "main.html", context)
