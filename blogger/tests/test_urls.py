from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blogger.views import (BlogListView, BlogDetailView, BlogCreateView, 
    CommentListView, CommentCreateView, BlogUpdateView, BlogDeleteView)

class TestUrls(SimpleTestCase):

	def test_bloglist_url_resolved(self):
		url = reverse('blog-home')
		self.assertEquals(resolve(url).func.view_class, BlogListView)

	def test_blogcreate_url_resolved(self):
		url = reverse('post-create')
		self.assertEquals(resolve(url).func.view_class, BlogCreateView)

	def test_blogdetail_url_resolved(self):
		url = reverse('post-detail', args=['1'])
		self.assertEquals(resolve(url).func.view_class, BlogDetailView)

	def test_commentlist_url_resolved(self):
		url = reverse('comment-list')
		self.assertEquals(resolve(url).func.view_class, CommentListView)

	def test_commentcreate_url_resolved(self):
		url = reverse('comment-create', args=['1'])
		self.assertEquals(resolve(url).func.view_class, CommentCreateView)

	def test_blogdelete_url_resolved(self):
		url = reverse('post-delete', args=['1'])
		self.assertEquals(resolve(url).func.view_class, BlogDeleteView)

	def test_blogupdate_url_resolved(self):
		url = reverse('post-update', args=['1'])
		self.assertEquals(resolve(url).func.view_class, BlogUpdateView)