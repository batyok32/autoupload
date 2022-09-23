import json
from .models import Queue
from django.shortcuts import get_object_or_404, redirect, render
import os
import subprocess

from .tasks import delete_file, upload_file

directory = "/home/batyr/Загрузки/"


# REMOTE WORK
def get_remote_link(request, path):
    some_command = f"rclone link '{path}'"
    p3 = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    print("Subprocess created")
    (output, err) = p3.communicate()
    if p3.wait() != 0:
        print("There was an error")
        return
    return render(
        request,
        "main/remote_list.html",
        context={"queryset": output.decode("utf-8"), "remote": path},
    )


def list_remotes(request, path=None):
    if path:
        # if request.method == "POST":
        # body_unicode = request.body.decode("utf-8")
        # body = json.loads(body_unicode)
        # path = body["path"]

        # TREE
        some_command = f"rclone tree '{path}'"
        p3 = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
        print("Subprocess created")
        (output1, err) = p3.communicate()
        if p3.wait() != 0:
            print("There was an error")
            return

        # SIZE
        some_command2 = f"rclone size '{path}'"
        p4 = subprocess.Popen(some_command2, stdout=subprocess.PIPE, shell=True)
        (output2, err) = p4.communicate()
        if p4.wait() != 0:
            print("There was an error")
            return

        # SUM OUTPUTS
        output = f"""
        {output1.decode("utf-8")}
        {output2.decode("utf-8")}
        """
        return render(
            request,
            "main/remote_list.html",
            context={"queryset": output, "remote": path},
        )
    return render(request, "main/remote_list.html")


def delete_remote(request, path):
    some_command = f"rclone delete '{path}'"
    p3 = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    print("Subprocess created")
    (output1, err) = p3.communicate()
    if p3.wait() != 0:
        print("There was an error")
        return
    get_only_folder = path.split("/")[0]
    return redirect(f"/remotes/list/{get_only_folder}/")


# QUEUES
def delete_queues(request, id):
    item = get_object_or_404(Queue, id=id)
    item.delete()
    return redirect("/queues/")


def list_queues(request):
    queryset = Queue.objects.all()
    context = {"queryset": queryset}
    return render(request, "main/queues.html", context)


# SERVER VIEWS
def upload(request, remote, path):
    result = upload_file.delay(remote, path, directory)
    print("Result", result)
    return redirect("/queues/")


def delete(request, path):
    result = delete_file.delay(path, directory)
    print("Result", result)
    return redirect("/")


def index(request):
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
