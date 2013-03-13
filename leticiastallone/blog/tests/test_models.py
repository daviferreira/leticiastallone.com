from django.test import TestCase
from blog.models import Post


class TestPostModel(TestCase):

    def setUp(self):
        self.post = Post.objects.create(title="Post 1", body="Post 1 body", tags="post, test")

    def tearDown(self):
        Post.objects.all().delete()

    def test_unicode_should_return_the_post_title(self):
        self.assertEqual(str(self.post), self.post.title)
