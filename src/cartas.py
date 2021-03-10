"""Manejo de las cartas"""
import random


class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
        self.boca_abajo = False

    def esta_boca_abajo(self):
        return self.boca_abajo

    def voltear(self):
        self.boca_abajo = True


class Mazo:
    def __init__(self):
        self.mazo = []

    def tomar_carta(self):
        return self.mazo.pop()

    def inicializar_mazo(self):
        palos = ["C", "D", "E", "T"]
        cartas_palo = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for p in palos:
            for c in cartas_palo:
                self.mazo.append(Carta(p, c))

    def barajar(self):
        random.shuffle(self.mazo)

    def suma(self, a, b):
        return a + b


class Mano:
    def __init__(self):
        self.mano = []

    def get_mano(self):
        return self.mano

    def agregar_carta(self, mazo):
        self.mano.append(mazo.tomar_carta())
