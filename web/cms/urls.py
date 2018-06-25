from django.conf.urls import url
from cms import views


urlpatterns = [
    url(r'^$', views.cms_index, name='cms_index'),
    url(r'^authors/(?P<current_page>\d+)/$', views.cms_index, name='cms_author_pages'),
    url(r'^authors/delete/$', views.cms_author_delete, name='cms_author_delete'),
    url(r'^authors/modify/(?P<uid>[\w\-]+)/$', views.cms_author_modify, name='cms_author_modify'),
    url(r'^article/(?P<current_page>\d+)/$', views.cms_article_manager, name='cms_article_manager'),
    url(r'^article/query/$', views.cms_article_query, name='cms_article_query'),
    url(r'^login/$', views.cms_login, name='cms_login'),
    url(r'^logout/$', views.cms_logout, name='cms_logout'),
    url(r'^test/$', views.cms_test, name='cms_test'),
]
