from rest_framework.renderers import JSONRenderer


class MyRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            code = data.pop("code")
            msg = data.pop("msg")
        except:
            code = "666"
            msg = "ok"

        result = {
            "code":code,
            "msg":msg,
            "data":data
        }
        return super().render(result)
