import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.edad import evaluar

class TestEdad(unittest.TestCase):
    def test2000Enero1(self):
        valor_esperado = "Usted tiene 24 años"
        valor_actual = evaluar(1, 1, 2000)
        self.assertEqual(valor_esperado, valor_actual)
    
def test2005Octubre24(self):
        valor_esperado = "Usted tiene 18 años"
        valor_actual = evaluar(24, 10, 2005)
        self.assertEqual(valor_esperado, valor_actual)
def test2009Mayo16(self):
        valor_esperado = "Usted tiene 14 años"
        valor_actual = evaluar(16, 5, 2009)
        self.assertEqual(valor_esperado, valor_actual)
def test1992Noviembre5(self):
        valor_esperado = "Usted tiene 31 años"
        valor_actual = evaluar(5, 11, 1992)
        self.assertEqual(valor_esperado, valor_actual)
def test1991Octubre29(self):
        valor_esperado = "Usted tiene 32 años"
        valor_actual = evaluar(29, 10, 1991)
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
