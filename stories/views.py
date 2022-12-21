from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm
from .models import Story, Report
from comments.models import Comment
from likes.models import Like
from django.http import JsonResponse
from adverts.models import Advert
from django.http import Http404


def home(request):
    stories = Story.objects.all().order_by("-id")
    ads= Advert.objects.all().order_by("-id")

    return render(request, "index.html", {"stories":stories, "ads":ads})

@login_required
def add_story(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            anonymus =  request.POST.get("anonymus", False)
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


@login_required
def report_story(request,pk):
    story = Story.objects.get(pk=pk)

    Report.objects.create(story=story, reporter=request.user)

    return JsonResponse("success", safe=False)


@login_required
def story_detail(request,pk):
    story = Story.objects.get(pk=pk)

    return render(request, "stories/story-detail.html", {"story":story})


@login_required
def add_comment(request,pk):
    try:
        story = Story.objects.get(id=pk)
        Comment.objects.create(comment=request.POST.get("comment"), user=request.user, story=story)

        return redirect('story_detail', pk=story.id)

    except Story.DoesNotExist:
        raise Http404


@login_required
def delete_comment(request,pk):
    try:
        comment = Comment.objects.get(id=pk)
        story_id = comment.story.id

        comment.delete()

        return redirect('story_detail', pk=story_id)

    except Comment.DoesNotExist:
        raise Http404