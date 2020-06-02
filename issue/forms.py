from django import forms
from .models import Issue, Comment
# from django.core.exceptions import ValidationError




# def validate_image(image):
#     file_size = image.file.size
#     limit_kb = 1
#     if file_size > limit_kb * 1024:
#         raise ValidationError(f"Max size of file is {limit} KB.")


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_title', 'issue_description']
        widgets = {
            'issue_title': forms.Textarea(attrs={'rows':1, 'cols':50, 'wrap': "soft", 'maxlength': 50}),
            'issue_description': forms.Textarea(attrs={
                'rows': 3, 'cols': 50, 'wrap': "soft", 'maxlength': 500}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'rows': 3, 'cols': 50, 'wrap': "soft", 'maxlength': 500}),
            # 'image' : forms.Filearea(attrs={'max_upload_size': 5242880})     validators=[validate_image]
            }

