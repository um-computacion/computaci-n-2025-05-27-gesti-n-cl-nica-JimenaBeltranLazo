#Clase Turno

from .paciente import Paciente
from .medico import Medico
from datetime import datetime

class Turno:
    #Atributos Privados
    def __init__(self, paciente, medico, fecha_hora: datetime, especialidad: str):
        #Validación
        if not paciente:
            raise ValueError("Error. El paciente no puede ser nulo.")
        if not isinstance(paciente, Paciente):
            raise ValueError("Error. El paciente no es válido.")
        if not medico:
            raise ValueError("Error. El médico no puede ser nulo.")
        if not isinstance(medico, Medico):
            raise ValueError("Error. El médico no es válido.")
        if not isinstance(fecha_hora, datetime):
            raise ValueError("Error. La fecha y hora deben ser un objeto datetime válido.")
        if fecha_hora < datetime.now():
            raise ValueError("Error. El turno debe ser una fecha futura.")
        if not especialidad or not isinstance(especialidad, str):
            raise ValueError("Error. La especialidad debe ser una cadena no vacía.")

        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad
    
    #Métodos
    def obtener_medico(self):
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora
    
    #Representación
    def __str__(self) -> str:
        return (f"Turno: Paciente {self.__paciente}\n"
                f"Médico: {self.__medico}\n"
                f"Especialidad: {self.__especialidad}\n"
                f"Fecha y Hora: {self.__fecha_hora.strftime('%d/%m/%Y %H:%M:%S')}"
        )