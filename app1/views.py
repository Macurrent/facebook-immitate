from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from app1.forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User
from .forms import PostForm
from django import forms
from django.utils import timezone
from app1.models import Post
from django.shortcuts import render, get_object_or_404
# Sign Up View


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'app1/index.html'


# Editor Profile View


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('post_detail')
    template_name = 'app1/profile.html'


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app1/posted_items.html', {'post': post})    

# post


def Post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'app1/post.html', {'form': form})


   
