from django.conf.urls import url
from mytest import views


urlpatterns = [
    url(r'^$', views.mytest_index, name='mytest_index'),
]
