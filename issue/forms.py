from django import forms
from .models import Issue, Comment

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_title', 'issue_description']
        widgets = {
            'issue_title': forms.Textarea(attrs={'rows':1, 'cols':50}),
            'issue_description': forms.Textarea(attrs={'rows':3}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'rows':3}),
        }

