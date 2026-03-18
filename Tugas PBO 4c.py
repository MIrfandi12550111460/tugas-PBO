import unittest

class Kalkulator:
    
    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    def bagi(self, a, b):
        if b == 0:
            raise ValueError("Tidak bisa membagi dengan nol!")
        return a / b
    

        from kalkulator import Kalkulator

class TestKalkulator(unittest.TestCase):

    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_tambah(self):
        self.assertEqual(self.kalkulator.tambah(2, 3), 6)

    def test_kurang(self):
        self.assertEqual(self.kalkulator.kurang(5, 3), 2)

    def test_kali(self):
        self.assertEqual(self.kalkulator.kali(4, 3), 12)

    def test_bagi(self):
        self.assertEqual(self.kalkulator.bagi(10, 2), 5)

if __name__ == "__main__":
    unittest.main()
