from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm
from .models import Story


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