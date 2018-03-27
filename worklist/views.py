# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from worklist.models import WorkList


# View to create a worklist
def create_worklist(request):
    content = {}
    if request.method == 'POST':
        content = {'error': 0, 'message': 'Successfully saved worklist'}
        data = {'name': request.POST.get('name', ''),
                'theme': request.POST.get('theme', ''),
                'description': request.POST.get('description', ''),
                'created_by': request.POST.get('created_by', ''),
                'psid': request.POST.get('psid', ''),
                'psid_added_by': request.POST.get('created_by', '')}

        if data['name'] and WorkList.objects.filter(name=data['name']).exists():
            content['error'] = 1
            content['message'] = 'Worklist with this name already exists'
            render(request, 'worklist-page.html', content)
        WorkList.create_object(data)
    return render(request, 'create-worklist.html', {'content':content})


def show_worklist(request):
    searchTerm = request.GET.get('searchTerm','')
    worklists = [] 
    if searchTerm == '':
        results = WorkList.objects.all()
    else:
        results = WorkList.objects.filter(name=searchTerm)
    for result in results:
        worklist = {
            'name': result.name,
            'theme': result.theme,
            'description': result.description,
            'created_by': result.created_by,
            'psid': result.psid,
            'psid_added_by': result.psid_added_by
        }
        worklists.append(worklist)

    return render(request, 'show-worklist.html', {'results': worklists})
