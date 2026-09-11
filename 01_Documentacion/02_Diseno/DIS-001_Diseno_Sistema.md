# Documento de Diseño del Sistema (DDS)

**Identificación del CI:** DIS-001  
**Proyecto:** SoftEdu-SCM  
**Versión:** 1.0  
**Estado:** Propuesto / Línea Base  
**Fecha:** 11/09/2026  
**Responsable:** Equipo de Desarrollo SoftEdu  

---

## 1. Historial de Versiones
| Versión | Fecha | Descripción del Cambio | Autor |
| :---: | :---: | :--- | :--- |
| 1.0 | 11/09/2026 | Definición inicial de la arquitectura y componentes del sistema. | Equipo SoftEdu |

---

## 2. Descripción General de la Arquitectura
El sistema `SoftEdu-SCM` sigue una arquitectura modular en Python orientada a objetos para la gestión de estudiantes.

---

## 3. Módulos y Componentes Principales
* **Componente `Estudiante`:** Representa la entidad de datos (ID, Nombre, Carrera, Estado).
* **Componente `GestionEstudiantes`:** Maneja la lógica de negocio (Registrar, Buscar, Listar).

---

## 4. Trazabilidad con Requisitos
* **REQ-001 (RF-001):** Implementado en la clase `Estudiante` y el método `registrar_estudiante()`.
* **REQ-001 (RF-002):** Implementado en el método `buscar_estudiante()`.