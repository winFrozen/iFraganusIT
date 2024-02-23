from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import context
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.generic import ListView
from blog.forms import KonsultatsiyaForms
from blog.models import Teachers, About, Aboutus, Course, Pupils, Teamtopbar, Pupils2, Pupils3, Pupils4, Pupils5, \
    Itcourse, Kids, Ittopbar, News


# from blog.forms import KonsultatsiyaForms
# from blog.models import Carusel

# Create your views here.

def index(request):
    form = KonsultatsiyaForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi !</h2>")

    teachers = Teachers.objects.all()
    about = About.objects.all()
    context = {
        "form": form,
        "teachers": teachers,
        "about": about
    }
    return render(request, "index.html", context=context)


def courses(request):
    course = Course.objects.all()
    teamtopbar = Teamtopbar.objects.all()

    context = {
        "course": course,
        "teamtopbar": teamtopbar,

    }
    return render(request, "courses.html", context=context)

def about(request):
    aboutus = Aboutus.objects.all()
    pupil = Pupils.objects.all()
    news = News.objects.all()
    context = {
        "aboutus": aboutus,
        "pupil": pupil,
        "news": news

    }
    return render(request, "about.html", context=context)

def team(request):
    teamtopbar = Teamtopbar.objects.all()
    pupil = Pupils.objects.all()
    pupils2 = Pupils2.objects.all()
    pupils3 = Pupils3.objects.all()
    pupils4 = Pupils4.objects.all()
    pupils5 = Pupils5.objects.all()

    context = {
        "teamtopbar": teamtopbar,
        "pupil": pupil,
        "pupils2": pupils2,
        "pupils3":pupils3,
        "pupils4":pupils4,
        "pupils5":pupils5

    }
    return render(request, "team.html", context=context)

def it(request):
    itcourse = Itcourse.objects.all()
    ittopbar = Ittopbar.objects.all()

    context = {
        "itcourse": itcourse,
        "ittopbar": ittopbar,

    }
    return render(request, "it.html", context=context)

def kids(request):
    kids = Kids.objects.all()
    teamtopbar = Teamtopbar.objects.all()

    context = {
        "kids": kids,
        "teamtopbar": teamtopbar,

    }
    return render(request, "kids.html", context=context)



