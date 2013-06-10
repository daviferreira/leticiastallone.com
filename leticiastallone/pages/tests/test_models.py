from django.test import TestCase

from pages.models import Page


class TestPageModel(TestCase):

    def setUp(self):
        self.page = Page.objects.create(title="Page 1", body="Page 1 body", keywords="page, test")

    def tearDown(self):
        Page.objects.all().delete()

    def test_unicode_should_return_the_page_title(self):
        self.assertEqual(str(self.page), self.page.title)
