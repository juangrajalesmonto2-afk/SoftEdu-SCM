# SRC-001 - Gestión de Estudiantes
# Proyecto: SoftEdu
# Versión: 1.1
# Estado: Aprobado para BL-002
# Fecha: 16/09/2026
# Responsable: Equipo SoftEdu
# Responsable del cambio: camiGuarin


class Estudiante:
    def __init__(self, identificacion, nombre_completo, correo_electronico, telefono):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico
        self.telefono = telefono

    def mostrar_informacion(self):
        return {
            "identificacion": self.identificacion,
            "nombre_completo": self.nombre_completo,
            "correo_electronico": self.correo_electronico,
            "telefono": self.telefono
        }


def registrar_estudiante(identificacion, nombre_completo, correo_electronico, telefono):
    estudiante = Estudiante(
        identificacion,
        nombre_completo,
        correo_electronico,
        telefono
    )

    return estudiante  
      