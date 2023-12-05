
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import User,Post
from .form import UserForm,PostForm
def home(request):
    return render(request, 'social_app/homepage.html')

def user_list(request):
    users = User.objects.all()
    return render(request,'social_app/user_list.html',{'users':users})

def user_details(request,username):
    user = get_object_or_404(User,username=username)
    return render(request,'social_app/user_detail.html',{'user':user})

def post_list(request):
    posts = Post.objects.all()
    return render(request,'social_app/post_list.html',{'posts':posts})

def post_detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'social_app/post_detail.html', {'post': post})
    
def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user)
    return render(request, 'social_app/user_posts.html', {'user': user, 'posts': posts})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            User.objects.create(
                username = data['username'],
                email = data['email'],
                bio = data['bio'],
                age = data['age'])
            return redirect('user_list')#succes url
        
        
    else :
        form = UserForm()        
    return render(request,'social_app/user_form.html',{'form':form})

def create_post(request,username):
    user = get_object_or_404(User,username=username)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                user = user,
                post = data['post'],
                visibility = data['visibility']
                )
            return redirect('user_posts',username=username)# success url
    else :
        form = PostForm()
    return render(request,'social_app/post_form.html',{'form':form})

def update_user(request,username):
    user = get_object_or_404(User,username=username)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username', user.username)
            user.email = form.cleaned_data.get('email', user.email)
            user.bio = form.cleaned_data.get('bio', user.bio)
            user.age = form.cleaned_data.get('age', user.age)
            
            # Save the updated user
            user.save()
        return redirect('user_detail',username=user.username)
    
    else:
        form = UserForm(initial={
            'username': user.username,
            'email': user.email,
            'bio': user.bio,
            'age': user.age,
        })
    return render(request, 'social_app/user_form.html', {'form': form, 'user': user})


       

 
            
    