import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings




class Issue(models.Model):
    issue = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    issue_title = models.CharField('Issue', max_length=50)
    issue_description = models.TextField('Description')
    pub_date = models.DateTimeField(default=timezone.now)
    issue_private = models.BooleanField(default=False)

    def __str__(self):
        return self.issue_title

    def published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=30))

    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'

    def create_issue_model(self, a,b,c):
        self.issue_title = a
        self.issue_description = b
        self.issue = c
        self.save()
        return


class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete = models.CASCADE)
    author_name = models.CharField('author name', max_length=50)
    comment_text = models.TextField('comment', max_length=500)
    image = models.ImageField(upload_to='media/img', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

