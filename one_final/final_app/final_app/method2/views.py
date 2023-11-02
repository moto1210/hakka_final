from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from method2.forms import CommentForm
from .models import Post
from django import forms

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
    
    param = {
        'form': form
    }
    return render(request, 'method2/signup.htm', param)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect("toppage")
                #return render(request, 'method2/index.htm')
    else:
        form = LoginForm()
    param = {
        'title': 'ログイン',
        'form': form,
    }
    return render(request, 'method2/login.htm', param)

def logout_view(request):
    logout(request)
    return render(request, 'method2/logout.htm')

@login_required
def user_view(request):
    user = request.user
    params = {
        'user': user
    }
    return render(request, 'method2/user.htm', params)

@login_required
def other_view(request):
    users = User.objects.exclude(username=request.user.username)
    params = {
        'users': users
    }
    return render(request, 'method2/other.htm', params)

def toppage(request):
    return render(request, "method2/toppage.htm")

def index(request):
    posts = Post.objects.all()
    return render(request, "method2/index.htm",{"posts":posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=post.slug)
    else:
        form = CommentForm()
    return render(request, "method2/post_detail.htm", {"post":post, "form":form})


def sub2_view(request):
    return render(request, 'method2/sub2.htm')

def sub3_view(request):
    return render(request, 'method2/sub3.htm')

def sub4_view(request):
    return render(request, 'method2/sub4.htm')



def getCheckBox(request):
    check = request.POST.getlist('subject')
    print(check)



