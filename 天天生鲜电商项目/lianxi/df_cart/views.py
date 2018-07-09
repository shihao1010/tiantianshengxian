from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import CartInfo
from df_user import user_decorator

# Create your views here.
@user_decorator.login
def cart(request):      #购物车
    uid =request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title':'购物车',
        'page_name':1,
        'carts':carts,
    }
    return render(request, 'df_cart/cart.html', context)

@user_decorator.login
def add(request, gid, count):       #分别为商品的id和数量
    if int(gid)==0 and request.is_ajax() and int(count)==0:
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()     #查询当前登录用户购物车的商品类型数量
        return JsonResponse({'count':count})
    uid = request.session['user_id']        #获取用户id
    gid = int(gid)  #转化为int型
    count = int(count)
    #查询购物车中是已有该商品,如果有则数量增加,如果没有则新增一个商品
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()
    #如果是ajax请求则返回json,否则转向购物车  测试  正常都不转
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()     #查询当前登录用户购物车的商品类型数量
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')   #转到购物车

def edit(request,gid,count):
    try:
        if request.is_ajax():
            goods = CartInfo.objects.get(id=int(gid))
            goods.count=int(count)
            goods.save()
            data={'ok':1}
    except Exception as e:
        data={'ok':int(count)}
    return JsonResponse(data)

def delete(request,gid):
    try:
        if request.is_ajax():
            goods=CartInfo.objects.get(id=int(gid))
            goods.delete()
            data={'ok':1}
            print(1111)
    except Exception as e:
        data={'ok':0,'e':e}
    return JsonResponse(data)

def place_order(request):
   return render(request,'df_cart/place_order.html')


