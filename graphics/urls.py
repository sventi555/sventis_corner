from django.urls import path
from graphics import views


app_name = 'graphics'

urlpatterns = [
    path('', views.list_graphics, name='list_graphics'),
    path('<str:title>/', views.graphic_detail, name='graphic_detail'),
]
