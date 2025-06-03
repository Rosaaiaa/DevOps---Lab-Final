import unittest
from app import app
import werkzeug
# Patch temporário para adicionar o atributo '__version__' em werkzeug

if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Criação do cliente de teste
        cls.client = app.test_client()

    def test_rota_invalida(self):
        response = self.client.get('/rota_invalida')
        self.assertEqual(response.status_code, 404)


    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"items": ["item1", "item2", "item3"]})


    def test_token_invalido(self):
        headers = {'Authorization': 'Bearer tokeninvalido123'}
        response = self.client.get('/protected', headers=headers)
        self.assertEqual(response.status_code, 422) 

if __name__ == '__main__':
    unittest.main()