from django import template

register = template.Library()


# Replaces all values of arg from the
# given string with underscore
def replace_space_filter(value, arg):
    return value.replace(arg, '_')


register.filter('replace', replace_space_filter)
