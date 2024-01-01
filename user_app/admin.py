from django.contrib import admin
from user_app.models import Sex , MyCustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ['id' , 'email' , 'username' , 'age' , 'sex' , 'phone']
    list_editable = ['email' , 'username' , 'age' , 'sex' , 'phone']
    list_display_links = ['id']
    list_filter = ['id']

admin.site.register(MyCustomUser , UserAdmin)
admin.site.register(Sex)
