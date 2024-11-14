import unittest
from media import calcular_media  # Supondo que o algoritmo será implementado em 'media.py'

class TestMedia(unittest.TestCase):

    def test_media_basica(self):
        # Verifica se a média de notas comuns está correta
        self.assertEqual(calcular_media(5, 7, 9), 7.0)

    def test_media_zeros(self):
        # Verifica se a média de três notas zero é zero
        self.assertEqual(calcular_media(0, 0, 0), 0.0)

    def test_media_maxima(self):
        # Verifica se a média de três notas máximas é o valor máximo
        self.assertEqual(calcular_media(10, 10, 10), 10.0)

    def test_media_decimais(self):
        # Verifica se a média é calculada corretamente com valores decimais
        self.assertAlmostEqual(calcular_media(7.5, 8.5, 9.0), 8.333, places=3)

if __name__ == "__main__":
    unittest.main()
