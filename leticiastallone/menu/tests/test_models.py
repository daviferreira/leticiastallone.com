from django.test import TestCase
from menu.models import ItemMenu


class TestItemMenuModel(TestCase):

    def setUp(self):
        self.item_menu = ItemMenu.objects.create(label="ItemMenu 1", link="http://www.test.com", order=1)

    def tearDown(self):
        ItemMenu.objects.all().delete()

    def test_unicode_should_return_the_item_menu_title(self):
        self.assertEqual(str(self.item_menu), "%s <%s>" % (self.item_menu.label, self.item_menu.link))
