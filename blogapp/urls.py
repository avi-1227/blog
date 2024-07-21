from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/<slug:post>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/', views.post_share, name='post_share'),
    path('post/<int:post_id>/comment', views.post_comment, name='post_comment'),
]