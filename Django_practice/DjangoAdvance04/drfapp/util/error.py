from rest_framework.exceptions import APIException


class MyException(APIException):   # 自定义DRF异常类
    def __init__(self,detail):
        self.detail = detail   # 使用detail属性接收异常信息