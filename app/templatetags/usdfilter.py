from django import template
register=template.Library()
@register.filter('swapping')
def swap(value):
    return value.swapcase()
def remove(value,arg):
    return value.replace(arg,'')
register.filter('remove',remove)
@register.filter(name='counting')
def count(value,arg):
    c=0
    for i in range(len(value)):
        if arg==value[i:i+len(arg):]:
            c+=1
    return c

