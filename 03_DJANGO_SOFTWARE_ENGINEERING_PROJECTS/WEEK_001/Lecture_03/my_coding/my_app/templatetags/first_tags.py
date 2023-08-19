from django import template
from django.template.loader import get_template

register = template.Library()

def my_template(value,args):
    if args=='change':
        value="Alex Goot"
        return value
    if args=='title':
        return value.title()
register.filter('change_name',my_template)


def show_courses():
    courses=[{'Id':101,'course':'c++','Teacher':'Alex Smith'},{'Id':102,'course':'databases','Teacher':'Gorkie'},{'Id':103,'course':'django','Teacher':'Bruno'}]
    return {'courses': courses}
courses_template =get_template('my_app/courses.html')

register.inclusion_tag(courses_template)(show_courses)