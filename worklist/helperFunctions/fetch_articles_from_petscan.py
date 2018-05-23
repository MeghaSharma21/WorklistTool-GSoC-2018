import requests
import json
import logging

logger = logging.getLogger('django')


# Function to fetch articles from
# Petscan by taking a petscan ID as input
def fetch_articles_from_petscan(psid):
    message = 'Successfully fetched articles from petscan ' \
              'using ID: {0}'.format(str(psid))
    success = True
    data = {}
    parameters = {'format': 'json', 'psid': psid}
    url = "https://petscan.wmflabs.org"
    response_object = requests.get(url, params=parameters)
    if response_object.status_code == 200:
        # Loading the response data into a dict variable
        json_data = json.loads(response_object.text)
        data = json_data['*'][0]['a']['*']
        if 'error' in json_data:
            success = False
            message = 'Execution Failed at getting petscanquery ' \
                      'articles, Error: {0}'\
                .format(str(json_data['error']['info']))
    else:
        # If response code is not ok
        success = False
        message = 'Execution Failed at getting petscan query articles,' \
                  ' HTTP Response Code: {0}'\
            .format(str(response_object.status_code))

    logger.info(message)
    return {"success": success, "message": message, "articles": data}
