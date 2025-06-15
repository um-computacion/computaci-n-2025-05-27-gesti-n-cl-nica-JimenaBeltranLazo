#Test Turno

import unittest
from modelo.turno import Turno
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from datetime import datetime, timedelta

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Lucía", "87654321", "07/11/2007")
        especialidad = Especialidad("Cardiología", ["jueves"])
        self.medico = Medico("Dr. Gutiérrez", "M377", [especialidad])

    def test_creacion_turno_exitoso(self):
        fecha = datetime.now() + timedelta(days=1)
        turno = Turno(self.paciente, self.medico, fecha, "Cardiología")
        self.assertEqual(turno.obtener_medico().obtener_matricula(), "M377")
        self.assertIn("Cardiología", str(turno)) #Representación

    def test_turno_medico_vacio(self):
        fecha = datetime.now() + timedelta(days=1)
        with self.assertRaises(ValueError):
            Turno(self.paciente, None, fecha, "Cardiología")

    def test_turno_especialidad_vacia(self):
        fecha = datetime.now() + timedelta(days=1)
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, fecha, "")

    def test_turno_en_fecha_pasada(self):
        fecha_pasada = datetime.now() - timedelta(days=1)
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, fecha_pasada, "Cardiología")

#Evitar turnos duplicados en test_clinica.py
#Error si el paciente no existe o médico no disponible en test_clinica.py
#Error si el médico no atiende la especialidad solicitada en test_clinica.py
#Error si el médico no trabaja ese día de la semana en test_clinica.py