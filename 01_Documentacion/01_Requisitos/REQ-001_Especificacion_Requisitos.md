# Especificación de Requisitos de Software (ERS)

**Identificación del CI:** REQ-001  
**Proyecto:** SoftEdu-SCM  
**Versión:** 1.0  
**Estado:** Propuesto / Línea Base  
**Fecha:** 11/09/2026  
**Responsable:** Equipo de Desarrollo SoftEdu  

---

## 1. Historial de Versiones
| Versión | Fecha | Descripción del Cambio | Autor |
| :---: | :---: | :--- | :--- |
| 1.0 | 11/09/2026 | Creación e inicialización del documento de requisitos. | Equipo SoftEdu |

---

## 2. Propósito y Alcance
* **Propósito:** Definir de manera clara y trazable las necesidades funcionales y no funcionales del módulo de gestión académica de SoftEdu.
* **Alcance:** Este documento cubre la gestión básica de estudiantes, matrículas y registro de calificaciones para el sistema SoftEdu-SCM.

---

## 3. Requisitos Funcionales (RF)
* **RF-001:** El sistema debe permitir registrar la información básica de un estudiante (ID, Nombre, Carrera, Estado).
* **RF-002:** El sistema debe permitir consultar la información de un estudiante registrado mediante su ID.
* **RF-003:** El sistema debe registrar inscripciones de materias para estudiantes activos.

---

## 4. Requisitos No Funcionales (RNF)
* **RNF-001:** El código base debe desarrollarse en Python 3.x garantizando legibilidad y modularidad.
* **RNF-002:** La documentación y trazabilidad de cambios deben cumplir con las buenas prácticas de SCM basadas en IEEE 828.

---

## 5. Criterios de Aceptación
1. Todas las funciones de lectura/escritura de estudiantes deben ejecutarse sin errores fatales.
2. Cada requisito expuesto debe tener correspondencia directa en el diseño (DIS-001) y en los casos de prueba (TST-001).

---

> **Nota de Control de Cambios:** Cualquier modificación a este documento posterior a la formalización de la Línea Base Inicial (BL-001) deberá solicitarse y aprobarse mediante el procedimiento formal de Control de Cambios del proyecto.