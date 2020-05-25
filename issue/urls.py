from django.urls import path
from . import views

app_name = 'issue'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:issue_id>/', views.detail, name = 'detail '),
    path('<int:issue_id>/leave_comment/', views.leave_comment, name = 'leave_comment '),

]
