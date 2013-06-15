# coding: utf-8
from datetime import datetime

from django.test import TestCase

from presentations.models import Presentation


class TestPresentationModel(TestCase):

    def setUp(self):
        self.presentation = Presentation.objects.create(title="Presentation 1",
                                                        abstract="Presentation 1 abstract",
                                                        embed='<iframe></iframe>',
                                                        pub_date=datetime.now())

    def tearDown(self):
        Presentation.objects.all().delete()

    def test_unicode_should_return_the_presentation_title(self):
        self.assertEqual(str(self.presentation), self.presentation.title)
