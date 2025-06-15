#Test Médico

import unittest
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def test_registro_exitoso_sin_especialidad(self):
        medico = Medico("Dr. Pérez", "M000")
        self.assertEqual(medico.obtener_matricula(), "M000")
    
    def test_datos_invalidos_medico(self):
        #Datos Faltantes
        with self.assertRaises(ValueError):
            Medico("", "")
        #Matrícula No Válida
        with self.assertRaises(ValueError):
            Medico("Dr. Pérez", "1ABC")

    def test_agregar_especialidad(self):
        medico = Medico("Dr. Pérez", "M000")
        esp1 = Especialidad("Pediatría", ["lunes", "viernes"])
        medico.agregar_especialidad(esp1)
        self.assertIn("Pediatría", str(medico)) #Representación

    def test_especialidad_duplicada(self):
        medico = Medico("Dr. Pérez", "M000")
        esp1 = Especialidad("Pediatría", ["lunes", "viernes"])
        esp2 = Especialidad("Pediatría", ["martes", "jueves"])
        medico.agregar_especialidad(esp1)
        with self.assertRaises(ValueError):
            medico.agregar_especialidad(esp2)

    def test_obtener_especialidad_para_dia(self):
        esp1 = Especialidad("Pediatría", ["lunes", "viernes"])
        esp2 = Especialidad("Cardiología", ["martes", "jueves"])
        medico = Medico("Dr. Pérez", "M000", [esp1, esp2])
        self.assertEqual(medico.obtener_especialidad_para_dia("martes"), "Cardiología")
        self.assertIsNone(medico.obtener_especialidad_para_dia("miércoles"))

#Prevención de registros duplicados (por matrícula) en test_clinica.py