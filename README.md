<pre>

	<p align=center>

Tecnológico Nacional de México
Instituto Tecnológico de Tijuana

Departamento de Sistemas y Computación
Ingeniería en Sistemas Computacionales

Semestre:
Agosto - Diciembre 2024

Materia:
Patrones de Diseño

Docente:
M.C. Rene Solis Reyes 

Bloque:
2

Título del trabajo:
 Cognify

Estudiante:
Sanchez Rosas Karime Lizbeth
Paez Beltra David

	</p>

</pre>


## Objetivos del Proyecto

Rehabilitación Eficiente: Transformar las experiencias de los delincuentes mediante recuerdos artificiales diseñados para fomentar la empatía y el arrepentimiento.
Reducción de Costos: Minimizar los costos asociados con el encarcelamiento tradicional, como la construcción y mantenimiento de prisiones.
Reinserción Social: Permitir una reintegración rápida y efectiva de los criminales rehabilitados a la sociedad.
Innovación en Justicia Penal: Proporcionar una alternativa ética y tecnológica al castigo convencional, centrada en el aprendizaje y la rehabilitación.

## Diagrama UML
```mermaid
classDiagram
    class CrimeType {
        - tipo: String
        + describir(): void
    }

    class Criminal {
        - nombre: String
        - edad: int
        - tipo_crimen: CrimeType
        + cometerCrimen(): void
        + recordarCrimen(): void
    }

    class Memory {
        - contenido: String
        - fecha: Date
        + recuperar(): void
        + personalizar(): void
    }

    class Configuracion {
        - instancia: Configuracion
        - parametros: Map<String, String>
        + getInstancia(): Configuracion
        + cargarParametros(): void
    }

    class Simulation {
        - configuracion: Configuracion
        + iniciar(): void
        + detener(): void
    }

    class MemoryFactory {
        + crearMemory(tipoCrimen: CrimeType): Memory
    }

    class MemoryBuilder {
        - memory: Memory
        + conContenido(contenido: String): MemoryBuilder
        + conFecha(fecha: Date): MemoryBuilder
        + build(): Memory
    }

    class Controller {
        - vista: Vista
        - modelo: Modelo
        + procesarEntrada(): void
        + actualizarVista(): void
    }

    class Vista {
        + mostrarOpciones(): void
        + recibirEntrada(): void
    }

    Criminal --> CrimeType : "tipo_crimen"
    Memory --> CrimeType : "asociado a"
    Simulation --> Configuracion : "configuracion"
    MemoryBuilder --> Memory : "construye"
    Controller --> Vista : "interactúa con"
    Controller --> Modelo : "gestiona"
    MemoryFactory --> Memory : "crea"

```

## Análisis del impacto social y técnico del sistema.



## Video LOOM
