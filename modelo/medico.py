#Clase Médico

from modelo.especialidad import Especialidad

class Medico:
    #Atributos Privados
    def __init__(self, nombre: str, matricula: str, especialidades=None):
        #Validaciones
        if not nombre or not matricula:
            raise ValueError("Error. Nombre y matrícula son datos obligatorios.")
        if not matricula.startswith("M") or not matricula[1:].isdigit():
            raise ValueError("Error. La matrícula debe empezar con 'M' y seguir con números, respetando el formato [M000].")
        
        self.__especialidades = []        
        if especialidades:
            for esp in especialidades:
                if not isinstance(esp, Especialidad):
                    raise ValueError("Error. La especialidad no es válida.")
                if any(existente.obtener_especialidad().lower() == esp.obtener_especialidad().lower() for existente in self.__especialidades):
                    raise ValueError(f"Error. El médico ya tiene la especialidad: {esp.obtener_especialidad()}.")
                self.__especialidades.append(esp)

        self.__nombre = nombre
        self.__matricula = matricula


    #Métodos
    def agregar_especialidad(self, especialidad: Especialidad):
        if not isinstance(especialidad, Especialidad):
            raise ValueError("Error. La especialidad no es válida.")
        if any(existente.obtener_especialidad().lower() == especialidad.obtener_especialidad().lower() for existente in self.__especialidades):
            raise ValueError(f"Error. El médico ya tiene la especialidad: {especialidad.obtener_especialidad()}.")
        self.__especialidades.append(especialidad)
        
    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        dia = dia.lower()
        for esp in self.__especialidades:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None
    
    #Representación
    def __str__(self) -> str:
        especialidades_str = ", ".join(str(esp) for esp in self.__especialidades)
        return f"{self.__nombre}, {self.__matricula}, [{especialidades_str}]"