import mock
import mongomock
from mock import patch
from unittest import TestCase

from ahorcado.ahorcado_cesar import Ahorcado


class TestAhorcado(TestCase):
    def setUp(self):
        self.ahorcado = Ahorcado()
        self.ahorcado.client = mongomock.MongoClient()
        self.ahorcado.db = self.ahorcado.client[self.ahorcado.DATABASE_NAME]

    def tearDown(self):
        self.ahorcado.db.drop_collection('articles')

    def test_saveWord(self):
        try:
            self.ahorcado.saveWord('hola')
        except Exception:
            self.fail("saveWord fails when I try to add 'hola'")

    @patch('ahorcado.ahorcado_cesar.raw_input', return_value='Hello')
    def test_selectWord(self, input):
        self.assertEqual(self.ahorcado.selectWord(), 'hello')
