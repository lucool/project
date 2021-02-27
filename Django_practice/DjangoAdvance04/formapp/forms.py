from django import forms


class UserForm(forms.Form):   # 自定义表单类
    regname = forms.CharField(label="注册用户名",max_length=10)
    regpwd = forms.CharField(label="注册密码",max_length=12,widget=forms.PasswordInput())
    reghome = forms.ChoiceField(label="籍贯",choices=((1,"北京"),(2,"上海"),(3,"山东")))
    regsex = forms.ChoiceField(label="性别",choices=((1,"男"),(2,"女")),widget=forms.RadioSelect())
