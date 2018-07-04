import os
import pymysql
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
os.environ["django_secret"]=<<DJANGO SECRET>>
os.environ["environment"]="prod"
os.environ["mediawiki_key"]=<<MEDIAWIKI KEY>>
os.environ["mediawiki_secret"]=<<MEDIAWIKI SECRET>>
os.environ["mediawiki_callback"]="https://tools.wmflabs.org/worklist-tool/oauth/complete/mediawiki/"

pymysql.install_as_MySQLdb()

app = get_wsgi_application()
