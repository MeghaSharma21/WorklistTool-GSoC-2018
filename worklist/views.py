import functools
import json
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
import logging
from worklist.constants import ARTICLE_STATUS_TO_NUMBER_MAPPING
from worklist.views_helper_functions.search_helpers import search_worklist_helper, search_task_helper
from worklist.views_helper_functions.store_articles import \
    store_added_articles, store_psid_articles
from worklist.models import WorkList, Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

logger = logging.getLogger('django')


# View related to OAuth using MediaWiki
def mediawiki_login(request):
    return HttpResponseRedirect(
        'https://tools.wmflabs.org/worklist-tool/oauth/login/mediawiki/')


# View for logging out from the app
@login_required
def app_logout(request):
    logout(request)

    # if user has logged out of the app, take him to home page
    return render(request, 'homepage.html',
                  {'message': '',
                   'error': False,
                   'logged_in_user': None,
                   })


def with_logged_in_user(view):
    @functools.wraps(view)
    def inner_method(request):
        user_or_none = None

        if request.user.is_authenticated:
            user_or_none = request.user.username

        return view(request, user_or_none)

    return inner_method


# View corresponding to homepage of the app
@with_logged_in_user
def homepage(request, username):
    message = ''
    error = False

    return render(request, 'homepage.html',
                  {'logged_in_user': username, 'message': message,
                   'error': error,
                   })


# View to create a worklist
@login_required
def create_worklist(request):
    username = request.user.username
    content = {'error': 0, 'message': ''}
    if request.method == 'POST':
        content = {'error': 0, 'message': 'Successfully saved worklist'}
        data = {'name': request.POST.get('name', None),
                'tags': request.POST.get('tags', ''),
                'description': request.POST.get('description', ''),
                'created_by': username,
                'psid': request.POST.get('psid', 0),  # As database stores blank integer
                                                      # field as zero
                'articles': json.loads(request.POST.get('articles', "[]"))
                }
        content['created_by'] = data['created_by']
        content['name'] = data['name']

        if data['name'] is None or data['name'] == '':
            content['error'] = 1
            content['message'] = 'Name of worklist can not be blank'
        elif WorkList.objects.filter(name=data['name'],
                                     created_by=data['created_by']).exists():
            content['error'] = 1
            content['message'] = 'Worklist with this name already exists'

        if content['error'] != 1:
            if data['psid'] == '':
                data['psid'] = 0

            # Saving data in Worklist, Task and Article tables
            worklist_object = WorkList.create_object(data)

            if data['articles']:
                success = \
                    store_added_articles(worklist_object, data['articles'])
                if success is False:
                    content['error'] = 1
                    content['message'] = 'Added articles could not be saved.'

            if data['psid'] != 0:
                success = store_psid_articles(worklist_object,
                                              data['psid'], data['created_by'])
                if success is False:
                    content['error'] = 1
                    content['message'] = 'Petscan articles could not be saved.'

        if content['error'] == 1:
            WorkList.objects.filter(name=data['name'],
                                    created_by=data['created_by']).delete()

        return JsonResponse(content)
    logger.info('Message:' + str(content['message']))
    return render(request, 'create-worklist.html', {'content': content,
                                                    'logged_in_user': username})


# View to add articles to a worklist
@login_required
def add_articles_to_worklist(request):
    username = request.user.username
    content = {'error': 0, 'message': ''}
    if request.method == 'POST':
        content = {'error': 0, 'message': 'Successfully added article to the worklist'}
        article = [{'name': request.POST.get('article_name', None),
                    'description': request.POST.get('article_description', ''),
                    'effort': request.POST.get('article_effort', ''),
                    'created_by': username
                    }]

        worklist_name = request.POST.get('worklist_name', None)
        worklist_created_by = request.POST.get('worklist_created_by', None)

        if article[0]['name'] is None:
            content['error'] = 1
            content['message'] = 'Article name can not be empty'

        if Task.objects.filter(worklist__name=worklist_name,
                               worklist__created_by=worklist_created_by,
                               article__name=article[0]['name']).exists():
            content['error'] = 1
            content['message'] = 'Article with this name already exists in the worklist'

        if content['error'] != 1:
            worklist_object = WorkList.objects.get(name=worklist_name, created_by=worklist_created_by)

            success = \
                store_added_articles(worklist_object, article)
            if success is False:
                content['error'] = 1
                content['message'] = 'Added article could not be saved.'

    logger.info('Message:' + str(content['message']))
    return JsonResponse({'error': content['error'], 'message': content['message']})


# View to search a worklist by it's name or by user who created the worklist
@with_logged_in_user
def search_worklist(request, username):
    search_term = request.GET.get('search_term', '')
    search_type = request.GET.get('search_type', '')

    worklists = search_worklist_helper(search_term, search_type)

    return render(request, 'show-worklist.html', {'results': worklists, 'logged_in_user': username})


# View to update the table displaying all worklists
def update_worklist_table(request):
    search_term = request.GET.get('search_term', '')
    search_type = request.GET.get('search_type', '')

    worklists = search_worklist_helper(search_term, search_type)
    return render(request, 'show-worklist-table.html', {'results': worklists})


# View to search a task by it's name
@with_logged_in_user
def search_task(request, username):
    search_term = request.GET.get('search_term', '')
    worklist_name = request.GET.get('worklist_name', '')
    worklist_created_by = request.GET.get('worklist_created_by', '')

    tasks = search_task_helper(search_term, worklist_name, worklist_created_by)

    return render(request, 'show-task.html', {'tasks': tasks,
                                              'worklist_name': worklist_name,
                                              'worklist_created_by': worklist_created_by,
                                              'logged_in_user': username})


# View to update the table displaying all tasks of a worklist
def update_task_table(request):
    search_term = request.GET.get('search_term', '')
    worklist_name = request.GET.get('worklist_name', '')
    worklist_created_by = request.GET.get('worklist_created_by', '')

    tasks = search_task_helper(search_term, worklist_name, worklist_created_by)
    return render(request, 'show-task-table.html', {'tasks': tasks})


# Update task information when user edits it
@login_required
def update_task_info(request):
    username = request.user.username
    worklist_name = request.POST.get('worklist_name', '')
    worklist_created_by = request.POST.get('worklist_created_by', '')
    article_name = request.POST.get('article_name', '')
    status = request.POST.get('status', '')
    progress = request.POST.get('progress', '')
    claimed_by = ''

    if status == 'claimed':
        claimed_by = username
    status_code = ARTICLE_STATUS_TO_NUMBER_MAPPING[status]

    results = Task.objects.filter(worklist__name=worklist_name,
                                  worklist__created_by=worklist_created_by,
                                  article__name=article_name)

    results.update(progress=progress, status=status_code, claimed_by=claimed_by)

    return JsonResponse({'success': True})


# View to display worklists created or being worked upon by the logged-in user
@login_required
def show_user_worklists(request):
    username = request.user.username

    def worklist_to_dict(worklist):
        return {'name': worklist.name, 'tags': worklist.tags,
                'description': worklist.description, 'psid': worklist.psid,
                'created_by': worklist.created_by}

    created_worklists = \
        map(worklist_to_dict, WorkList.objects.filter(created_by=username))
    worked_upon_worklists = \
        map(worklist_to_dict, [r.worklist for r in Task.objects.filter(claimed_by=username)])

    return render(request, 'user-worklists.html', {'logged_in_user': username,
                                                   'created_worklists': list(created_worklists),
                                                   'worked_upon_worklists': list(worked_upon_worklists)})
