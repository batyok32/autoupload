from .models import Queue
from django.http import HttpResponse
from django.shortcuts import redirect, render
import os

from .tasks import upload_file


# Create your views here.
def index(request):
    directory = "/home/batyr/Загрузки/"
    file_list = os.listdir(directory)
    result_list = []
    for f in file_list:
        ext = f.split(".")
        if len(ext) >= 2:
            result_list.append({"name": f, "ext": ext[-1]})
        else:
            result_list.append({"name": f, "ext": "folder"})
    context = {"directory": directory, "files": result_list}
    return render(request, "main/index.html", context)


def list_queues(request):
    queryset = Queue.objects.all()
    context = {"queryset": queryset}
    return render(request, "main/queues.html", context)


def upload(request, path):
    result = upload_file.delay(path)
    print("Result", result)
    return redirect("/queues/")
