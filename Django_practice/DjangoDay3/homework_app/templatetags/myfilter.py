from django import template

register = template.Library()


@register.filter
def info_filter(value,key):
    try:
        return value[key]
    except:
        return "使用错误！"