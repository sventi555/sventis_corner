from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('post<int:pk>', views.post_detail, name='post_detail'),
    path('talia', views.talia_page, name='talia_page')
]
