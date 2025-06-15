#Test Receta

import unittest
from modelo.receta import Receta
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import RecetaInvalidaException

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Lucía", "87654321", "07/11/2007")
        especialidad = Especialidad("Cardiología", ["jueves"])
        self.medico = Medico("Dr. Gutiérrez", "M377", [especialidad])

    def test_creacion_receta_exitosa(self):
        receta = Receta(self.paciente, self.medico, ["Ibuprofeno", "Corticoides"])
        self.assertIn("Ibuprofeno", str(receta)) #Representación
        self.assertIn("Corticoides", str(receta)) #Representación

    def test_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.paciente, self.medico, [])
    def test_receta_con_medicamento_vacio(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.paciente, self.medico, ["", ""])
    
    def test_receta_paciente_vacio(self):
        with self.assertRaises(ValueError):
            Receta(None, self.medico, ["Corticoides"])

    def test_receta_medico_vacio(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, None, ["Corticoides"])