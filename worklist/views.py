# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import JsonResponse
from django.shortcuts import render
import logging
from worklist.constants import SEARCH_BY_NAME_FOR_WORKLISTS, \
    SEARCH_BY_USERNAME_FOR_WORKLISTS
from worklist.views_helper_functions.store_articles import \
    store_added_articles, store_psid_articles
from worklist.models import WorkList, Task

logger = logging.getLogger('django')


# View to create a worklist
def create_worklist(request):
    content = {'error': 0, 'message': ''}
    if request.method == 'POST':
        content = {'error': 0, 'message': 'Successfully saved worklist'}
        data = {'name': request.POST.get('name', None),
                'tags': request.POST.get('tags', ''),
                'description': request.POST.get('description', ''),
                'created_by': request.POST.get('created_by', None),
                'psid': request.POST.get('psid', 0),  # As database stores blank integer
                                                      # field as zero
                'articles': json.loads(request.POST.get('articles', "[]"))
                }

        if data['name'] is None:
            content['error'] = 1
            content['message'] = 'Name of worklist can not be blank'
        elif data['created_by'] is None:
            content['error'] = 1
            content['message'] = 'Please login to create a worklist'
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

        return JsonResponse(content)
    logger.info('Message:' + str(content['message']))
    return render(request, 'create-worklist.html', {'content': content})


# View to search a worklist by it's name or by user who created the worklist
def search_worklist(request):
    search_term = request.GET.get('search_term', '')
    search_type = request.GET.get('search_type', '')

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

    return render(request, 'show-worklist.html', {'results': worklists})


# View to search a task by it's name
def search_task(request):
    search_term = request.GET.get('search_term', '')
    worklist_name = request.GET.get('worklist_name', '')
    worklist_created_by = request.GET.get('created_by', '')
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
            'status': result.status,
            'progress': result.progress,
            'effort': result.effort,
            'claimed_by': result.claimed_by
        }

        tasks.append(task)

    return render(request, 'show-task.html', {'tasks': tasks,
                                              'worklist_name': worklist_name,
                                              'worklist_created_by': worklist_created_by})
