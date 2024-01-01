from django import forms
from user_app.models import MyCustomUser
from django.contrib.auth.forms import UserCreationForm

class MyCustomUserCreationForm(UserCreationForm):
    # def __init__(self , *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].help_text = ''
    #     self.fields['password1'].help_text = ''

    class Meta:
        model = MyCustomUser
        fields = ['username' , 'email' , 'phone']



# class MyPersonalUserCreationForm(UserCreationForm):
#     def __init__(self , *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].help_text = ''
#         self.fields['password1'].help_text = ''

#     class Meta:
#         model = MyCustomUser
#         fields = ['username' , 'email' , 'phone']