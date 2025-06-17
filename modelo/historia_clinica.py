#Clase Historia Clínica

from .paciente import Paciente
from .turno import Turno
from .receta import Receta
from typing import List

class HistoriaClinica:
    #Atributos Privados
    def __init__(self, paciente: Paciente):
        if not isinstance(paciente, Paciente):
            raise ValueError("Error. El paciente no es válido.")
        
        self.__paciente = paciente
        self.__turnos: List = []
        self.__recetas: List = []
    
    #Métodos
    def agregar_turno(self, turno):
        if not isinstance(turno, Turno):
            raise ValueError("Error. El turno no es válido.")
        self.__turnos.append(turno)

    def agregar_receta(self, receta):
        if not isinstance(receta, Receta):
            raise ValueError("Error. La receta no es válida.")
        self.__recetas.append(receta)

    def obtener_turnos(self) -> List:
        return list(self.__turnos)

    def obtener_recetas(self) -> List:
        return list(self.__recetas)
    
    #Representación
    def __str__(self) -> str:
        turnos_str = "\n".join(str(turno) for turno in self.__turnos) or "No hay turnos registrados."
        recetas_str = "\n".join(str(receta) for receta in self.__recetas) or "No hay recetas registradas."
        return (
            f"---Historia Clínica---\n"
            f"{self.__paciente}\n"
            f"\n"
            f"--Turno/s--\n"
            f"{turnos_str}\n"
            f"\n"
            f"--Receta/s--\n"
            f"{recetas_str}\n"
            f"\n"
        )