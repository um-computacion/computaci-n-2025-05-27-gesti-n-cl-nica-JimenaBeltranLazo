#Clase Clínica

from datetime import datetime
from .paciente import Paciente
from .medico import Medico
from .turno import Turno
from .historia_clinica import HistoriaClinica
from .receta import Receta
from .excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class Clinica:
    #Atributos Privados
    def __init__(self):
        self.__pacientes = {} #dict[str, Paciente]
        self.__medicos = {} #dict[str, Medico]
        self.__turnos = [] #list[Turno]
        self.__historias_clinicas = {} #dict[str, HistoriaClinica]
    
    #Métodos
    #Registro y Acceso
    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError(f"Error. El paciente con DNI {dni} ya está registrado.")
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError(f"Error. El médico con matrícula {matricula} ya está registrado.")
        self.__medicos[matricula] = medico

    def obtener_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes.values())
    
    def obtener_medicos(self) -> list[Medico]:
        return list(self.__medicos.values())
    
    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        if matricula not in self.__medicos:
            raise ValueError(f"Error. No existe un médico con matrícula {matricula}.")
        return self.__medicos[matricula]
    
    #Turnos
    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        #Validaciones
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        medico = self.__medicos[matricula]
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)

        turno = Turno(self.__pacientes[dni], medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos.copy()
    
    #Recetas e Historias Clínicas
    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        #Validaciones
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)

        if not medicamentos or any(not med.strip() for med in medicamentos):
            raise RecetaInvalidaException("Error. La receta debe contener al menos un medicamento válido.")

        receta = Receta(self.__pacientes[dni], self.__medicos[matricula], medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]
    
    #Validaciones y Utilidades
    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"Error. Paciente con DNI {dni} no encontrado.")
    
    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos:
            raise ValueError(f"Error. Médico con matrícula {matricula} no encontrado.")
    
    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.__turnos:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException(f"Error. El médico ya tiene un turno para esa fecha y hora.")

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
        return dias[fecha_hora.weekday()]

    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> str | None:
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        esp_disponible = medico.obtener_especialidad_para_dia(dia_semana)
        if esp_disponible is None:
            raise MedicoNoDisponibleException(f"Error. El médico no atiende ningún día {dia_semana}.")
        if esp_disponible.lower() != especialidad_solicitada.lower():
            raise MedicoNoDisponibleException(f"Error. El médico no atiende {especialidad_solicitada} el día {dia_semana}.")
