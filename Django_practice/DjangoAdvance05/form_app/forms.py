from django import forms


class RegisterForm(forms.Form):   # 自定义表单类
    regname = forms.CharField(label="注册名",required=True,max_length=10)
    regpwd = forms.CharField(label="注册密码",required=True,widget=forms.PasswordInput())  # 通过widget挂件设置为密码框
    reghome = forms.ChoiceField(label="籍贯",choices=((1,"北京"),(2,"陕西"),(3,"江苏")))
    regsex = forms.ChoiceField(label="性别",choices=((1,"男"),(2,"女")),widget=forms.RadioSelect())  # 添加单选按钮挂件