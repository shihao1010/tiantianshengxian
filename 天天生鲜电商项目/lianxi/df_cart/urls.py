from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart, name='cart'),
    url(r'^add(\d+)_(\d+)/$', views.add),     #加入购物车  分别为商品的id和数量
    url(r'^edit(\d+)_(\d+)/$', views.edit),   #修改购物车中商品的数量 分别为商品的id和数量
    url(r'^delete(\d+)/$',views.delete),      #删除购物车中的某个商品
    url(r'^place_order/$',views.place_order),
]