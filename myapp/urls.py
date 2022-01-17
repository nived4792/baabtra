from .import views
from django.urls import path


urlpatterns=[
    path ('home',views.home),

    path ('demo',views.demo)
]