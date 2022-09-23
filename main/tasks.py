from celery import shared_task
import os
import subprocess
from .models import Queue

# from celery.signals import task_prerun, task_success
# directory_path = "/home/batyr/Загрузки/"


@shared_task
def upload_file(remote, path, directory_path):
    """
    Task to upload to remote backend
    """
    direcory = f"{remote}:downloads"
    full_path = os.path.join(directory_path, path)
    print("FULL PATH", full_path)
    some_command = f"rclone copy '{full_path}' {direcory}"
    q = Queue.objects.create(path=full_path, status="Uploading")
    print("Created queue")
    p3 = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    print("Subprocess created")
    (output, err) = p3.communicate()
    if p3.wait() != 0:
        q.status = "Error"
        q.save()
        print("There was an error")
        return
    q.status = "Finished"
    q.save()
    # os.remove(full_path)
    print("OUTPUT", output)
    print("all processed finished")


@shared_task
def delete_file(path, directory_path):
    """
    Task to delete
    """
    full_path = os.path.join(directory_path, path)
    print("FULL PATH", full_path)
    some_command = f"rm -rf '{full_path}'"
    p3 = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    print("Subprocess created")
    (output, err) = p3.communicate()
    if p3.wait() != 0:
        print("There was an error")
        return
    print("OUTPUT", output)
    print("all processed finished")
