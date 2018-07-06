from django.conf.urls import url
from cms import views


urlpatterns = [
    url(r'^$', views.cms_index, name='cms_index'),
    url(r'^authors/(?P<current_page>\d+)/$', views.cms_index, name='cms_author_pages'),
    url(r'^authors/delete/$', views.cms_author_delete, name='cms_author_delete'),
    url(r'^authors/modify/(?P<uid>[\w\-]+)/$', views.cms_author_modify, name='cms_author_modify'),
    url(r'^article/$', views.cms_article_manager, name='cms_article_manager'),
    url(r'^article/delete/$', views.cms_article_delete, name='cms_article_delete'),
    url(r'^article/top/$', views.cms_article_top, name='cms_article_top'),
    url(r'^article/untop/$', views.cms_article_untop, name='cms_article_untop'),
    url(r'^article/query/$', views.cms_article_query, name='cms_article_query'),
    url(r'^article/modify/(?P<uid>[\w\-]+)/$', views.cms_article_modify, name='cms_article_modify'),
    url(r'^article/add_category/$', views.cms_add_category, name='cms_add_category'),
    url(r'^article/add_tag/$', views.cms_add_tag, name='cms_add_tag'),
    url(r'^login/$', views.cms_login, name='cms_login'),
    url(r'^logout/$', views.cms_logout, name='cms_logout'),
    url(r'^test/$', views.cms_test, name='cms_test'),
]
