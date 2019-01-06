from worklist.constants import OPEN_STATUS, CLAIMED_STATUS


# Determines whether logged-in user can modify the status of the task or not
def can_modify_task_status(task_status, task_claimed_by, username):
    if username and (task_status == OPEN_STATUS or (task_status == CLAIMED_STATUS and
                                                    task_claimed_by == username)):
        return True

    return False


# Determines whether logged-in user can modify the progress of the task or not
def can_modify_task_progress(task_status, task_claimed_by, username):
    if username and (task_status == CLAIMED_STATUS and task_claimed_by == username):
        return True

    return False
