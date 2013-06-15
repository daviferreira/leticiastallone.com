# coding: utf-8
from datetime import datetime

from django.test import TestCase

from publications.models import Article


class TestArticleModel(TestCase):

    def setUp(self):
        self.post = Article.objects.create(title="Article 1",
                                           abstract="Article 1 abstract",
                                           authors=u'Letícia, Davi',
                                           journal='Journal of Automated Testing',
                                           pub_date=datetime.now())

    def tearDown(self):
        Article.objects.all().delete()

    def test_unicode_should_return_the_post_title(self):
        self.assertEqual(str(self.post), self.post.title)
