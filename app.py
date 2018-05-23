import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
os.environ["django_secret"]="5f^ouu_s%s@@(476pwmglzanj58a#eiv)p&v3x7h6_cs5+6@#c"
os.environ["environment"]="prod"

app = get_wsgi_application()
