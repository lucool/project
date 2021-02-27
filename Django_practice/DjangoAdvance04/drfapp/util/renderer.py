from rest_framework.renderers import JSONRenderer


class MyJSONRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        print("data=",data,type(data))
        try:
            code = data.pop("code")    #  可以自己限定，只有验证失败了，才能弹出code与msg
            msg = data.pop("msg")
        except:
            code = "200"
            msg = "ok"

        result = {
            "code":code,
            "msg":msg,
            "data":data
        }
        return super().render(result)