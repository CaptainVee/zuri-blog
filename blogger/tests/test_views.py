from django.test import TestCase, Client, override_settings
from django.urls import reverse
from blogger.models import Post, Comment
import json
from django.contrib.auth.models import User



@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestView(TestCase):
	def setUp(self):
		self.user1 = User.objects.create(
			username='user1',
			email='test@gmail.com',
			password='password'

			)

		self.post1 = Post.objects.create(
            title='test post',
            content='this is a test content',
            author=self.user1
			)

	def test_blog_list_GET(self):
		response = self.client.get(reverse('blog-home'))
		self.assertContains(response, 'test post')
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blogger/home.html')


	def test_blog_detail_GET(self):
		response = self.client.get(reverse('post-detail', args=['1']))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blogger/post_detail.html')

	def test_blog_create_POST(self):
		url = reverse('post-create')
		self.client.force_login(user=self.user1)
		response = self.client.post(url, {
			'title': 'test post2',
			'content': 'this is another test post',
			'author': 'user2'
			})

		self.assertEquals(response.status_code, 302)

	def test_blog_detail_DELETE(self):
		response = self.client.get(reverse('post-delete', args=['1']))

		self.assertEquals(response.status_code, 302)

	def test_comment_create_POST(self):
		url = reverse('comment-create', args=['1'])
		self.client.force_login(user=self.user1)
		response = self.client.post(url, {
			'content': 'this is a test comment',
			})