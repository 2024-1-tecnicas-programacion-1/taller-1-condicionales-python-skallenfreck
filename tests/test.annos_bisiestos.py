import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.annos_bisiestos import evaluar

class TestAnnosBisiestos(unittest.TestCase):
    def test_1988(self):
        valor_esperado = "1988 es bisiesto"
        valor_actual = evaluar(1988)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_2011(self):
        valor_esperado = "2011 no es bisiesto"
        valor_actual = evaluar(2011)
        self.assertEqual(valor_esperado, valor_actual)
    def test_1700(self):
        valor_esperado = "1700 no es bisiesto"
        valor_actual = evaluar(1700)
        self.assertEqual(valor_esperado, valor_actual)
    def test_1500(self):
        valor_esperado = "1500 no es bisiesto"
        valor_actual = evaluar(1500)
        self.assertEqual(valor_esperado, valor_actual)
    def test_2400(self):
        valor_esperado = "2400 es bisiesto"
        valor_actual = evaluar(2400)
        self.assertEqual(valor_esperado, valor_actual)
    def test_2024(self):
        valor_esperado = "2024 es bisiesto"
        valor_actual = evaluar(2024)
        self.assertEqual(valor_esperado, valor_actual)
    def test_2404(self):
        valor_esperado = "2404 es bisiesto"
        valor_actual = evaluar(2404)
        self.assertEqual(valor_esperado, valor_actual)
    def test_2100(self):
        valor_esperado = "2100 no es bisiesto"
        valor_actual = evaluar(2100)
        self.assertEqual(valor_esperado, valor_actual)
    def test_2200(self):
        valor_esperado = "2200 no es bisiesto"
        valor_actual = evaluar(2200)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
