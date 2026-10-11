from pista_de_corrida import *
import unittest

class TestarVeiculo(unittest.TestCase):
    def testar_veiculo(self):
        v1 = Veiculo("ABC1010", "Vermelho", 10, 0, 10, "O-O")
        self.assertEqual(v1.placa, "ABC1010")
        self.assertEqual(v1.cor, "Vermelho")
        self.assertEqual(v1.tanque, 10)
        self.assertEqual(v1.odometro, 0)
        self.assertEqual(v1.rendimento, 10)
        self.assertEqual(v1.desenho, "O-O")