from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'
    # Post 모델을 사용하면 post_list.html이 필요하다.
    # PostList 클래스에서 template_name을 직접 지정해줄 수도 있고, post_list.html을 만들어줄 수도 있다.
    #template_name = 'blog/index.html'




# CBV방식 기능 구현(참고용으로만 보자)
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts':posts
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post
#         }
#     )
