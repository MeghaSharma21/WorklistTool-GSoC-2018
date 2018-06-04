import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
os.environ["django_secret"] = "5f^ouu_s%s@@(476pwmglzanj58a#eiv)p&v3x7h6_cs5+6@#c"
os.environ["mediawiki_key"] = "70bed874bd3e1d8d749ab6635633d78d"
os.environ["mediawiki_secret"] = "d5125cbe417c8b695f33b622a28ef460b102063a"
os.environ["mediawiki_callback"] = "https://tools.wmflabs.org/worklist-tool/oauth/complete/mediawiki/"

app = get_wsgi_application()
