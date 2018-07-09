from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import TypeInfo, GoodsInfo

# Create your views here.
def index(request):             #主页
    #查询各分类的最新4条,最热4条信息
    typelist = TypeInfo.objects.all()        #首先获得外键指向的表中对象，然后通过‘_set’这样的方法获得目标表中的数据
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]          #按降序获得,获得最大的
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    context = {
        'title':'首页',
        'type0':type0, 'type01':type01,
        'type1':type1, 'type11':type11,
        'type2':type2, 'type21':type21,
        'type3':type3, 'type31':type31,
        'type4':type4, 'type41':type41,
        'type5':type5, 'type51':type51,
    }
    return render(request, 'df_goods/index.html', context)

def list(request, tid, pindex, sort):  #列表页     #分别为类型的id,第几页,按什么排序
    typeinfo = TypeInfo.objects.get(id=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]  #取该类型最新的两个
    if sort == '1':   #默认  最新
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
        # print(22233)
    elif sort == '2':     #按价格排序
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort == '3':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    paginator = Paginator(goods_list,10)         #分页, 每页有几个元素
    page = paginator.page(int(pindex))          #获得pindex页的元素列表
    context = {
        'title':typeinfo.ttitle,    #类型名称  为了给base传递title
        'page':page,        #排序后的每页的元素列表
        'typeinfo':typeinfo,    #类型信息
        'news':news,    #新品推荐列表
        'sort':sort,    #传递排序数字, 方便图标active
        'paginator':paginator,  #分页
    }
    return render(request, 'df_goods/list.html', context)

def detail(request, id):        #详情页    #商品id
    goods = GoodsInfo.objects.get(id=int(id))
    goods.gclick = goods.gclick + 1     #点击量
    goods.save()
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title':goods.gtype.ttitle,
        'goods':goods,
        'news':news,
        'id': id,
    }
    response = render(request, 'df_goods/detail.html', context)

    # #记录最近浏览,在用户中心使用
    # if request.session.has_key('user_id'):   #判断是否已经登录
    #     goods_ids = request.COOKIES.get('goods_ids','')     #获取浏览记录, 获取的值为str型
    #     # print(type(goods_ids))
    #     # print(goods_ids)
    #     goods_id = str(goods.id)        #将int型转化为str类型
    #     if goods_ids != '':     #判断是否有浏览记录,如果则继续判断
    #         goods_ids1 = goods_ids.split(',')   #以逗号分隔切片    切片后为list型
    #         if goods_ids1.count(goods_id) >= 1:     #如果已经存在,删除掉
    #             goods_ids1.remove(goods_id)
    #         goods_ids1.insert(0, goods_id)  #添加到第一个
    #         if len(goods_ids1) >= 6:        #如果超过6个则删除最后一个
    #             del goods_ids1[5]
    #         goods_ids=','.join(goods_ids1)     #  's'.join(seq)  以s作为分隔符，将seq所有的元素合并成一个新的字符串,为str型
    #     else:
    #         goods_ids=goods_id      #如果没有记录则直接加 ,   str型
    #     # print(type(goods_ids))
    #     # print(goods_ids)
    #     response.set_cookie('goods_ids',goods_ids)  #写入cookie

    #记录最近浏览,在用户中心使用
    if request.session.has_key('user_id'):   #判断是否已经登录
        key=str(request.session.get('user_id'))
        goods_ids=request.session.get(key,'')
        # print(type(goods_ids))
        # print(goods_ids)
        goods_id = str(goods.id)  # 将int型转化为str类型
        if goods_ids != '':  # 判断是否有浏览记录,如果则继续判断
            # goods_ids = goods_ids.split(',')  # 以逗号分隔切片    切片后为list型
            if goods_ids.count(goods_id) >= 1:  # 如果已经存在,删除掉
                goods_ids.remove(goods_id)
            goods_ids.insert(0, goods_id)  # 添加到第一个
            if len(goods_ids) >= 6:  # 如果超过6个则删除最后一个
                del goods_ids[5]
        else:
            goods_ids = []
            goods_ids.append(goods_id)
        # print(type(goods_ids))
        # print(goods_ids)
        request.session[key]=goods_ids
    return response

# from haystack.views import SearchView
# class MySearchView(SearchView):
#     def extra_context(self):
#         context=super(MySearchView,self).extra_context()
#         context['title']='搜索'
#         context['guest_cart']=1
#         return context

from haystack.views import SearchView
from lianxi.settings import HAYSTACK_SEARCH_RESULTS_PER_PAGE

class MySearchView(SearchView):
    def build_page(self):
        #分页重写
        context=super(MySearchView, self).extra_context()   #继承自带的context
        try:
            page_no = int(self.request.GET.get('page', 1))
        except Exception:
            return HttpResponse("Not a valid number for page.")

        if page_no < 1:
            return HttpResponse("Pages should be 1 or greater.")
        a =[]
        for i in self.results:
            a.append(i.object)
        paginator = Paginator(a, HAYSTACK_SEARCH_RESULTS_PER_PAGE)
        # print("--------")
        # print(page_no)
        page = paginator.page(page_no)
        return (paginator,page)

    def extra_context(self):
        context = super(MySearchView, self).extra_context()  # 继承自带的context
        context['title']='搜索'
        return context