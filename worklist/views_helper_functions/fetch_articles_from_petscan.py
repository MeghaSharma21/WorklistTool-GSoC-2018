import requests
import logging
from worklist.constants import TIMEOUT_FOR_PETSCAN, PETSCAN_URL

logger = logging.getLogger('django')


# Function to fetch articles from
# Petscan by taking a petscan ID as input
def fetch_articles_from_petscan(psid):
    message = 'Successfully fetched articles from petscan ' \
              'using ID: {0}'.format(psid)
    articles = []
    parameters = {'format': 'json', 'psid': psid}
    
    try:
        response = requests.get(PETSCAN_URL, params=parameters, timeout=TIMEOUT_FOR_PETSCAN).json()
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
