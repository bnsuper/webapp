from django.conf.urls import url
from cms import views


urlpatterns = [
    url(r'^$', views.cms_index, name='cms_index'),
    url(r'^authors/(?P<current_page>\d+)/$', views.cms_index, name='cms_author_pages'),
    url(r'^article/$', views.cms_article_manager, name='cms_article_manager'),
    url(r'^login/$', views.cms_login, name='cms_login'),
    url(r'^test/$', views.cms_test, name='cms_test'),
]
