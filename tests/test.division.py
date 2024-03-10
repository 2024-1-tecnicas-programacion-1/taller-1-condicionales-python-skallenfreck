import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.division import evaluar

class TestDivision(unittest.TestCase):
    def testDivisionExacta(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 2\n" \
                         "Residuo: 4"
        valor_actual = evaluar(14, 5)
        self.assertEqual(valor_esperado, valor_actual)
class TestDivision1(unittest.TestCase):
    def testDivisionExacta1(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 10\n" \
                         "Residuo: 0"
        valor_actual = evaluar(100, 10)
        self.assertEqual(valor_esperado, valor_actual)
class TestDivision2(unittest.TestCase):
    def testDivisionExacta2(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 2\n" \
                         "Residuo: 0"
        valor_actual = evaluar(80, 40)
        self.assertEqual(valor_esperado, valor_actual)    
class TestDivision3(unittest.TestCase):
    def testDivisionExacta(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 3\n" \
                         "Residuo: 0"
        valor_actual = evaluar(27, 9)
        self.assertEqual(valor_esperado, valor_actual)
class TestDivision4(unittest.TestCase):
    def testDivisionExacta(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 3\n" \
                         "Residuo: 1"
        valor_actual = evaluar(10, 3)
        self.assertEqual(valor_esperado, valor_actual)  
class TestDivision5(unittest.TestCase):
    def testDivisionExacta(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 22\n" \
                         "Residuo: 2"
        valor_actual = evaluar(90, 4)
        self.assertEqual(valor_esperado, valor_actual)  
    

if __name__ == '__main__':
    unittest.main()

