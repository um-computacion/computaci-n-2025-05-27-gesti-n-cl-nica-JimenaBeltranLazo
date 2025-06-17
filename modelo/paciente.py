#Clase Paciente

from datetime import datetime

class Paciente:
    #Atributos Privados
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        #Validaciones
        if not nombre or not dni or not fecha_nacimiento:
            raise ValueError("Error. Debes completar todos los datos.")
        if not dni.isdigit():
            raise ValueError("Error. El DNI debe contener solo números.")
        
        try:
            fecha_paciente = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Error. La fecha de nacimiento debe respetar el formato dd/mm/aaaa.")
        if fecha_paciente > datetime.now():
            raise ValueError("Error. La fecha de nacimiento no puede ser futura.")
        
        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento

    #Método
    def obtener_dni(self) -> str:
        return self.__dni

    #Representación
    def __str__(self) -> str:
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}"