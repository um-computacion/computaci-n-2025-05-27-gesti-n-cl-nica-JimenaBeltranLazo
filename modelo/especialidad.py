#Clase Especialidad

class Especialidad:
    #Atributos Privados
    def __init__(self, tipo: str, dias: list[str]):
        #Validaciones
        if not tipo:
            raise ValueError("Error. El nombre de la especialidad es obligatorio.")
        if not dias:
            raise ValueError("Error. Se requiere al menos un día de atención.")
        
        self.__dias = []        
        for dia in dias:
            if not isinstance(dia, str):
                raise ValueError("Error. Los días deben indicarse como texto.")
            dia_lower = dia.strip().lower()
            if dia_lower not in {"lunes", "martes", "miércoles", "jueves", "viernes", "sábado"}:
                raise ValueError(f"Error, '{dia}' no es un día permitido.")
            self.__dias.append(dia_lower)

        self.__tipo = tipo

    
    #Métodos
    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        if not isinstance(dia, str) or not dia:
            return False
        return dia.strip().lower() in self.__dias
    
    #Representación
    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"