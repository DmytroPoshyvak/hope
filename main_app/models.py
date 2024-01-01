from django.db import models
from django.urls import reverse
from user_app.models import MyCustomUser

class Category(models.Model):
    category = models.CharField(max_length=225)
    photo = models.ImageField(upload_to = 'media' , null=True)
    slug = models.SlugField()
    is_active = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category
    
    def get_absolute_url(self):
        return reverse('cat' , kwargs={'slug' : self.slug})

class Product(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    name = models.CharField(max_length=225 , null=True)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True , null=True)
    price_with_discount = models.PositiveIntegerField(null=True , blank=True)
    is_new = models.BooleanField(null=True , blank=True)
    description = models.TextField()
    characters = models.TextField(null=True)
    short = models.CharField(max_length=225 , null = True , blank = True)
    slug = models.SlugField()
    is_prespense = models.BooleanField(null = True)
    is_active = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('detail_product' , kwargs={'sluge' : self.category.slug , 'slug' : self.slug})

    def save(self , *args , **kwargs):
        if self.discount:
            self.price_with_discount = self.price - (self.discount * self.price / 100)
            super().save(*args, **kwargs)
        else:
            self.price_with_discount = self.price
            super().save(*args, **kwargs)
        

    def __str__(self):
        return self.name

class Photos(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    photot = models.ImageField(upload_to = 'media')
    is_main = models.BooleanField()
    is_active = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name}"

class ProductInBasket(models.Model):
    order = models.ForeignKey('Order' , on_delete=models.CASCADE , null = True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , null=True)
    session_key = models.CharField(max_length=225 , null=True)
    product_total_price = models.IntegerField(null=True)
    number = models.PositiveBigIntegerField(null=True)
    discount = models.PositiveIntegerField(blank=True , null=True)
    is_active = models.BooleanField(null=True)
    date_added = models.DateTimeField(auto_now_add=True , null=True)
    time_edited = models.DateTimeField(auto_now=True , null=True)
    
    # def save(self , *args , **kwargs):
    #     products = P
    #     self.total_products_amount = int(self.product_total_price) + int(self.)
    #     super().save(*args, **kwargs)

class ProductInOrder(models.Model):
    order = models.ForeignKey('Order' , on_delete=models.CASCADE , null = True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , null=True)
    session_key = models.CharField(max_length=225 , null=True)
    product_total_price = models.IntegerField(null=True)
    number = models.PositiveBigIntegerField(null=True)
    discount = models.PositiveIntegerField(blank=True , null=True)
    is_active = models.BooleanField(null=True)
    date_added = models.DateTimeField(auto_now_add=True , null=True)
    time_edited = models.DateTimeField(auto_now=True , null=True)

    def save(self , *args , **kwargs):
        if not self.product_total_price:
            if self.discount:
                product_total_price = int(self.number) * int(self.product.price) * (self.product.discount) / 100
                super().save(*args, **kwargs)
            else:
                product_total_price = int(self.number) * int(self.product.price)
                super().save(*args, **kwargs)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name

class ProductInFavourite(models.Model):
    session_key = models.CharField(max_length=225 , null=True)
    product_total_price = models.IntegerField(null=True)
    number = models.PositiveBigIntegerField(null=True)
    discount = models.PositiveIntegerField(blank=True , null=True)
    is_active = models.BooleanField(null=True)
    date_added = models.DateTimeField(auto_now_add=True  ,null=True)
    time_edited = models.DateTimeField(auto_now=True , null=True)

class Order(models.Model):
    status = models.ForeignKey('Status' , on_delete=models.DO_NOTHING , null=True)
    session_key = models.CharField(max_length=225 , null=True)
    user = models.ForeignKey(MyCustomUser , on_delete=models.CASCADE , null=True)
    name = models.CharField(max_length=225 , null=True)
    surname = models.CharField(max_length=225 , null=True)
    email = models.EmailField(null=True)
    adress = models.TextField(null=True)
    is_active = models.BooleanField(null=True)
    date_added = models.DateTimeField(auto_now_add=True , null=True)
    time_edited = models.DateTimeField(auto_now=True)
    total_price = models.IntegerField(null=True)

    # def save(self , *args , **Kwargs):
    #     order = Orders.ob
    #     if self.total_price == None or 0:
    #         self.total_price = self..productinorder_set.all()

    # def __str__(self):
    #     return 'замовлення'

class Status(models.Model):
    status = models.CharField(max_length=225)
    is_active = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True , null=True)
    time_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status