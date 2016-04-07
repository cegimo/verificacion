from unittest import TestCase
from AhorcadoCesar import Ahorcado
import mock
import mongomock


class TestScraper(TestCase):
    def setUp(self):
        self.ahorcado = Ahorcado()
        self.ahorcado.client = mongomock.MongoClient()
        self.ahorcado.db = self.scraper.client[self.scraper.DATABASE_NAME]

    def test_get_all_words(self, mock_parse):
        self.assertIsNotNone()