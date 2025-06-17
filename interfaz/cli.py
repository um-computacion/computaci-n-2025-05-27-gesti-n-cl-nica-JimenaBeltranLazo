# Interfaz de Consola (CLI)

from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from datetime import datetime
from modelo.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class CLI:
    def __init__(self):
        self.clinica = Clinica()
    
    #Flujo Principal
    def mostrar_menu(self):
        while True:
            print("\n--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Agregar especialidad a médico")
            print("5) Emitir receta")
            print("6) Ver historia clínica")
            print("7) Ver todos los turnos")
            print("8) Ver todos los pacientes")
            print("9) Ver todos los médicos")
            print("0) Salir")

            opcion = input("Por favor. Seleccione una opción: ")

            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.agregar_medico()
            elif opcion == "3":
                self.agendar_turno()
            elif opcion == "4":
                self.agregar_especialidad()
            elif opcion == "5":
                self.emitir_receta()
            elif opcion == "6":
                self.ver_historia_clinica()
            elif opcion == "7":
                self.ver_turnos()
            elif opcion == "8":
                self.ver_pacientes()
            elif opcion == "9":
                self.ver_medicos()
            elif opcion == "0":
                print("¡Gracias por usar el sistema! ¡Adios!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
    
    #Operaciones Principales
    def agregar_paciente(self):
        try:
            nombre = input("Ingrese el nombre del paciente: ")
            dni = input("DNI del paciente: ")
            fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
            paciente = Paciente(nombre, dni, fecha_nacimiento)
            self.clinica.agregar_paciente(paciente)
            print("Paciente registrado exitosamente.")
        except ValueError as error:
            print(f"Error: {error}")

    def agregar_medico(self):
        try:
            nombre = input("Ingerese el nombre del médico: ")
            matricula = input("Matrícula del médico: ")
            medico = Medico(nombre, matricula)
            self.clinica.agregar_medico(medico)
            print("Médico registrado exitosamente.")
        except ValueError as error:
            print(f"Error: {error}")

    def agendar_turno(self):
        try:
            dni = input("Ingrese DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            especialidad = input("Especialidad: ")
            fecha_str = input("Fecha y hora del turno (dd/mm/aaaa HH:MM): ")
            fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M:%S")
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("Turno agendado exitosamente.")
        except (ValueError, PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException) as error:
            print(f"Error: {error}")

    def agregar_especialidad(self):
        try:
            matricula = input("Ingresar Matrícula del médico: ")
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            tipo = input("Nombre de la especialidad: ")
            dias = input("Días de atención (separados por coma): ").split(",")
            dias = [d.strip().lower() for d in dias]
            especialidad = Especialidad(tipo, dias)
            medico.agregar_especialidad(especialidad)
            print("Especialidad agregada exitosamente.")
        except ValueError as error:
            print(f"Error: {error}")

    def emitir_receta(self):
        try:
            dni = input("Ingresar DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            medicamentos = input("Medicamentos (separados por coma): ").split(",")
            medicamentos = [meds.strip() for meds in medicamentos]
            self.clinica.emitir_receta(dni, matricula, medicamentos)
            print("Receta emitida exitosamente.")
        except (ValueError, PacienteNoEncontradoException, RecetaInvalidaException) as error:
            print(f"Error: {error}")

    def ver_historia_clinica(self):
        try:
            dni = input("Ingresar DNI del paciente: ")
            histclinica = self.clinica.obtener_historia_clinica(dni)
            print(histclinica)
        except PacienteNoEncontradoException as error:
            print(f"Error: {error}")

    def ver_turnos(self):
        turnos = self.clinica.obtener_turnos()
        if not turnos:
            print("No hay turnos registrados.")
        else:
            for turno in turnos:
                print(turno)

    def ver_pacientes(self):
        pacientes = self.clinica.obtener_pacientes()
        if not pacientes:
            print("No hay pacientes registrados.")
        else:
            for paciente in pacientes:
                print(paciente)

    def ver_medicos(self):
        medicos = self.clinica.obtener_medicos()
        if not medicos:
            print("No hay médicos registrados.")
        else:
            for medico in medicos:
                print(medico)
