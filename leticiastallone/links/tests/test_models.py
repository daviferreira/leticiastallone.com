from django.test import TestCase

from links.models import ItemLink


class TestItemLinkModel(TestCase):

    def setUp(self):
        self.item_link = ItemLink.objects.create(title="ItemLink 1",
                                                 description="Description",
                                                 link="http://www.test.com",
                                                 order=1,
                                                 new_window=True)

    def tearDown(self):
        ItemLink.objects.all().delete()

    def test_unicode_should_return_the_item_link_title(self):
        self.assertEqual(str(self.item_link), "%s" % self.item_link.title)
