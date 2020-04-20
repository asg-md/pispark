from unittest import TestCase

from contador_de_palabras import cargar_texto, contador_de_palabras


class Test(TestCase):
    def test_partidor_palabras(self):
        texto = cargar_texto('texto_prueba.txt')
        n_palabras = contador_de_palabras(texto)
        self.assertEquals(n_palabras,15)