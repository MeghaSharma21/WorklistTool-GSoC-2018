from django.conf.urls import url
from worklist import views

urlpatterns = [
        url(r'^create-worklist$', views.create_worklist, name='create_worklist'),
        url(r'^show-worklist$', views.search_worklist, name='show_worklist'),
        url(r'^$', views.search_worklist, name='show_worklist'),
        url(r'^show-tasks$', views.search_task, name='show_tasks'),
]
