from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("queues/", views.list_queues, name="list"),
    path("upload/<str:path>/", views.upload, name="upload"),
]
