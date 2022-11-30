from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm
from .models import Story
from likes.models import Like
from django.http import JsonResponse
def home(request):
    stories = Story.objects.all().order_by("-id")

    return render(request, "index.html", {"stories":stories})

@login_required
def add_story(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            anonymus =  request.POST.get("anonymus", False)
            print("wjat", anonymus)
            if anonymus:
                print("anon", anonymus)
                post.anonymus = True
            post.save()

            return redirect(reverse("dashboard", args=(request.user.id,)))
        else:
            print(form.errors)
    else:
        form = AddPostForm()

    return render(request, "stories/add-story.html", {"form":form})


@login_required
def like_story(request, pk):
    story = Story.objects.get(id=pk)
    like = Like.objects.filter(story=story, user=request.user).first()

    if not like:
        like = Like.objects.create(story=story, user=request.user)

    # check if like is in list of likes for post
    if like in story.likes.all():
        story.likes.remove(like)
    else:
        story.likes.add(like)
    
    return JsonResponse({"likes":story.likes.all().count()})