import unittest
from src import cartas


class TestBaraja(unittest.TestCase):
    def test_inicializacion(self):
        nuevo_mazo = cartas.Mazo()
        nuevo_mazo.inicializar_mazo()
        self.assertIsNotNone(nuevo_mazo.mazo)

    def test_carta(self):
        nuevo_mazo = cartas.Mazo()
        nuevo_mazo.inicializar_mazo()
        self.assertIsInstance(nuevo_mazo.mazo[0], cartas.Carta)
