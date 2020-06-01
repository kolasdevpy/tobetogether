from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Issue, Comment
from .forms import IssueForm, CommentForm
from django.conf import settings
import random
import hashlib  #

from django.db.models import Q
from django.views.decorators.http import require_GET




@require_GET
def search(request):
    query = request.GET.get("q", "")
    search_issues = Issue.objects.filter(
        Q(issue_title__icontains=query) & Q(issue_private=False)
        ).order_by('-pub_date')[:]
    return render(request, 'search.html', context={'search_issues': search_issues})


def index(request):
    latest_issues_list = Issue.objects.filter(issue_private=False).order_by('pub_date')[:]
    return render(request, 'account/new_issues.html', {'latest_issues_list': latest_issues_list})


def detail(request, id):
    # if id == author, commentator --------------------------------------------
    try:
        a = Issue.objects.get(pk=id)
    except:
        raise Http404('Issue not found.')
    latest_comments = a.comment_set.order_by('-id')[:]
    return render(request, 'issue/detail.html', {'issue': a, 'form': CommentForm(), 'latest_comments': latest_comments})


def leave_comment(request, id):
    try:
        a = Issue.objects.get(pk=id)
    except:
        raise Http404('Issue not found.')
    form = CommentForm(request.POST)
    if form.is_valid():
        comment_text = form.cleaned_data['comment_text']
        a.comment_set.create(author_name=request.user.username, comment_text=comment_text, image=request.FILES.get('image'))
        a.issue_private = True
        # issue_new_id = Issue.objects.get(pk=id)
        # print(issue_new_id.pk)
        # new_id = random.randint(1, 1e6)
        # print(new_id)
        # a.pk = new_id
        a.save()
    return HttpResponseRedirect(reverse('detail', args=[a.id]))


@login_required
def create_issue(request):
    if request.method == 'GET':
        form = IssueForm()
        return render(request, 'create_issue.html', context={'form': form})
    elif request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = Issue()
            issue.create_issue_model(form.data['issue_title'],
                                    form.data['issue_description'],
                                    request.user)
            return redirect('/my_issues/')
        return render(request, 'create_issue.html', context={'form': form}) 



# Issue.object.filter(issue_title__startswith = "qwerty")


# import timezone
# for_the_last = timezone.now().month  # month
# Issue.object.filter(pub_date = for_the_last)


# Issue.object.get(id = 1)     # issue_title =

# issue.comment_set_all()      # show all comments
# issue.comment_set.count()    # quantity
# issue.comment_set.filter(author_name__startswith = "~name~")

# delete


# def all_issues(request):
#     return