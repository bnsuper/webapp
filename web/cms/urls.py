from django.conf.urls import url
from cms import views


urlpatterns = [
    url(r'^$', views.cms_index, name='cms_index'),
    url(r'^login/$', views.cms_login, name='cms_login'),
    url(r'^test/$', views.cms_test, name='cms_test'),
]
