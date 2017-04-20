import re
import os
import hashlib
import time
from shemutils.logger import Logger
from telemanager.database import db, t3
import unicodedata


logger = Logger("Tasks")



def remove_accents(input_str):
    """
    Receive a input_str (bytes or String) and returns a no-accent String
    """
    if type(input_str) is bytes:
        input_str = input_str.decode()
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    if type(only_ascii) is bytes:
        only_ascii = only_ascii.decode()
    return only_ascii


def generate_new_task_hash():
    """
    Generate a hash for the task
    """
    m = hashlib.md5()
    m.update(os.urandom(256))
    return m.hexdigest()


def new_task_regex(message):
    """
    Regex to match the task creation request
    """
    if type(message) is bytes:
        message = message.decode()
    regex = "^(criar?|nova?|new?|add)\s(tarefa?|task)\s(\"?|')(?P<task>[a-zA-Z0-9\s\/:\.\-ç]+)(\"?|')"
    m = re.match(regex, remove_accents(message).decode())
    if not m:
        return None
    else:
        return m.groupdict()

def list_task_regex(message):
    """
    Regex to match the task creation request
    """
    if type(message) is bytes:
        message = message.decode()
    regex = "^(listar?|list)\s(tarefa?(s)?|task?|tasks)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return True

def delete_task_regex(message):
    """
    Regex to match the task creation request
    """
    if type(message) is bytes:
        message = message.decode()
    regex = "^(deletar?|delete?|del?|concluir?|finish)\s+(task(s)?|tarefa?|tarefas)\s+('?|\")(?P<task_id>[0-9A-Za-z]+)('?|\")"
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

    sql = "UPDATE TASKS SET STATUS = 'CLOSED' WHERE TASK_ID = '{0}'".format(task_id)
    db.controller.execute(sql)
    db.save()
    return 0


def list_all_tasks(chat_id):
    """
    Query for tasks of the same chat_id and returns a list of them
    If the result does not yield any result, returns -1.
    """
    sql = "SELECT * FROM TASKS WHERE CHAT_ID = '{0}' AND STATUS = 'OPEN'".format(chat_id)
    db.controller.execute(sql)
    result = db.controller.get()
    if len(result) == 0:
        return -1
    return result


def present_tasks(task_list):
    """
    Given a task set, returns a string object presenting the data.
    """
    task_n = len(task_list)
    header = "Existem {0} tarefas que necessitam da sua atencao:\n\n".format(task_n)
    body = ""
    for task in task_list:
        # [(1, 'Dade Murphy', '193665372', 'f0287edaa341e5fb7eccfe7b6a43d9e3c2607cd60023877b10db9b004215264e', 'tarefa alex marino 13/03', 'OPEN', '1489168850.2677088')]
        task_id, user, chat_id, task_hash, task_text, status, timestamp = task
        body += "Task id: _{0}_\n*{1}*\n\n".format(task_hash, task_text)
    return header + body
