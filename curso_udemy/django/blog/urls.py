from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]