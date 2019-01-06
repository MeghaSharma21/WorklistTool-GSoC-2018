# Constant for the initial status being
# assigned to newly added articles
OPEN_STATUS = 'Open'

# Constant assigned for claimed tasks
CLAIMED_STATUS = 'Claimed'

# Constant for the initial progress being
# assigned to newly added articles
INITIAL_ARTICLE_PROGRESS = 0

# Constant for mapping article status to a
# number for storing purposes
ARTICLE_STATUS_TO_NUMBER_MAPPING = \
    {'Open': 0, 'Closed': 1, 'Claimed': 2}

# Constant for mapping a number to article status
ARTICLE_NUMBER_TO_STATUS_MAPPING = {
  number: status for status, number in ARTICLE_STATUS_TO_NUMBER_MAPPING.items()
}

# Search type for searching of worklists - by
# name of the worklist
SEARCH_BY_NAME_FOR_WORKLISTS = 'worklist_name'

# Search type for searching of worklists - by
# name of the user who had created it
SEARCH_BY_USERNAME_FOR_WORKLISTS = 'username'

# Default timeout for HTTP GET Request
TIMEOUT_IN_SECONDS = 10

