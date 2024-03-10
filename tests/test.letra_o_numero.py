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

class TestLetraONumero(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es número"
        valor_actual = evaluar('9')
        self.assertEqual(valor_esperado, valor_actual)
class TestLetraONumero1(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es número"
        valor_actual = evaluar('0')
        self.assertEqual(valor_esperado, valor_actual)
class TestLetraONumero2(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es número"
        valor_actual = evaluar('4')
        self.assertEqual(valor_esperado, valor_actual)
class TestLetraONumero3(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es letra mayúscula"
        valor_actual = evaluar('C')
        self.assertEqual(valor_esperado, valor_actual)   
class TestLetraONumero4(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es letra mayúscula"
        valor_actual = evaluar('A')
        self.assertEqual(valor_esperado, valor_actual)
class TestLetraONumero5(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es letra mayúscula"
        valor_actual = evaluar('Z')
        self.assertEqual(valor_esperado, valor_actual)  
class TestLetraONumero6(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es letra minúscula"
        valor_actual = evaluar('c')
        self.assertEqual(valor_esperado, valor_actual) 
class TestLetraONumero7(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es letra minúscula"
        valor_actual = evaluar('f')
        self.assertEqual(valor_esperado, valor_actual) 
class TestLetraONumero8(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es letra minúscula"
        valor_actual = evaluar('o')
        self.assertEqual(valor_esperado, valor_actual)         

if __name__ == '__main__':
    unittest.main()