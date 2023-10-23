import requests
from django.urls import reverse
from django.shortcuts import render, redirect
from main.forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from .models import Post
from django.db.utils import IntegrityError
from django.contrib import messages



# @login_required(login_url="/login")
def home(request):

    api_key = '444a9fd7acc2dbc7312b699f7ef2f493'

    # Joensuu, Finland's latitude and longitude
    lat = 62.6017
    lon = 29.7636

    # Make a request to the OpenWeatherMap API
    weather_response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    )
    
    # Check if the request was successful
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
    else:
        temperature = 'N/A'
        weather_description = 'N/A'
    chatbot_url = reverse('chat') 
      # Check if the user is authenticated
    if request.user.is_authenticated:
        # If the user is logged in, fetch and display posts
        posts = Post.objects.all()
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass 
    return render(request, 'main/home.html', {"posts": posts,"chatbot_url": chatbot_url, "temperature": temperature, "weather_description": weather_description})


@login_required(login_url="/login")
@permission_required("main.add_post", login_url="/login", raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
           
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           human = True
           try: 
            user = form.save()
            login(request, user)
            return redirect('/home')
           except IntegrityError: # Virheilmoitus jos käyttäjänimi on jo varattu
               messages.error(request,'username or password not correct')
        else:
            messages.error(request, 'Form is not valid. Please check your input.')
            return render(request, 'registration/sign_up.html', {"form": form})                 
    else:
        form = RegisterForm()
        return render(request, 'registration/sign_up.html', {"form": form})



