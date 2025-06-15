#Test Historia Clínica

import unittest
from modelo.historia_clinica import HistoriaClinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.turno import Turno
from modelo.receta import Receta     
from datetime import datetime, timedelta

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Lucía", "87654321", "07/11/2007")
        self.histclinica = HistoriaClinica(self.paciente)
        self.medico = Medico("Dr. Gutiérrez", "M377", [Especialidad("Cardiología", ["jueves"])])

    def test_agregar_y_obtener_turno(self):
        turno = Turno(self.paciente, self.medico, datetime.now() + timedelta(days=1), "Cardiología")
        self.histclinica.agregar_turno(turno)
        turnos = self.histclinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), "M377")

    def test_agregar_y_obtener_receta(self):
        receta = Receta(self.paciente, self.medico, ["Medicamento1"])
        self.histclinica.agregar_receta(receta)
        recetas = self.histclinica.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertIn("Medicamento1", str(recetas[0]))
        