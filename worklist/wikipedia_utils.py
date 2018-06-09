from collections import defaultdict
import math
import mwclient


# Function that uses MediaWiki API that maps page titles to IDs
def convert_article_titles_into_ids(titles):
    if len(titles) == 0:
        return defaultdict(int)

    page_title_to_id_mapping = defaultdict(int)

    for i in range(math.ceil(len(titles) / 50)):
        # Since at max 50 titles can be passed in one request
        titles_list = ' | '.join(str(page) for page in
                                 titles[i * 50:(i + 1) * 50])

        site = mwclient.Site('en.wikipedia.org')
        result = site.api('query', prop='info', titles=titles_list)
        for page in result['query']['pages'].values():
            page_title_to_id_mapping[str(page.get('title'))] = page.get('pageid')

    return page_title_to_id_mapping
