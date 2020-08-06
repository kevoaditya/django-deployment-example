from django import template
# This is the normal way
register = template.Library()


#this one line below is decorators
@register.filter(name='cut')
def cut(value,arg):
    # This cuts out all values of "arg" from the string!
    return value.replace(arg,'')

# register.filter('cut',cut)
