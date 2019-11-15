from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
import time

from .forms import PostForm, CommentForm, UserForm
from .models import Post, Comment
from django.db.models import Q
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_list.html', stuff_for_frontend)

def search(request):
    request.start_time = time.time()
    duration = time.time() - request.start_time
    print(request.start_time)
    print(time.time())
    print(duration)
    user_query = str(request.GET.get('query', ''))
    search_result = Post.objects.filter(title__contains=user_query).order_by('-published_date')
    print(search_result)
    if search_result.count() == 0:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        stuff_for_frontend = {'posts': posts}
        messages.warning(request, 'Results containing ' + user_query + ' Not found, Sorry!')
        return render(request, 'blog/post_list.html', stuff_for_frontend)

    else:
        stuff_for_frontend = {'search_result': search_result}
        post_found = str(search_result.count())
        messages.success(request, 'About '+post_found+' results ')
        return render(request, 'blog/post_list.html', stuff_for_frontend)




def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blog/post_detail.html', stuff_for_frontend)



@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.info(request, 'Posted as Draft. Now Publish for Everyone to see')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # updating an existing form
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form, 'post': post}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)

@login_required
def post_draft_list(request):
    post = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'posts': post }
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    messages.success(request, 'Post Published Successfully. Everyone can see')
    return redirect('post_detail', pk=pk)

@login_required
def post_delete(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, 'Post was Deleted Successfully')
    return redirect('/', pk=post.pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

        return render(request, 'blog/add_comment_to_post.html', {'form':form, 'post': post})
@login_required
def comment_remove(request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        messages.success(request, 'Comment was Deleted Successfully')
        return  redirect('post_detail', pk=comment.post.pk)
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    messages.success(request, 'You Approved the Comment Successfully')
    return redirect('post_detail', pk=comment.post.pk)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            messages.success(request, 'Welcome ' + new_user.username +' Your account ha been Created Successfully.')
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'blog/signup.html', {'form': form})

