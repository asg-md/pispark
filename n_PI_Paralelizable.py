from random import random as rnd


def calc_pi(n):
    x = []
    y = []
    radio = []
    dentro_circulo = 0
    for i in range(n):
        x = rnd()
        y = rnd()
        radio = (x ** 2 + y ** 2)
        if radio <= 1.0:
            dentro_circulo = dentro_circulo + 1

    return (4 * dentro_circulo) / n


# print(calc_pi(iteraciones))

n_maquinas = int(input(f"Cuantas máquinas se utilizarán?: "))
iteraciones = int(input(f"Cuantas iteraciones?: "))
calc_x_maquina = [int(iteraciones / n_maquinas) for n in range(n_maquinas)]

n_pi = sum(list(map(calc_pi, calc_x_maquina))) / n_maquinas

print(n_pi)
