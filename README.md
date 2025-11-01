# 📇 Gestor de Contactos (CRUD en Python)

## 🧠 Descripción general

Este proyecto es un **CRUD completo (Create, Read, Update, Delete)** desarrollado en **Python**, que permite administrar una **agenda de contactos** desde la consola.  
El programa almacena los datos en un archivo **JSON**, garantizando la **persistencia de la información** entre ejecuciones.

Su propósito principal es servir como ejemplo práctico para el aprendizaje de **estructuras de datos, manejo de archivos, validación de entradas y funciones modulares** en Python.

---

## ⚙️ ¿Cómo funciona?

El programa funciona mediante un menú interactivo en consola que permite:

1. **Agregar contactos:** solicita nombre, teléfono, correo y categoría (amigo, familiar, compañero de trabajo o conocido).  
2. **Mostrar contactos:** lista todos los contactos almacenados.  
3. **Buscar contactos:** filtra por nombre e imprime todos los resultados coincidentes.  
4. **Editar contactos:** permite actualizar los datos de un contacto con confirmaciones individuales.  
5. **Eliminar contactos:** borra uno o varios registros, con opción de cancelar o continuar el proceso.  
6. **Salir del programa:** guarda automáticamente los cambios realizados en el archivo `contactos.json`.

El archivo JSON se actualiza cada vez que se cierra el programa, manteniendo todos los registros almacenados para la siguiente ejecución.

---

## 🧩 Estructura del archivo JSON

Los datos se guardan en un formato legible y estructurado como este:

```json
[
    {
        "nombre": "Juan Pérez",
        "telefono": "987654321",
        "email": "juan@example.com",
        "categoria": "amigo"
    }
]
```

## 🚀 Ejecución

* Descarga o clona el repositorio.
* Asegúrate de tener instalado Python 3.10 o superior.
* Ejecuta el archivo principal:

```
python contactos.py
```
* Interactúa con el menú desde la consola.

## 💡 Mejoras previstas

Aunque el programa es completamente funcional, existen mejoras planificadas para futuras versiones:

* 🖼️ Agregar interfaz gráfica utilizando la librería Tkinter, para hacerlo más amigable al usuario.
* 😄 Incluir emojis y colores ANSI en consola para mejorar la experiencia visual.
* 🗃️ Reemplazar el archivo JSON por una base de datos relacional, probablemente SQLite o MySQL, para permitir búsquedas y registros más eficientes.
* 💬 Agregar funciones avanzadas, como exportar contactos a CSV, importar datos o filtrar por categoría.

## 🧾 Conclusión

Este proyecto representa un CRUD funcional, modular y persistente, desarrollado desde cero para comprender los fundamentos prácticos de Python.
Además de ser una excelente herramienta de estudio, demuestra un dominio sólido de:

* Control de flujo y estructuras de repetición
* Listas, diccionarios y comprensión de listas
* Manejo de excepciones
* Lectura y escritura de archivos JSON
* Diseño estructurado de funciones

En conjunto, este Gestor de Contactos es un ejemplo claro de cómo aplicar la programación estructurada para crear soluciones simples, eficientes y escalables.

* 📌 Autor: Javier-va32
* 📅 Versión actual: 1.0
* 💻 Lenguaje: Python 3.12
* 📂 Tipo de proyecto: Aplicación de consola – CRUD educativo / portafolio