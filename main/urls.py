from django.urls import path

from . import views

urlpatterns = [
    # Working with remote
    path("remotes/delete/<str:path>/", views.delete_remote, name="delete_remotes_path"),
    path(
        "remotes/link/<str:path>/", views.get_remote_link, name="get_link_remotes_path"
    ),
    path("remotes/list/<str:path>/", views.list_remotes, name="list_remotes_path"),
    path("remotes/list/", views.list_remotes, name="list_remotes"),
    # QUEUES
    path("queues/delete/<int:id>/", views.delete_queues, name="delete_queues"),
    path("queues/", views.list_queues, name="list"),
    # Upload/Delete on server
    path("upload/<str:remote>/<str:path>/", views.upload, name="upload"),
    path("delete/<str:path>/", views.delete, name="delete"),
    path("", views.index, name="index"),
]
