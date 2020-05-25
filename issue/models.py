import datetime
from django.db import models
from django.utils import timezone



class Issue(models.Model):
    #issue = models.ForeignKey(Issue, on_delete = models.CASCADE)
    issue_title = models.CharField('Issue', max_length=100)
    issue_description = models.TextField('Description')
    pub_date = models.DateTimeField('Data')

    def __str__(self):
        return self.issue_title

    def published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=30))

    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'

    # only ONE commentator and author


class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete = models.CASCADE)
    author_name = models.CharField('author name', max_length=50)
    comment_text = models.TextField('comment')
    # img
    # file

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'



