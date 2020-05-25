from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Issue, Comment


def index(request):
    # print(Issue.__text_signature__)
    latest_issues_list = Issue.object.order_by('-pub_date')[:5]
    # latest_issues_list = Issue()
    # Entry.objects.order_by('blog__name', 'headline')

    return render(request, 'issue/list_issues.html', {'latest_issues_list': latest_issues_list})

def detail(request, issue_id):
    try:
        a = Issue.object.get(id=issue_id)
    except:
        raise Http404('Issue not found.')

    latest_comments = a.comment_set.order_by('-id')[:]

    return render(recuest, 'issue/detail.html', {'issue': a})

def leave_comment(request, issue_id):
    try:
        a = Issue.object.get(id=issue_id)
    except:
        raise Http404('Issue not found.')

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('issue:detail', args = (a.id)))


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