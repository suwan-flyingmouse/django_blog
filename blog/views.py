
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'
    # Post 모델을 사용하면 post_list.html이 필요하다.
    # PostList 클래스에서 template_name을 직접 지정해줄 수도 있고, post_list.html을 만들어줄 수도 있다.
    #template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post