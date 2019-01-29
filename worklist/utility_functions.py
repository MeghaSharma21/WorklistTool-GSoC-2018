from worklist.constants import OPEN_STATUS, CLAIMED_STATUS, ARTICLE_STATUS_TO_NUMBER_MAPPING


# Determines whether logged-in user can modify the status of the task or not
def can_modify_task_status(task_status, task_claimed_by, task_created_by, username):
    if username and (task_status == ARTICLE_STATUS_TO_NUMBER_MAPPING[OPEN_STATUS] or
                     (task_status == ARTICLE_STATUS_TO_NUMBER_MAPPING[CLAIMED_STATUS]
                      and task_claimed_by == username)) or task_created_by == username:
        return 1

    return 0


# Determines whether logged-in user can modify the progress of the task or not
def can_modify_task_progress(task_status, task_claimed_by, task_created_by, username):
    if username and (task_status == ARTICLE_STATUS_TO_NUMBER_MAPPING[CLAIMED_STATUS]
                     and task_claimed_by == username) or task_created_by == username:
        return 1

    return 0
