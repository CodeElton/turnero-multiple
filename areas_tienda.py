def perfumeria():
    turnos_perfumes = 0
    while True:
        turnos_perfumes += 1
        yield turnos_perfumes


def farmacia():
    turnos_farmacia = 0
    while True:
        turnos_farmacia += 1
        yield turnos_farmacia


def cosmeticos():
    turnos_cosmeticos = 0
    while True:
        turnos_cosmeticos += 1
        yield turnos_cosmeticos