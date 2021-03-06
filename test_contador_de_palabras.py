from unittest import TestCase

from contador_de_palabras import cargar_texto, limpiar_acentos, partidor_palabras


class Test(TestCase):
    def test_partidor_palabras(self):
        texto = cargar_texto('texto_prueba.txt')
        n_palabras = len(partidor_palabras(limpiar_acentos(texto).upper()))
        self.assertEquals(n_palabras,15)


class Test(TestCase):
    def test_limpiar_acentos(self):
        texto = 'Hóla añigo'
        self.assertEquals(limpiar_acentos(texto),'Hola anigo')
