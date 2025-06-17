# Test Clínica

import unittest
from datetime import datetime, timedelta
from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestClinica(unittest.TestCase):
    #Registro y Acceso
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Lucía", "87654321", "07/11/2007")
        self.clinica.agregar_paciente(self.paciente)
        especialidad = Especialidad("Cardiología", ["martes", "jueves"])
        self.medico = Medico("Dr. Gutiérrez", "M377", [especialidad])
        self.clinica.agregar_medico(self.medico)

    def test_agregar_paciente_y_medico_duplicados(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(Paciente("Lucía", "87654321", "07/11/2007"))
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(Medico("Dr. Gutiérrez", "M377"))

    def test_agregar_especialidad_a_medico_no_registrado(self):
        with self.assertRaises(ValueError):
            self.clinica.obtener_medico_por_matricula("M001").agregar_especialidad(
            Especialidad("Dermatología", ["miércoles"])
        )
    
    #Turnos
    def test_agendar_turno_exitoso_y_duplicado(self):
        fecha = self.proximo_dia("jueves")
        self.clinica.agendar_turno("87654321", "M377", "Cardiología", fecha)
        self.assertEqual(len(self.clinica.obtener_turnos()), 1)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("87654321", "M377", "Cardiología", fecha)

    def test_turno_errores(self):
        fecha = self.proximo_dia("jueves")
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("11111111", "M377", "Cardiología", fecha)
        fecha_mal_dia = self.proximo_dia("miércoles")
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("87654321", "M377", "Cardiología", fecha_mal_dia)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("87654321", "M377", "Pediatría", fecha) 
    
    def proximo_dia(self, dia_turno):
        dias = {"lunes": 0, "martes": 1, "miércoles": 2, "jueves": 3, "viernes": 4}
        hoy = datetime.now().weekday()
        objetivo = dias[dia_turno]
        delta = (objetivo - hoy + 7) % 7 or 7
        fecha = datetime.now() + timedelta(days=delta)
        return fecha.replace(hour=11, minute=0, second=0, microsecond=0)
    
    #Recetas e Historias Clínicas
    def test_emitir_receta_exitosa_y_errores(self):
        self.clinica.emitir_receta("87654321", "M377", ["Medicamento1"])
        histclinica = self.clinica.obtener_historia_clinica("87654321")
        self.assertEqual(len(histclinica.obtener_recetas()), 1)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("11111111", "M377", ["Medicamento1"])
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("87654321", "M377", [])
            