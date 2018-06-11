import requests
import logging
from worklist.constants import TIMEOUT_IN_SECONDS

logger = logging.getLogger('django')


# Function to fetch articles from
# Petscan by taking a petscan ID as input
def fetch_articles_from_petscan(psid):
    message = 'Successfully fetched articles from petscan ' \
              'using ID: {0}'.format(psid)
    articles = []
    parameters = {'format': 'json', 'psid': psid}
    url = "https://petscan.wmflabs.org"
    try:
        response = requests.get(url, params=parameters, timeout=TIMEOUT_IN_SECONDS).json()
    except Exception as e:
        logger.info('Failed to query PetScan: {0} {1}'.format(type(e), e))
        return articles

    if 'error' in response:
        message = 'Execution Failed at getting petscanquery ' \
                  'articles, Error: {0}' \
            .format(response['error']['info'])
    else:
        articles = response['*'][0]['a']['*']

    logger.info(message)
    return articles
