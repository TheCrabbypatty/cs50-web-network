from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.urls import reverse
import json


from .models import User, Post


def index(request):
    if request.method == "POST":
        content = request.POST["content"]
        Post.objects.create(poster=request.user, content=content)
        return redirect("index")
    posts = Post.objects.all().order_by("-timestamp")
    return render(request, "network/index.html", {
            "posts": posts
        })

@csrf_exempt
def edit(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        post = Post.objects.get(id=post_id)
        if request.user != post.poster:
            return JsonResponse({"error": "Not allowed"}, status=403)
        post.content = data["content"]
        post.save()
        return JsonResponse({"content": post.content})

@csrf_exempt
def like(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)

        return JsonResponse({"likes": post.likes.count()})

@csrf_exempt
def follow(request, username):
    profile_user = User.objects.get(username=username)
    user = request.user

    if user == profile_user:
        return JsonResponse({"error": "Cannot follow yourself"}, status=400)

    if user in profile_user.followers.all():
        profile_user.followers.remove(user)
        following = False
    else:
        profile_user.followers.add(user)
        following = True

    return JsonResponse({
        "followers": profile_user.followers.count(),
        "following": following
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(poster = user).order_by("-timestamp")
    is_following = request.user in user.followers.all()
    return render(request, "network/profile.html", {"profile_user": user, "posts": posts, "followers": user.followers.count(), "following": user.following.count(), "is_following": is_following})