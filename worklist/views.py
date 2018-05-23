# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import logging
from worklist.constants import SEARCH_BY_NAME_FOR_WORKLISTS, SEARCH_BY_USERNAME_FOR_WORKLISTS
from worklist.helperFunctions.storeArticles import \
    store_added_articles_in_task_table, store_psid_articles_in_task_table
from worklist.models import WorkList

logger = logging.getLogger('django')


# View to create a worklist
def create_worklist(request):
    content = {'error': 1, 'message': 'Can save worklist only with POST request'}
    if request.method == 'POST':
        content = {'error': 0, 'message': 'Successfully saved worklist'}
        data = {'name': request.POST.get('name', None),
                'tags': request.POST.get('tags', ''),
                'description': request.POST.get('description', ''),
                'created_by': request.POST.get('created_by', None),
                'psid': request.POST.get('psid', 0),  # As database stores blank integer
                                                      # field as zero
                'articles': request.POST.get('articles', [])
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

        if content['error'] == 1:
            render(request, 'worklist-page.html', content)

        # Saving data in Worklist, Task and Article tables
        worklist_id = WorkList.create_object(data)

        function_error = \
            store_added_articles_in_task_table(worklist_id, data['articles'])
        if function_error is True:
            content['error'] = 1
            content['message'] = 'Added articles could not be saved.'

        function_error = store_psid_articles_in_task_table(worklist_id,
                                                           data['psid'], data['created_by'])
        if function_error is True:
            content['error'] = 1
            content['message'] = 'Petscan articles could not be saved.'

    logger.info('Message:' + str(content['message']))
    return render(request, 'create-worklist.html', {'content': content})


# View to search a worklist by username or by user who created the worklist
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
