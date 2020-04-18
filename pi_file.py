from random import random as rnd

def pi_formula(iteraciones):
    # en iteraciones saldrá la probabilidad 1 (área total del cuadrado 4),
    # pero dentro del círculo será la probabilidad (dentro_circulo) de PI

    dentro_circulo = 0

    for i in range(iteraciones):
        x = rnd()
        y = rnd()
        radio = ((x ** 2 + y ** 2) ** 0.5)
        if radio <= 1.0:
            dentro_circulo = dentro_circulo + 1

        estimar_pi = (4 * dentro_circulo) / iteraciones

    return estimar_pi
