from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from blog_app.forms import PostForm
from blog_app.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class PostListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = 'blog.view_post'
    # model = Post
    queryset = Post.objects.filter(status=True).order_by('-created_date')
    context_object_name = 'posts'
    paginate_by = 2

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    # fields = ['author','title', 'content', 'status', 'category','published_date']
    success_url = '/blog/post/'

    # به صورت خودکار فردی که پست ایجاد میکنه اسم یا ایمیلش زیر پست قرار کیگیره و نیاز به وارد کزدن دستی نیست
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/blog/post/'