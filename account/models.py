from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

# class Issue(models.Model):
#     issue = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
#     issue_title = models.CharField('Issue', max_length=100)
#     issue_description = models.TextField('Description')
#     pub_date = models.DateTimeField('Data')

#     def __str__(self):
#         return self.issue_title

#     def published_recently(self):
#         return self.pub_date >= (timezone.now() - datetime.timedelta(days=30))

#     class Meta:
#         verbose_name = 'Issue'
#         verbose_name_plural = 'Issues'

#     # only ONE commentator and author



# class Post(models.Model):
#     STATUS_CHOICES = (
#         ('draft', 'Draft'),
#         ('published', 'Published'),
#     )
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250, unique_for_date='publish')
#     author = models.ForeignKey(User, related_name='blog_posts')
#     body = models.TextField()
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

#     class Meta:
#         ordering = ('-publish',)

#     def __str__(self):
#         return self.title


# class Comment(models.Model):
#     issue = models.ForeignKey(Issue, on_delete = models.CASCADE)
#     author_name = models.CharField('author name', max_length=50)
#     comment_text = models.TextField('comment')
#     image = models.ImageField(upload_to='img')
#     created_at = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.author_name

#     class Meta:
#         verbose_name = 'Comment'
#         verbose_name_plural = 'Comments'