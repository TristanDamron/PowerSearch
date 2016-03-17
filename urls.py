from django.conf.urls import url
from . import views

urlpatterns = [
    #Url for the home screen
    url(r'^home/', views.home, name="Home"),
    #Url for the search screen
    url(r'^search/', views.search, name="Search"),
]
