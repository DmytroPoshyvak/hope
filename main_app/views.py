from typing import Any, Dict
from django import http
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import *
from main_app.models import *
from main_app.utilts import DataMixin
from django.http import JsonResponse
from main_app.models import ProductInBasket , ProductInFavourite
from main_app.forms import CheckOutForm
from user_app.models import MyCustomUser
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

class HomeView(DataMixin , ListView):
    # paginate_by = 3
    model = Product
    context_object_name = 'list'
    template_name = 'index.html'

    def get_context_data(self, *args , **kwargs):
        get_context = super().get_context_data(*args , **kwargs)
        cats = Category.objects.filter(is_active = True)
        my_context = {'categories' : Category.objects.filter(is_active = True)}
        utilts_context = super().my_data(*args , **kwargs)
        context = dict(list(get_context.items()) + list(my_context.items()) + list(utilts_context.items()))
        a = 0
        for i in cats:
            a = a + 1
            cat_products = Product.objects.filter(is_active = True , category = i.id)[:3]
            context[f"n{a}"] = cat_products


        print('GET CONTEXT DATAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' , context)
        return context
        
    def get_queryset(self):
        my_context = Product.objects.filter(is_active = True)[:6]
        print('GET QUERYSET' , my_context)
        return my_context

class Categories(ListView):
    model = Category
    context_object_name = 'list'
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def get_queryset(self):
        return Category.objects.filter(is_active = True)

class CategoriesDetail(DataMixin , DetailView):
    # paginate_by = 3
    model = Category
    template_name = 'category_detail.html'

    def get_queryset(self):
        context = Category.objects.filter(is_active = True)
        return context

    def get_context_data(self, *args , **kwargs):
        # page = self.request.GET.get('page', 1)
        context_f = super().get_context_data(*args , **kwargs)


        cat = Category.objects.get(category = self.kwargs['slug'])
        my_cont = {'list' : cat.product_set.all()}
        utilts_context = super().my_data(*args , **kwargs)
        context = dict(list(my_cont.items()) + list(context_f.items()) + list(utilts_context.items()))


        products = Product.objects.filter(is_active = True , category = get_object_or_404(Category, category=self.kwargs['slug']))
        p = Paginator(products, 3)
        current_category = get_object_or_404(Category, category=self.kwargs['slug'])
        print(current_category)
        print('SSSSSSSSSSSSSSSSSSSSSSUUUUUUUUUUUUUUUDAAAAAAAAAAAAAAAAAA' , self.request.GET.get('page')
               , self.args , 'shtrgd' , self.kwargs , self.request.session)

        page_number = self.request.GET.get('page')
        page_obj = p.get_page(page_number)

        context['p'] = p
        context['page_number'] = page_number
        context['page_obj'] = page_obj


        pre_products = Product.objects.filter(is_active = True , is_prespense = True , category = get_object_or_404(Category, category=self.kwargs['slug']))
        pp = Paginator(pre_products, 3)

        page_numberr = self.request.GET.get('page')
        page_objj = pp.get_page(page_numberr)

        context['pp'] = pp
        context['page_objj'] = page_objj




        print(context)
        return context
    
class NewProducts(DataMixin , ListView):
    paginate_by = 6
    model = Product
    context_object_name = 'list'
    template_name = 'new_products.html'

    def get_context_data(self, *args , **kwargs):
        get_context = super().get_context_data(*args , **kwargs)
        my_context = {'categories' : Category.objects.filter(is_active = True)}
        utilts_context = super().my_data(*args , **kwargs)
        context = dict(list(get_context.items()) + list(my_context.items()) + list(utilts_context.items()))
        return context
        
    def get_queryset(self):
        context = Product.objects.filter(is_active = True , is_new = True)
        return context

class DetailProduct(DataMixin , DetailView):
    model = Product
    template_name = 'detail_product.html'

    def get_context_data(self, **kwargs):
        super_cont = super().get_context_data(**kwargs)
        print(self.kwargs , self.kwargs['slug'])
        product = Product.objects.get(slug = self.kwargs['slug'])
        products = Product.objects.filter(is_active = True)
        context = dict(list({'photos' : product.photos_set.all()}.items()) + list(super_cont.items()))
        return context

