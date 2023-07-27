from django.shortcuts import render

# Create your views here.
def my_app(request):
    contex=    context = {
        'author': 'My_app',
        'age': 19,
        'marks': 65,
        'courses': [
            {
                'id': 1,
                'course': 'C++',
                'teacher': 'Akram Khan',
            },
            {
                'id': 2,
                'course': 'database',
                'teacher': 'Alex Goot'
            },
            {
                'id': 3,
                'course': 'Django',
                'teacher': 'Goytrne Alex',
            },
        ],
        'my_list' :[1,2,3,4,5,5],
        'blog':"Excellent: We demand excellence. We understand the importance of critical thinking, discipline and responsibility, and we expect the very highest standards of ourselves and our students.",
    }
    return render(request,'./my_app/index.html',context)
