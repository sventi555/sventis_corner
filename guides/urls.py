from django.urls import path
from guides import views

app_name = 'guides'
urlpatterns = [
    path('', views.home, name="home"),
]