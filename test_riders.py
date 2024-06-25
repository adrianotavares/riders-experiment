import unittest
import json
from riders import app  # Importe o aplicativo Flask

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        # Cria um cliente de teste
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        # Testa a resposta da rota raiz
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_riders_without_city(self):
        # Testa obter motociclistas sem especificar cidade
        response = self.app.get('/riders')
        self.assertEqual(response.status_code, 200)
        # Verifica se a resposta contém a chave correta (ajuste conforme necessário)
        data = json.loads(response.data.decode())
        self.assertIn('error', data)

    def test_get_riders_all_cities(self):
        # Testa obter motociclistas para todas as cidades
        response = self.app.get('/riders?city=ALL')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIsInstance(data, list)  # Supondo que todos os dados sejam retornados como lista

    def test_get_riders_specific_city(self):
        # Testa obter motociclistas para uma cidade específica válida
        response = self.app.get('/riders?city=Belo Horizonte')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIsInstance(data, list)  # Checa se retorna lista

    def test_get_riders_non_existent_city(self):
        # Testa obter motociclistas para uma cidade inexistente
        response = self.app.get('/riders?city=NoCity')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data.decode())
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
