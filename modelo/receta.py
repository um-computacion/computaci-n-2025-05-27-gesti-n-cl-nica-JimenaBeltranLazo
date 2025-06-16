#Clase Receta

from .paciente import Paciente
from .medico import Medico
from .excepciones import RecetaInvalidaException
from datetime import datetime

class Receta:
    #Atributos Privados
    def __init__(self, paciente, medico, medicamentos: list[str]):
        #Validaciones
        if not paciente:
            raise ValueError("Error. El paciente no puede ser nulo.")
        if not isinstance(paciente, Paciente):
            raise ValueError("Error. El paciente no es válido.")
        if not medico:
            raise ValueError("Error. El médico no puede ser nulo.")
        if not isinstance(medico, Medico):
            raise ValueError("Error. El médico no es válido.")
        if not medicamentos or not isinstance(medicamentos, list):
            raise RecetaInvalidaException("Error. Debe indicarse al menos un medicamento.")
        if not all(isinstance(med, str) and med.strip() for med in medicamentos):
            raise RecetaInvalidaException("Error. Los medicamentos deben ser nombres válidos y no nulos.")

        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()
    
    #Representación
    def __str__(self) -> str:
        meds = ", ".join(self.__medicamentos)
        return (
            f"Receta (Paciente {self.__paciente})\n"
            f"Médico: {self.__medico}\n"
            f"Medicamento/s: [{meds}]\n"
            f"Fecha: {self.__fecha.strftime('%d/%m/%Y')}"
        )