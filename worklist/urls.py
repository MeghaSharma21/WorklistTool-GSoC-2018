from django.conf.urls import url, include
from worklist import views

urlpatterns = [
        url(r'^create-worklist$', views.create_worklist, name='create_worklist'$
        url(r'^show-worklist$', views.show_worklist, name='show_worklist'),
        url(r'^$', views.show_worklist, name='show_worklist'),
]


