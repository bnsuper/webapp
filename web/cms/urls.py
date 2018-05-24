from django.conf.urls import url
from cms import views


urlpatterns = [
    url(r'^$', views.cms_index, name='cms_index'),
]
