from django.urls import path
from . import views

app_name = 'graphics'
urlpatterns = [
    path('', views.list_graphics, name='list_graphics'),
    path('<int:pk>', views.graphic_detail, name='graphic_detail'),
]