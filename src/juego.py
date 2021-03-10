"""Flujo principal del juego"""

from clear_screen import clear
from src import cartas, jugador


class Juego:
    def __init__(self):
        self.jugadores = {}
        self.mazo = cartas.Mazo()

    def run(self):
        """Función principal del juego"""
        self.mazo.inicializar_mazo()
        self.mazo.barajar()

        self.crear_jugadores()
        self.manos_iniciales()

        self.imprimir_mesa()

    def manos_iniciales(self):
        numero_cartas = 2
        for i in range(numero_cartas):
            for j in range(len(self.jugadores) - 1, -1, -1):
                self.jugadores[j].mano.agregar_carta(self.mazo)
        self.jugadores[0].mano.get_mano()[1].voltear()

    def crear_jugadores(self):
        """Crea los jugadores en la mesa de blackjack"""
        cantidad = self.pedir_numero_jugadores()
        self.pedir_nombre_jugador(cantidad)
        self.jugadores[0] = jugador.Jugador("Dealer")

    def pedir_numero_jugadores(self):
        while True:
            try:
                clear()
                cantidad = int(input("¿Cuantos jugadores (1 - 7): ?"))
                if cantidad not in [1, 2, 3, 4, 5, 6, 7]:
                    raise
                break
            except:
                print("      Numero invalido... Digite un numero entre 1 y 7\n")
                input()
                continue
        return cantidad

    def pedir_nombre_jugador(self, cantidad):
        clear()
        for i in range(1, cantidad + 1):
            nombre = input("Nombre del jugador #{}: ".format(i))
            self.jugadores[i] = jugador.Jugador(nombre)

    def imprimir_mesa(self):
        clear()
        print("{}: ".format(self.jugadores[0].nombre), end=' ')
        for carta in self.jugadores[0].mano.get_mano():
            print("{}{}".format(carta.valor, carta.palo), end=' ')

        print("\n")

        for j in range(len(self.jugadores) - 1, 0, -1):
            print("{}: ".format(self.jugadores[j].nombre), end=' ')
            for carta in self.jugadores[j].mano.get_mano():
                print("{}{}".format(carta.valor, carta.palo), end=' ')
            print("\n")
