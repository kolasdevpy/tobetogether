from django.urls import path
from issue import views
from account.urls import urlpatterns

# app_name = 'issue'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create_issue/', views.create_issue, name='create_issue'),
    path('<int:issue_id>/', views.detail, name = 'detail '),
    path('<int:issue_id>/leave_comment/', views.leave_comment, name = 'leave_comment '),
    # create issue
]
