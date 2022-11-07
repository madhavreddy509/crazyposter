from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . models import Post
from django.contrib.auth.models import User


# Create your views here.
def home (request):
    posts=Post.objects.all()
    
    return render(request,'home.html',{'context':posts})

class PostListView(ListView):
    model=Post
    template_name='home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=6

class UserPostListView(ListView):
    model=Post
    template_name='user_posts.html'
    context_object_name='posts'
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
class PostDetailView(DetailView):
    model=Post
    template_name='post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content','photo']
    template_name='post_form.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content','photo']
    template_name='post_form.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author :
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name='post_confirm_delete.html'
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author :
            return True
        return False


def about(request):
    return render(request,'about.html')