import requests
import logging

logger = logging.getLogger('django')


# Function to fetch articles from
# Petscan by taking a petscan ID as input
def fetch_articles_from_petscan(psid):
    message = 'Successfully fetched articles from petscan ' \
              'using ID: {0}'.format(psid)
    success = True

    parameters = {'format': 'json', 'psid': psid}
    url = "https://petscan.wmflabs.org"
    try:
        response = requests.get(url, params=parameters).json()
    except Exception as e:
        logger.info('Failed to query PetScan: {0} {1}'.format(type(e), e))
        return False

    if 'error' in response:
        success = False
        message = 'Execution Failed at getting petscanquery ' \
                  'articles, Error: {0}' \
            .format(response['error']['info'])

    articles = response['*'][0]['a']['*']

    logger.info(message)
    return {"success": success, "message": message, "articles": articles}
