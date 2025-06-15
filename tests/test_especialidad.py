#Test Especialidad 

import unittest
from modelo.especialidad import Especialidad


class TestEspecialidad(unittest.TestCase):
    def test_creacion_exitosa(self):
        especialidad = Especialidad("Pediatría", ["lunes", "viernes"])
        self.assertTrue(especialidad.verificar_dia("lunes"))
        self.assertTrue(especialidad.verificar_dia("LUNES"))
        self.assertFalse(especialidad.verificar_dia("martes"))
        salida = str(especialidad)
        self.assertIn("Pediatría", salida) #Representación
        self.assertIn("lunes", salida) #Representación
        self.assertIn("viernes", salida) #Representación

    def test_obtener_especialidad(self):
        especialidad = Especialidad("Pediatría", ["lunes"])
        self.assertEqual(especialidad.obtener_especialidad(), "Pediatría")

    def test_lista_dias_vacia(self):
        with self.assertRaises(ValueError):
            Especialidad("Cardiología", [])

    def test_dia_invalido(self):
        with self.assertRaises(ValueError):
            Especialidad("Cardiología", ["dominguez"])

#Evitar duplicados de especialidad en el mismo médico en test_medico.py
#Error si se intenta agregar especialidad a un médico no registrado en test_clinica.py