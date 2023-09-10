from django.http import HttpResponse
from django.urls import reverse

def home(request):
    one_home_url = reverse('One_contact')
    two_home_url = reverse('One_about')

    html_content = f'''
        I'm  home page
        <a href="{one_home_url}">one_contact</a>
        <a href="{two_home_url}">one_about</a>
    '''

    return HttpResponse(html_content)
