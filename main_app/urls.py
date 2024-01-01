from django.urls import path
from main_app import views

urlpatterns = [
    path('prespense' , views.ListProductsAvaliable.as_view() , name = 'pro_ava'),
    path('prodcuts' , views.ListProducts.as_view() , name = 'pro'),
    path('/test' , views.Test.as_view() , name = 'test'),
    path('' , views.HomeView.as_view() , name = 'index'),
    path('categories' , views.Categories.as_view() , name = 'categories'),
    path('new_products' , views.NewProducts.as_view() , name = 'new_products'),
    path('busket_adding/' , views.busket_adding , name = 'busket_adding' ),
    path('check_out/' , views.check_out , name = 'check_out'),
    path('user/<slug:slug>' , views.DetailViewAccount.as_view() , name = 'user' ),
    path('<slug:slug>' , views.CategoriesDetail.as_view() , name = 'cat'),
    path('<slug:sluge>/<slug:slug>' , views.DetailProduct.as_view() , name = 'detail_product'),
    path('/feed_back' , views.FeedBack.as_view() , name = 'feed_back'),
]