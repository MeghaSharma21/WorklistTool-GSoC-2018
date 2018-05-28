from django.conf.urls import url, include
from worklist import views

urlpatterns = [
        url(r'^create-worklist$', views.create_worklist, name='create_worklist'),
        url(r'^show-worklist$', views.search_worklist, name='show_worklist'),
        url(r'^$', views.homepage, name='homepage'),
        url(r'^homepage$', views.homepage, name='homepage'),
        url(r'^show-tasks$', views.search_task, name='show_tasks'),
        url(r'^update-task-info$', views.update_task_info, name='update_task_info'),
        url(r'oauth/', include('social_django.urls', namespace='social')),
        url(r'^mediawiki-login$', views.mediawiki_login, name='login_url'),
        url(r'^app-logout$', views.app_logout, name='app_logout'),
]
