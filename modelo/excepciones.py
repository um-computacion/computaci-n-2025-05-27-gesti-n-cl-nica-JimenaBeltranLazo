#Excepciones Personalizadas

class PacienteNoEncontradoException(Exception):
    "Se lanza cuando un paciente no está registrado en el sistema."
    pass

class MedicoNoDisponibleException(Exception):
    "Se lanza cuando el médico no atiende cierto día o especialidad específica."
    pass

class TurnoOcupadoException(Exception):
    "Se lanza cuando ya existe un turno para el mismo médico, fecha y hora."
    pass

class RecetaInvalidaException(Exception):
    "Se lanza cuando la receta no puede crearse/emitirse. Por ejemplo si la lista está sin medicamentos o vacía."
    pass