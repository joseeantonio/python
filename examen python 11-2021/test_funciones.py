from funciones import *
import pytest
from ejercicios import ejercicios

def test_filtra_ejercicios():
    assert filtra_ejercicios([{"denominacion": "No hay respiro", "descripcion": "Buscamos llegar a tres pases en el equipo para devolver el balón al sacador de banda = 2 ptos.\nEste devolverá el balón al equipo pasador = 1 pto.\n(2x2, 3x3, 4x4...+1)\nVariante: logrados 3 pases en el equipo al pasar al sacador intercambio de funciones.", "estrategia": ["Siempre en movimiento.", "Acción para el otro.", "Dos actitudes en defensa a descubrir ante diversas valoraciones en el jugar.", "Enriquecer con cortes y su defensa. Chocar los cortes."], "duracion": 20},
                              {"denominacion": "Balón-azúcar", "descripcion": "4x1. Quien la para sólo puede pillar al jugador que no está en posesión de balón.\nAcotar el terreno de juego.", "estrategia": ["Anticipar.", "Fintar", "Apoyar la línea de pase.", "Crear exigencias antes de poder pasar y delimitar espacios."], "duracion": 10}],10)==[{"denominacion": "Balón-azúcar", "descripcion": "4x1. Quien la para sólo puede pillar al jugador que no está en posesión de balón.\nAcotar el terreno de juego.", "estrategia": ["Anticipar.", "Fintar", "Apoyar la línea de pase.", "Crear exigencias antes de poder pasar y delimitar espacios."], "duracion": 10}]

    assert filtra_ejercicios([{"denominacion": "No hay respiro",
                               "descripcion": "Buscamos llegar a tres pases en el equipo para devolver el balón al sacador de banda = 2 ptos.\nEste devolverá el balón al equipo pasador = 1 pto.\n(2x2, 3x3, 4x4...+1)\nVariante: logrados 3 pases en el equipo al pasar al sacador intercambio de funciones.",
                               "estrategia": ["Siempre en movimiento.", "Acción para el otro.",
                                              "Dos actitudes en defensa a descubrir ante diversas valoraciones en el jugar.",
                                              "Enriquecer con cortes y su defensa. Chocar los cortes."],
                               "duracion": 9},
                              {"denominacion": "Balón-azúcar",
                               "descripcion": "4x1. Quien la para sólo puede pillar al jugador que no está en posesión de balón.\nAcotar el terreno de juego.",
                               "estrategia": ["Anticipar.", "Fintar", "Apoyar la línea de pase.",
                                              "Crear exigencias antes de poder pasar y delimitar espacios."],
                               "duracion": 10}], 10) == [{"denominacion": "No hay respiro",
                               "descripcion": "Buscamos llegar a tres pases en el equipo para devolver el balón al sacador de banda = 2 ptos.\nEste devolverá el balón al equipo pasador = 1 pto.\n(2x2, 3x3, 4x4...+1)\nVariante: logrados 3 pases en el equipo al pasar al sacador intercambio de funciones.",
                               "estrategia": ["Siempre en movimiento.", "Acción para el otro.",
                                              "Dos actitudes en defensa a descubrir ante diversas valoraciones en el jugar.",
                                              "Enriquecer con cortes y su defensa. Chocar los cortes."],
                               "duracion": 9},{"denominacion": "Balón-azúcar",
                                                          "descripcion": "4x1. Quien la para sólo puede pillar al jugador que no está en posesión de balón.\nAcotar el terreno de juego.",
                                                          "estrategia": ["Anticipar.", "Fintar",
                                                                         "Apoyar la línea de pase.",
                                                                         "Crear exigencias antes de poder pasar y delimitar espacios."],
                                                          "duracion": 10}]



def test_duracion_ejercico():
    assert duracion_ejercicios(ejercicios)==490


def test_entrenamiento():
    assert duracion_ejercicios(entrenamiento(ejercicios,60))==60