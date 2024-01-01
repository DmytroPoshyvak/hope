from main_app.models import Product , Category

class DataMixin():
    def my_data(self , *args , **kwargs):
        products = Product.objects.all()
        v = []
        for i in products:
            product = Product.objects.get(id = i.id)
            images = product.photos_set.all()
            v.append(images)
        vv = {'test' : v}
        cats = Category.objects.all()
        b = {}
        for i in cats:
            cat = Category.objects.get(id = i.id)
            products = cat.product_set.all()
            b[cat.category] = products
        context = dict(list(b.items()) + list(vv.items()))
        return context
        
        