def busket_adding(request):

    context = dict()
    python_data = request.POST

    session_key = request.session.session_key
    product_name = python_data.get('product_name')
    product_id = python_data.get('product_id')
    product_price = python_data.get('prodcut_price')
    product_total_price = python_data.get('product_total_price')
    product_number = python_data.get('product_number')
    is_delete = python_data.get("is_delete")

    if is_delete == 'true':
        deleted_product = ProductInBasket.objects.get(session_key = session_key , product_id = product_id , is_active = True)
        deleted_product.is_active = False
        deleted_product.save()

    elif is_delete == 'emergency':
        update , new_product = ProductInBasket.objects.get_or_create(session_key = session_key ,
                                                            product_id = product_id ,
                                                            is_active = True,
                                                            defaults= {
                                                            'number' : product_number,
                                                            'product_total_price' : product_total_price,
                                                            })
        if not new_product:
            update.number = int(product_number)
            update.product_total_price = int(product_total_price)
            update.save()

    else:
        update , new_product = ProductInBasket.objects.get_or_create(session_key = session_key ,
                                                                    product_id = product_id ,
                                                                    is_active = True,
                                                                    defaults= {
                                                                    'number' : product_number,
                                                                    'product_total_price' : product_total_price,
                                                                    })
        if not new_product:
            update.number = update.number + int(product_number)
            update.product_total_price = update.product_total_price + int(product_total_price)
            update.save()
    
    context['products_in_basket'] = []
    products_in_basket = ProductInBasket.objects.filter(is_active = True , session_key = session_key)

    for i in products_in_basket:
        one_product = {}  
        one_product['product_name'] = i.product.name
        one_product['product_id'] = i.product.id
        one_product['number'] = i.number
        one_product['product_total_price'] = i.product_total_price
        one_product['product_price'] = i.product.price_with_discount
        context['products_in_basket'].append(one_product)

    number_of_products = ProductInBasket.objects.filter(is_active = True , session_key = session_key).count()
    context['number_of_products'] = number_of_products

    return JsonResponse(context)

def check_out(request):
    form = CheckOutForm()
    if request.method == 'POST':
        form = CheckOutForm(request.POST)
        print('method POST' , request.POST)

        if form.is_valid():
            data = request.POST
            name = data.get("name")
            age = data.get('age')
            email = data.get('email')
            session_key = data.get('session_key')
            new_data = list(data.items())
            user = data.get('id')
            updated_data = new_data[7:]
            print(updated_data , 'WHATCH' , new_data)
            if len(updated_data) >= 1:
                if name:
                    if user:
                        print(user , 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
                        order = Order.objects.create(session_key=session_key, name=name, email=email, is_active=True , user_id = user)
                    else:
                        order = Order.objects.create(session_key=session_key, name=name, email=email, is_active=True)
            else:
                order = False

            n = -1
            for i in updated_data:
                n = n + 1
                integer = int(updated_data[n][1]) * int(Product.objects.get(id=updated_data[n][0]).price_with_discount)
                products_in_order = ProductInOrder.objects.create(session_key = session_key , order_id = order.id , is_active = True,
                                                                  product_id = updated_data[n][0] , number = updated_data[n][1] ,
                                                                  product_total_price = integer)
                
            products_in_basket = ProductInBasket.objects.filter(session_key=session_key).update(is_active = False)
            orders_number = Order.objects.count()
            if orders_number > 5:
                order_another = Order.objects.filter(is_active=True).order_by('date_added').first()
                print(order_another)
                order_another.is_active = False
                order_another.save()
            if order:
                products = order.productinorder_set.all()
                v = 0
                for i in products:
                        v = v + i.product_total_price
                order.total_price = v
                order.status_id = 1
                order.save()

            for key , value in data.items():
                print(key , value)
        else:
            print('form is not valid' , form)

    context = {'form' : form }
    return render(request , 'check_out.html', context)

class DetailViewAccount(DetailView):
    model = MyCustomUser
    template_name = 'account_detail_view.html'

    def get_context_data(self, **kwargs):
        user = self.object  # Assuming MyCustomUser is the user associated with this view
        orders = Order.objects.filter(user=user, is_active=True).order_by('-date_added')
        products = ProductInOrder.objects.filter(order__in=orders , is_active = True).order_by('date_added')

        context = {'orders': orders, 'm': products}
        return context

class FeedBack(TemplateView):
    template_name = 'feed_back.html'

class Test(TemplateView):
    template_name = 'test.html'

class ListProducts(ListView):
    paginate_by = 6
    model = Product
    context_object_name = 'list'
    template_name = 'products.html'
    
    # def get_context_data(self, *args , **kwargs):
    #     get_context = super().get_context_data(*args , **kwargs)
    #     products_esp = Product.objects.filter(is_active = True , is_prespense = True)
    #     get_context['esp'] = products_esp
    #     return get_context

class ListProductsAvaliable(ListView):
    paginate_by = 6
    model = Product
    context_object_name = 'list'
    template_name = 'products_avaliable.html'

    def get_queryset(self):
        prod = Product.objects.filter(is_active=True, is_prespense=True)
        return prod
    
    def get_context_data(self, *args, **kwargs):
        products_ava = Product.objects.filter(is_active=True, is_prespense=True)
        context = super().get_context_data(*args, **kwargs)
        context['ava'] = products_ava
        return context

