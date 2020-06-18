from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# posts = [
#     {
#         'author':'achyuth',
#         'title':'blog1',
#         'content':'first post content',
#         'date_posted':'august 27, 2020'
#     },
#       {
#         'author':'jandoe',
#         'title':'blog2',
#         'content':'first post content',
#         'date_posted':'august 28, 2020'
#     }
# ]
def home(request):
    context = {
        'posts':Post.objects.all(),
        
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')