from django.db import models

# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey('df_user.UserInfo', on_delete=models.CASCADE)
    goods = models.ForeignKey('df_goods.GoodsInfo', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)     #买的数量
    class Meta:
        verbose_name = '购物车商品信息'
        verbose_name_plural = '购物车商品信息'
