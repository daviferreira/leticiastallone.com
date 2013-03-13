from django.test import TestCase
from blog.models import Post


class TestPostModel(TestCase):

    def setUp(self):
        self.post = Post.objects.create(title="Post 1", body="Post 1 body", tags="post, test")

    def tearDown(self):
        Post.objects.all().delete()

    def testItShouldAlterThePostsCount(self):
        self.assertEqual(len(Post.objects.all()), 1)
