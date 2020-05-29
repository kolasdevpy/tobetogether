from django import forms
from .models import Issue, Comment

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_title', 'issue_description']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'image']