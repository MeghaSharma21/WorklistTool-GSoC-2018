import requests
import json
from django.http import JsonResponse
from django.shortcuts import render

def getPetScanQueryArticles(request):
        message = ''
        result = True
        data = {}
        psid = request.GET['psid']
        parameters = {'format':'json','psid':psid}
        url = "https://petscan.wmflabs.org"
        response_object = requests.get(url, params=parameters)
        if response_object.status_code == 200:
                # Loading the response data into a dict variable
                json_data = json.loads(response_object.text)
                data = json_data['*'][0]['a']['*']
                if 'error' in json_data:
                        result = False
                        message = 'Execution Failed at getting petscan' + \
                        'query articles, Error: ' + str(json_data['error']['info'])
        else:
                # If response code is not ok
                result = False
                message = 'Execution Failed at getting petscan ' + \
                'query articles, HTTP Response Code: ' + str(response_object.status_code)
        return JsonResponse({"result": result, "message": message, "articles": data})

def home(request):
        return render(request, 'index.html',{})
