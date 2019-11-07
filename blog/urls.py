from django.urls import path
from . import views

urlpatterns = [

    # 127.0.0.1:8000 ==> local
    # mydjangoblog.com ==> online
    path('', views.post_list, name='post_list'),

    # 127.0.0.1:8000/post/3 ==> local
    # mydjangoblog.com/post/3 ==> online
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 127.0.0.1:8000/post/new ==> local
    # mydjangoblog.com/post/new ==> online
    path('post/new/', views.post_new, name='post_new'),

    # 127.0.0.1:8000/post/3/edit ==> local
    # mydjangoblog.com/post/3/edit ==> online
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
