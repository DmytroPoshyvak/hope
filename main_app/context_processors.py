from main_app.models import ProductInBasket , Product , Order
from user_app.models import MyCustomUser
def basket(request):
    session_key = request.session.session_key
    if not session_key:
        
        request.session.cycle_key()
        print('NO THERE IS NO SESSION_KEY --------------------------------------' , request.session.session_key)
    else:
        print('THERE IS SESSION_KEY --------------------------------------------' , request.session.session_key)
    productss = ProductInBasket.objects.filter(is_active = True , session_key = session_key)
    all_products = Product.objects.filter(is_active = True).count()
    products_amount = productss.count()
    acc = MyCustomUser.objects.get(id = 1)
    orders = Order.objects.filter(is_active=True)
    products = Product.objects.filter(is_active = True)[:8]
    return locals()
