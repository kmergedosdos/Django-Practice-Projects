from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient

# TESTING REST FRAMEWORK API.

class PostTests(APITestCase):

  # test PostList view to see if we can view the posts with the api
  def test_view_posts(self):
    # get endpoint
    url = reverse("blog_api:postlist") #[app_name]:[path_name]
    # get response
    response = self.client.get(url, format='json')
    # test response
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  # test PostList view to see if we can create data with the api
  def test_create_post(self):
    self.test_category = Category.objects.create(name='django')
    self.test_user1 = User.objects.create_user(username='testuser1', password='123456789')
    data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}

    # create a user
    self.client.login(username=self.test_user1.username, password='123456789')

    # get endpoint
    url = reverse("blog_api:postlist")
    # get response
    response = self.client.post(url, data, format='json')
    # test response
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_post_update(self):
    client = APIClient()

    self.test_category = Category.objects.create(name='django')
    self.test_user1 = User.objects.create_user(username='testuser1', password='123456789')
    self.test_user2 = User.objects.create_user(username='testuser2', password='123456789')

    test_post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post Excerpt', content="Post content", slug='post-title', status='published', author_id=1)

    client.login(username=self.test_user1.username, password='123456789')

    url = reverse("blog_api:postdetail", kwargs={'pk': 1})
    data = {"title": "new", "author": 1, "excerpt": "new", "content": "new", "status": 'published'}
    response = client.put(url,data, format='json')
    print(response.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
