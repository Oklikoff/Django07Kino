from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpform(UserCreationForm):
    username=forms.CharField(label='логин',
                             help_text='')
    password1 = forms.CharField(label='пароль',
        help_text='', widget=forms.PasswordInput(
            attrs={"autocomplite":"new-password"}
        )
    )
    password2 = forms.CharField(label='подтверждение',
        help_text='', widget=forms.PasswordInput(
            attrs={"autocomplite":"new-password"}
        )
    )
    email=forms.EmailField(label='почта',
        widget=forms.TextInput(attrs={'placeholder':'qwe@mail.ru'})
    )
    first_name=forms.CharField(label='имя', max_length=20)
    last_name = forms.CharField(label='фамилия', max_length=20, required=False)

    # class Meta():
    #     model=User
    #     fields=('username','password1','password1','first_name','last_name','email')