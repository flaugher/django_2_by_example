from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Post


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

#def post_list(request):
#    object_list = Post.published.all()
#    paginator = Paginator(object_list, 3) # 3 posts per page
#    page = request.GET.get('page')
#    try:
#        posts = paginator.page(page)
#    except PageNotAnInteger:
#        # If page is not an integer, deliver the first page
#        posts = paginator.page(1)
#    except EmptyPage:
#        # If page is out of range, deliver the last page of results
#        posts = paginator.page(paginator.num_pages)
#    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'