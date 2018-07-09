from django.db import models
from DjangoUeditor.models import UEditorField
from faker import Factory   #作假数据
import random
# Create your models here.

class TypeInfo(models.Model):       #index首页商品分类信息
    ttitle = models.CharField('类型名称',max_length=20)
    isDelete = models.BooleanField('是否删除', default=False)   #是否删除,默认不删
    def __str__(self):
        return self.ttitle
    class Meta:
        verbose_name = '分类信息'
        verbose_name_plural = '分类信息'

class GoodsInfo(models.Model):      #商品信息
    gtitle = models.CharField('商品名称', max_length=20)
    gpic = models.ImageField('商品图片',upload_to='df_goods', null=True, blank=True)      #商品图片
    gprice = models.DecimalField('商品价格',max_digits=7, decimal_places=2)        #总共最多有7位,小数占2位
    gunit = models.CharField('商品单位',max_length=20, default='500g')     #商品的单位
    gclick = models.IntegerField('点击量')          #商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除',default=False)
    gjianjie = models.CharField('简介',max_length=200)     #商品简介
    gkucun = models.IntegerField('库存')          #商品库存
    gcontent = UEditorField('详细介绍', height=300, width=1000)                  #商品详细内容
    gtype = models.ForeignKey(TypeInfo, verbose_name='所属分类', on_delete=models.CASCADE)     #商品所属类型
    # gadv = models.BooleanField(default=False)   #商品推荐
    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'

#
# TypeInfo_list = TypeInfo.objects.all()
#
# fake = Factory.create('zh_CN')   #伪造数据生成器    可批量造假数据测试
# for i in range(0,300):
#     j = random.randint(0, 100)
#     s1 = random.randint(0, 100)
#     s2 = random.randint(0, 100)
#     k = random.randint(0, 5)
#     v = GoodsInfo(
#         gtitle=fake.text(max_nb_chars=10),
#         gpic='df_goods/goods.jpg',
#         gprice=j,
#         gunit='500g',
#         gclick=0,
#         isDelete=fake.pybool(),   #是否删除
#         gjianjie=fake.text(max_nb_chars=70),
#         gkucun=s2,
#         gcontent=fake.text(max_nb_chars=300),
#         gtype=TypeInfo_list[k],   #所属类型
#     )
#     v.save()
