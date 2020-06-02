from django.urls import path
from issue import views
from account.urls import urlpatterns




urlpatterns = [
    path('', views.index, name = 'index'),
    path('create_issue/', views.create_issue, name='create_issue'),
    path('<int:id>/', views.detail, name = 'detail'),
    path('<int:id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
    path('new_issues/', views.index, name = 'new_issues'),
    path('new_issues/search/', views.search, name='search'),
    ]

