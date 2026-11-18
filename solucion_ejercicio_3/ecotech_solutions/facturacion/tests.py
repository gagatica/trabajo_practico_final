import unittest
from funciones import calcular_emisiones_carbono

class TestCalculoEmisiones(unittest.TestCase):
    def test_calcular_emisiones_carbono(self):
        consumo_kwh = 100.0
        factor_emision = 0.4        
        resultado_esperado = consumo_kwh * factor_emision
        self.assertEqual(calcular_emisiones_carbono(consumo_kwh), resultado_esperado)

    def test_emisiones_igual_a_cero(self):
        consumo_kwh_igual_a_cero = 0.0
        factor_emision = 0.4
        resultado_esperado = consumo_kwh_igual_a_cero * factor_emision
        self.assertEqual(calcular_emisiones_carbono(consumo_kwh_igual_a_cero), resultado_esperado)

    def test_emisiones_negativas(self):
        consumo_kwh_negativo = -50.0
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(consumo_kwh_negativo)

if __name__ == '__main__':
    unittest.main()