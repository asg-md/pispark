import math
from unittest import TestCase

from pi_file import pi_formula


class Test(TestCase):
    def test_pi_formula(self):
        estimacion_de_pi = pi_formula(100000)
        self.assertAlmostEqual(estimacion_de_pi, math.pi, 1)