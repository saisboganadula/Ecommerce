from django.urls import path
from products import views

urlpatterns = [
    path("hello/", views.helloView),
    path("hello/<slug:username>", views.helloName),
]