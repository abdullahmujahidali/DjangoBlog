from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Abdullah Mujahid',
        'title': 'Blog Post',
        'content': 'First Post',
        'date_posted': 'August 27,1998'
    },
    {
        'author': 'Saima Khan',
        'title': 'Post Test',
        'content': '2nd in line ',
        'date_posted': 'July 27,2011'
    },
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})