"""Jugador de Blackjack"""

from src import cartas


class Jugador:
    def __init__(self, nombre=""):
        self.nombre = nombre
        self.mano = cartas.Mano()
        self.pasar = False
        self.gano = False

    def set_nombre(self, nombre):
        self.nombre = nombre

    def pedir_carta(self, mazo):
        self.mano.agregar_carta(mazo)

    def pasar(self):
        self.pasar = True

    def gano(self):
        self.gano = True
