from worklist.constants import SEARCH_BY_NAME_FOR_WORKLISTS, SEARCH_BY_USERNAME_FOR_WORKLISTS, \
    ARTICLE_NUMBER_TO_STATUS_MAPPING
from worklist.models import WorkList, Task


# Helper function for searching worklists
def search_worklist_helper(search_term, search_type):
    worklists = []
    if search_type == '':
        # Default type for search
        search_type = SEARCH_BY_NAME_FOR_WORKLISTS

    if search_term == '':
        # Output all results in case search term is empty
        results = WorkList.objects.all()
    else:
        # In either types the pattern is searched instead of complete names
        if search_type == SEARCH_BY_NAME_FOR_WORKLISTS:
            results = WorkList.objects.filter(name__icontains=search_term)
        elif search_type == SEARCH_BY_USERNAME_FOR_WORKLISTS:
            results = WorkList.objects.filter(created_by__icontains=search_term)

    for result in results:
        worklist = {
            'name': result.name,
            'tags': result.tags,
            'description': result.description,
            'created_by': result.created_by,
            'psid': result.psid,
        }

        worklists.append(worklist)

    return worklists


# Helper function for searching tasks
def search_task_helper(search_term, worklist_name, worklist_created_by):
    tasks = []

    if search_term == '':
        # Output all tasks of that worklist in case search term is empty
        results = Task.objects.filter(worklist__name=worklist_name,
                                      worklist__created_by=worklist_created_by)
    else:
        # Here the pattern is searched instead of complete names
        results = Task.objects.filter(worklist__name=worklist_name,
                                      worklist__created_by=worklist_created_by,
                                      article__name__icontains=search_term)

    for result in results:
        task = {
            'article_name': result.article.name,
            'description': result.description,
            'created_by': result.created_by,
            'status': ARTICLE_NUMBER_TO_STATUS_MAPPING[result.status],
            'progress': result.progress,
            'effort': result.effort,
            'claimed_by': result.claimed_by
        }

        tasks.append(task)

    return tasks

