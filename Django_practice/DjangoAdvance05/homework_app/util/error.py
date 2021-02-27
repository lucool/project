from rest_framework.exceptions import APIException


class HomeException(APIException):
    def __init__(self,detail):
        self.detail = detail