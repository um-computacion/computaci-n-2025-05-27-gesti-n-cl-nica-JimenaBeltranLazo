#Test Paciente

import unittest
from modelo.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_registro_exitoso(self):
        paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertIn("Juan Pérez", str(paciente)) #Representación

    def test_datos_invalidos(self):
        #Datos Faltantes
        with self.assertRaises(ValueError):
            Paciente("", "", "")
        #DNI No Válido
        with self.assertRaises(ValueError):
            Paciente("Juan Pérez", "ABCDEFGH", "12/12/2000")
        #Fecha Nacimiento No Válida
        with self.assertRaises(ValueError):
            Paciente("Juan Pérez", "12345678", "12-12-2000")

#Prevención de registros duplicados (por DNI) en test_clinica.py