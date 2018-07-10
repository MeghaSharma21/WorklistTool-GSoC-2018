from django.conf.urls import url, include
from worklist import views

urlpatterns = [
        url(r'^add-articles-to-worklistt$', views.add_articles_to_worklist, name='add_articles_to_worklist'),
        url(r'^create-worklist$', views.create_worklist, name='create_worklist'),
        url(r'^show-worklist$', views.search_worklist, name='show_worklist'),
        url(r'^update-worklist-table$', views.update_worklist_table, name='update_worklist_table'),
        url(r'^update-task-table(?:/(?P<worklist_created_by>[\s\S]+))?/(?:/(?P<worklist_name>[\s\S]+))?/$', views.update_task_table, name='update_task_table'),
        url(r'^$', views.homepage, name='homepage'),
        url(r'^homepage$', views.homepage, name='homepage'),
        url(r'^show-tasks/(?P<worklist_created_by>[\s\S]+)/(?P<worklist_name>[\s\S]+)?/$', views.search_task, name='show_tasks'),
        url(r'^update-task-info(?:/(?P<worklist_created_by>[\s\S]+))?/(?:/(?P<worklist_name>[\s\S]+))?/$', views.update_task_info, name='update_task_info'),
        url(r'oauth/', include('social_django.urls', namespace='social')),
        url(r'^mediawiki-login$', views.mediawiki_login, name='login_url'),
        url(r'^app-logout$', views.app_logout, name='app_logout'),
        url(r'^show-user-worklists$', views.show_user_worklists, name='show_user_worklists'),
        url(r'^refresh-task-page-views(?:/(?P<worklist_created_by>[\s\S]+))?/(?:/(?P<worklist_name>[\s\S]+))?/$', views.refresh_task_page_views, name='refresh_task_page_views'),

]
