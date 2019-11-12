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

    # 127.0.0.1:8000/drafts ==> local
    # mydjangoblog.com/drafts ==> online
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    # 127.0.0.1:8000/post/3/publish ==> local
    # mydjangoblog.com/post/3/publish ==> online
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),

    # 127.0.0.1:8000/post/3/comment ==> local
    # mydjangoblog.com/post/3/comment ==> online
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]





