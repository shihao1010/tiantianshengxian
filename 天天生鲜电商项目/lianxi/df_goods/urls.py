from django.conf.urls import url
from . import views
from .views import *
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^list/$', views.list, name='list'),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list, name='list'),      #第一个d+为类型的id, 第二个为当前是第几页,第三个是排序的依据
    url(r'^(\d+)/$', views.detail, name='detail'),     #详细页
    url(r'^search/$',MySearchView()),
]
