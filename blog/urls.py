from django.urls import path
from . import views

urlpatterns = [

    # 127.0.0.1:8000 ==> local
    # mydjangoblog.com ==> online
    path('', views.post_list, name='post_list'),

    # 127.0.0.1:8000/post/3 ==> local
    # mydjangoblog.com/post/3 ==> online
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]