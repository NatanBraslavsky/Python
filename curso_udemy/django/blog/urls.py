from blog import views
from django.urls import path

urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo)
]