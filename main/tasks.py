from celery import shared_task
import os
import subprocess
from .models import Queue

# from celery.signals import task_prerun, task_success


@shared_task
def upload_file(path):
    """
    Task to upload to remote backend
    """
    direcory = "gdrive:mail"
    directory_path = "/home/batyr/Загрузки/"
    full_path = directory_path + path
    some_command = f"rclone copy {full_path} {direcory}"
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
