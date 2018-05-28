from worklist.constants import ARTICLE_STATUS_TO_NUMBER_MAPPING,\
    INITIAL_ARTICLE_STATUS, INITIAL_ARTICLE_PROGRESS
from worklist.views_helper_functions.fetch_articles_from_petscan import \
    fetch_articles_from_petscan
from worklist.wikipedia_utils import convert_article_titles_into_ids
from worklist.models import Task, Articles
import logging

logger = logging.getLogger('django')


# Function to store newly added articles into Task & Article table
def store_added_articles(worklist_object, articles):
    success = True
    titles = []

    # Mapping article titles into IDs
    for article in articles:
        if article['name'] != '':
            titles.append(article['name'])
    article_ids = convert_article_titles_into_ids(titles)

    for article in articles:
        if article['name'] == '':
            continue
        title = article['name']
        data = {'article_id': article_ids[title], 'name': title}
        article_object = Articles.create_object(data)

        data = {'worklist': worklist_object,
                'article': article_object,
                'description': article['description'],
                'status':
                    ARTICLE_STATUS_TO_NUMBER_MAPPING[INITIAL_ARTICLE_STATUS],
                'progress': INITIAL_ARTICLE_PROGRESS,
                'effort': str(article['effort']),
                'created_by': article['created_by']}
        Task.create_object(data)

    if success is True:
        logger.info('Successfully saved added articles in task table')
    else:
        logger.info('Error occurred while saving added articles in task table')

    return success


# Function to store articles fetched from Petscan in Task & Article table
def store_psid_articles(worklist_object, psid, created_by):
    success = True
    # Fetching articles from petscan using psid
    results = fetch_articles_from_petscan(psid)

    if results is False or results['success'] is False:
        success = False
        return success

    titles = []

    # Mapping article titles into IDs
    for article in results['articles']:
        titles.append(str(article['title']))
    article_ids = convert_article_titles_into_ids(titles)

    for key, value in article_ids.items():
        data = {'article_id': value, 'name': key}
        article_object = Articles.create_object(data)

        data = {'worklist': worklist_object,
                'article': article_object,
                'psid': psid,
                'status':
                    ARTICLE_STATUS_TO_NUMBER_MAPPING[INITIAL_ARTICLE_STATUS],
                'progress': INITIAL_ARTICLE_PROGRESS,
                'created_by': created_by,
                'description': 'This article is a part of petscan '
                               'query having ID: {0}'.format(psid)}
        Task.create_object(data)

    if success is True:
        logger.info('Successfully saved petscan articles in task table')
    else:
        logger.info('Error occurred while saving petscan articles in task table')

    return success
