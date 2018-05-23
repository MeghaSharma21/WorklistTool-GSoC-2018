from worklist.constants import ARTICLE_STATUS_TO_NUMBER_MAPPING,\
    INITIAL_ARTICLE_STATUS, INITIAL_ARTICLE_PROGRESS
from worklist.helperFunctions.fetch_articles_from_petscan import \
    fetch_articles_from_petscan
from worklist.utility import convert_article_titles_into_ids
from worklist.models import Task, Articles
import logging

logger = logging.getLogger('django')


# Function to store newly added articles into Task table
def store_added_articles_in_task_table(worklist_id, articles):
    error = False
    titles = []
    for article in articles:
        titles.append(str(article['name']))
    article_ids = convert_article_titles_into_ids(titles)

    if article_ids == -1:
        error = True
        return error

    for article in articles:
        data = {'worklist_id': worklist_id,
                'article_id': article_ids(str(article['name'])),
                'description': str(article['description']),
                'status':
                    ARTICLE_STATUS_TO_NUMBER_MAPPING[INITIAL_ARTICLE_STATUS],
                'progress': INITIAL_ARTICLE_PROGRESS,
                'effort': str(article['effort']),
                'created_by': str(article['created_by'])}
        Task.create_object(data)

    store_articles_in_article_table(article_ids)

    if error is False:
        logger.info('Successfully saved added articles in task table')
    else:
        logger.info('Error occurred while saving added articles in task table')

    return error


# Function to store articles fetched from Petscan in Task table
def store_psid_articles_in_task_table(worklist_id, psid, created_by):
    error = False
    # Fetching articles from petscan using psid
    results = fetch_articles_from_petscan(psid)

    if results['success'] is False:
        error = True
        return error

    titles = []
    for article in results['articles']:
        titles.append(str(article['title']))
    article_ids = convert_article_titles_into_ids(titles)

    for key, value in article_ids:
        # todo Allow claimed_by, description to be null
        data = {'worklist_id': worklist_id,
                'article_id': value,
                'psid': psid,
                'status':
                    ARTICLE_STATUS_TO_NUMBER_MAPPING[INITIAL_ARTICLE_STATUS],
                'progress': INITIAL_ARTICLE_PROGRESS,
                'created_by': created_by}
        Task.create_object(data)

    store_articles_in_article_table(article_ids)

    if error is False:
        logger.info('Successfully saved petscan articles in task table')
    else:
        logger.info('Error occurred while saving petscan articles in task table')

    return error


# Function to store article information in Article table
def store_articles_in_article_table(input_articles):
    for key, value in input_articles.items():
        data = {'id': value, 'name': key}
        Articles.create_object(data)

        logger.info('Successfully saved articles in article table')
