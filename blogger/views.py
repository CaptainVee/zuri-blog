from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class BlogListView(ListView):
	model = Post
	template_name = 'blogger/home.html'
	context_object_name = 'post'

class BlogCreateView(CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class BlogDetailView(DetailView):
	model = Post

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class CommentCreateView(CreateView):
	model = Comment
	fields = ['content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.post = get_object_or_404(Post, pk = self.kwargs.get('pk'))
		form.save()
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == comment.author:
			return True
		return False
