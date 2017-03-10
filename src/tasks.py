import re
import os
import hashlib
import time
from shemutils.logger import Logger
from telemanager.database import db, t3


logger = Logger("Tasks")


def generate_new_task_hash():
    """
    Generate a hash for the task
    """
    m = hashlib.sha256()
    m.update(os.urandom(256))
    return m.hexdigest()


def new_task_regex(message):
    """
    Regex to match the task creation request
    """
    regex = "^(criar?|nova?|new?|registrar?|register)\s(tarefa?|task)\s(\"?|')(?P<task>[a-zA-Z0-9\s\/]+)(\"?|')"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()

def list_task_regex(message):
    """
    Regex to match the task creation request
    """
    regex = "^(listar?|list)\s(tarefa(s)?|task(s))"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()

def delete_task_regex(message):
    """
    Regex to match the task creation request
    """
    regex = "^(deletar?|remover?|delete?|unregister?|del)\s(tarefa?|task)\s(\"?|')(?P<task>[a-zA-Z0-9\s\/]+)(\"?|')"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()

def create_new_task(username, chat_id, task):
    """
    Creates a task.
    """
    task_id = generate_new_task_hash()
    timestamp = str(time.time())

    if not db:
        logger.critical("Database is not defined.")
        return -1

    sql = t3.insert_data([username, str(chat_id), task_id, task, "OPEN", timestamp])
    db.controller.execute(sql)
    db.save()
    return 0


def delete_a_task(task_id):
    """
    Deletes a task.
    """
    if not db:
        logger.critical("Database is not defined.")

    sql = "DELETE FROM TASKS WHERE TASK_ID = '{0}'".format(task_id)
    db.controller.execute(sql)
    db.save()
    return 0


def list_all_tasks(chat_id):
    """
    Query for tasks of the same chat_id and returns a list of them
    If the result does not yield any result, returns -1.
    """
    sql = "SELECT * FROM TASKS WHERE CHAT_ID = '{0}'".format(chat_id)
    db.controller.execute(sql)
    result = db.controller.get()
    if len(result) == 0:
        return -1
    return result
