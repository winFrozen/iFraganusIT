from django.urls import path
from .views import index, about, team, kids, courses, it

urlpatterns = [
    path('index/', index, name='index'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('courses/', courses, name='courses'),
    path('it/', it, name='it'),
    path('kids/', kids, name='kids')



]