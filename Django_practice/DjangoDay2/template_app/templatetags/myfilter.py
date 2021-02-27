from django import template

register =  template.Library()   # 创建Library对象，该对象用来注册模板过滤器


@register.filter(name="n2c")      # 注册模板过滤器
def number_to_chinese(value,info):   # 该函数是过滤器会实际执行的函数，value参数代表模板变量
    chineses = ["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
    try:
        return chineses[value] + "；过滤器参数为：" + info
    except:
        return "转换出错！" + "；过滤器参数为：" + info
