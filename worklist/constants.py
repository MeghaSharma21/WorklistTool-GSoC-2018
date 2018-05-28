# Constant for the initial status being
# assigned to newly added articles
INITIAL_ARTICLE_STATUS = 'open'

# Constant for the initial progress being
# assigned to newly added articles
INITIAL_ARTICLE_PROGRESS = 0

# Constant for mapping article status to a
# number for storing purposes
ARTICLE_STATUS_TO_NUMBER_MAPPING = \
    {'open': 0, 'closed': 1, 'claimed': 2}

ARTICLE_NUMBER_TO_STATUS_MAPPING = \
    {0: 'open', 1: 'closed', 2: 'claimed'}

# Search type for searching of worklists - by
# name of the worklist
SEARCH_BY_NAME_FOR_WORKLISTS = 'worklist_name'

# Search type for searching of worklists - by
# name of the user who had created it
SEARCH_BY_USERNAME_FOR_WORKLISTS = 'username'
