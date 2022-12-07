from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

# testing models
class Test_Create_Post(TestCase):

  @classmethod
  def setUpTestData(cls) -> None:
    test_category = Category.objects.create(name="django")
    test_user1 = User.objects.create(username='testuser1', password='123456789')
    test_post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post Excerpt', content="Post content", slug='post-title', status='published', author_id=1)
    return super().setUpTestData()

  def test_blog_content(self):
    post = Post.postobjects.get(id=1)
    category = Category.objects.get(id=1)
    
    author = f'{post.author}'
    excerpt = f'{post.excerpt}'
    title = f'{post.title}'
    content = f'{post.content}'
    status = f'{post.status}'
    self.assertEqual(author, 'testuser1')
    self.assertEqual(excerpt, 'Post Excerpt')
    self.assertEqual(title, 'Post Title')
    self.assertEqual(content, 'Post content')
    self.assertEqual(status, 'published')
    self.assertEqual(str(post), 'Post Title')
    self.assertEqual(str(category), "django")
