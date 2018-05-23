import math
import logging
from collections import defaultdict
import requests
import json

logger = logging.getLogger('django')


# Function to convert a comma separated
# string into list of strings
def convert_string_to_list(input_string):
    output_list = input_string.split(',')
    return output_list


# Function to convert a list of strings
# into a comma separated string
def convert_list_to_string(input_list):
    output_string = ','.join(input_list)
    return output_string


# General function to call MediaWiki API and fetch data from it
def fetch_data_from_mediawiki_api(parameters):
    message = ''
    result = True
    json_data = {}
    url = 'https://en.wikipedia.org/w/api.php'
    response_object = requests.get(url, params=parameters)
    if response_object.status_code == 200:
        # Loading the response data into a dict variable
        json_data = json.loads(response_object.text)
        if 'error' in json_data:
            result = False
            message = 'Execution Failed at MediaWiki web service API,' \
                      + 'Error:' + str(json_data['error']['info'])
    else:
        # If response code is not ok
        result = False
        message = 'Execution Failed at MediaWiki web service API,' \
                  + 'HTTP Response Code: ' \
                  + str(response_object.status_code)

    return {"result": result, "message": message, "json_data": json_data}


# Function that uses MediaWiki API that maps page titles to IDs
def convert_article_titles_into_ids(titles):
    page_title_to_id_mapping = defaultdict(int)
    page_ids_results = []
    message = 'Page titles successfully converted to IDs.'
    success = True
    for i in range(math.ceil(len(titles) / 50)):
        # Since at max 50 titles can be passed in one request
        titles_list = ' | '.join(str(page) for page in
                                 titles[i * 50:(i + 1) * 50])

        parameters = {'action': 'query',
                      'format': 'json',
                      'prop': 'info',
                      'formatversion': 2,
                      'titles': titles_list}
        while True:
            results = fetch_data_from_mediawiki_api(parameters)
            if not results['result']:
                message = 'Error occurred while fetching page ' \
                          'IDs for titles. Results:'
                success = False
                break

            json_data = results['json_data']
            page_ids_results = \
                page_ids_results + json_data['query']['pages']

            if 'continue' in json_data:
                parameters['incontinue'] = \
                    json_data['continue']['incontinue']
                parameters['continue'] = \
                    json_data['continue']['continue']
            else:
                break

    logger.info(message)

    if not success:
        return -1
    else:
        for result in page_ids_results:
            page_title_to_id_mapping[str(result.get('title'))] = \
                str(result.get('pageid'))

        return page_title_to_id_mapping
