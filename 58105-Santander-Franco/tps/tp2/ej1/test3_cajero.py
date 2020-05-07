import unittest
from billete import Billete1000, Billete500, Billete200
from cajero import Cajero


class TestCajero(unittest.TestCase):
    def setUp(self):

        self.b1000 = Billete1000()
        self.b500 = Billete500()
        self.b200 = Billete200()
        self.cajero = Cajero()
        billetes = []
        for i in range(0, 10):
            billetes.append(self.b1000)
        for i in range(0, 20):
            billetes.append(self.b500)
        for i in range(0, 15):
            billetes.append(self.b200)
        self.cajero.agregar_dinero(billetes)

    def test_contar(self):
        a = self.cajero.contar_dinero()
        self.assertEqual(a, "10 billetes de $1000, " +
                            "parcial $10000\n" +
                            "20 billetes de $500, " +
                            "parcial $10000\n" +
                            "15 billetes de $200, " +
                            "parcial $3000\n" +
                            "Total $23000")

    def test_extraer1(self):
        b = self.cajero.extraer_dinero(5000)
        self.assertEqual(b, "5 billetes de $1000\n")

    def test_extraer2(self):
        c = self.cajero.extraer_dinero(12000)
        self.assertEqual(c, "10 billetes de $1000\n" +
                            "4 billetes de $500\n")

    def test_extraer3(self):
        d = self.cajero.extraer_dinero(12100)
        self.assertEqual(d, "Error. No hay una combinacion de billetes"
                            " que nos permita extraer ese monto.")


if __name__ == "__main__":
    unittest.main()
