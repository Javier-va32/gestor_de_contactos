
import json

def guardar_contactos(contactos):
    with open("contactos.json", "w", encoding="utf-8") as archivo:
        json.dump(contactos, archivo, ensure_ascii=False, indent=4)
    print("Contactos guardados correctamente")

def cargar_contactos():
    try:
        with open("contactos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("No se encontró el archivo de contactos. Se creará uno nuevo.")
        return [] #Para evitar errores en caso de no haber un archivo.json

def diccionario(nombre, telefono, email, categoria):
    persona = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "categoria": categoria
    }
    return persona

def validacion_contactos():
    #Script para manejar errores en ingresar_contactos()
    while True:
        try:
            opcion = int(input(">"))
            if 1<= opcion <=4:
                break
            else:
                print("Error: solo puede ingresar números del 1 al 4")
        except ValueError:
            print("Error: Solo puede ingresar números enteros")
    return opcion

def ingresar_contactos():
    # Se crean la lista para guardar los datos
    contactos = []
    #Tupla donde se almacenan las categorías. 
    categorias = ("amigo", "familiar", "compañero de trabajo", "conocido")

    while True:
        nombre = input("Ingrese el nombre \n>")
        telefono = input("Ingrese el número telefónico \n>")
        email = input("Ingrese el correo electrónico \n>")

        print("Seleccione la categoría del usuario.")
        for i, categoria in enumerate(categorias, start=1):
            print(f"{i}. {categoria}")
        
        opcion = validacion_contactos()
        categoria = categorias[opcion - 1]
        persona = diccionario(nombre, telefono, email, categoria)
        contactos.append(persona)
        fin_datos = input("¿Agregar un nuevo contacto? (S/N) \n>").lower()
        if fin_datos == "n":
            break
    return contactos

def buscar_contacto(contactos):
    nombre_buscar = input("Ingrese el nombre del contacto que desea buscar> \n>").lower()
    #Se usa comprensión de listas para devolver más de un contacto con el mismo nombre. 
    contacto_encontrado = [p for p in contactos if p['nombre'].lower() == nombre_buscar]

    if contacto_encontrado: 
        print("\n=== Resultados encontrados ===")
        for persona in contacto_encontrado: #Se recorre una nueva lista con los contactos encontrados.
            print (f"Nombre: {persona['nombre']} ({persona['categoria']}), Teléfono: {persona['telefono']}, Email: {persona['email']}")
    else:
        print("Contacto no encontrado")

def eliminar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a eliminar: \n>").lower()
    #Se usa comprensión de listas para generar una lista con las coincidencias. 
    encontrados = [p for p in contactos if p["nombre"].lower() == nombre]

    if not encontrados:
        print("No se encontró el contacto.")
        return

    for persona in encontrados[:]: # recorre copia, modifica original. Eso evita fallos al borrar elementos
        confirmar = input(f"¿Desea eliminar a {persona['nombre']} de sus contactos? (S/N) \n>").lower()
        if confirmar == "s":
            contactos.remove(persona)
            print(f"Contacto '{persona['nombre']}' eliminado correctamente.")
        else:
            print(f"Contacto '{persona['nombre']}' no fue eliminado.")

        # preguntar si desea continuar con los demás
        continuar = input("¿Desea seguir eliminando otros contactos? (S/N): \n>").lower()
        if continuar == "n":
            print("Finalizando proceso de eliminación.")
            break

def editar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a editar: ").lower()
    for persona in contactos:
        if persona["nombre"].lower() == nombre:
            print("\nDeje en blanco cualquier campo que no desee cambiar.\n")

            # === Nombre ===
            nuevo_nombre = input(f"Nombre actual: {persona['nombre']}\nNuevo nombre: ")
            if nuevo_nombre:
                confirmar = input(f"Confirmar cambio de nombre a '{nuevo_nombre}'? (S/N): ").lower()
                if confirmar == "s":
                    persona["nombre"] = nuevo_nombre

            # === Teléfono ===
            nuevo_telefono = input(f"\nTeléfono actual: {persona['telefono']}\nNuevo teléfono: ")
            if nuevo_telefono:
                confirmar = input(f"Confirmar cambio de teléfono a '{nuevo_telefono}'? (S/N): ").lower()
                if confirmar == "s":
                    persona["telefono"] = nuevo_telefono

            # === Email ===
            while True:
                nuevo_email = input(f"\nEmail actual: {persona['email']}\nNuevo email: ")
                if not nuevo_email:  # vacío → no cambia
                    break
                elif "@" in nuevo_email and "." in nuevo_email:
                    confirmar = input(f"Confirmar cambio de email a '{nuevo_email}'? (S/N): ").lower()
                    if confirmar == "s":
                        persona["email"] = nuevo_email
                    break
                else:
                    print("Error: ingrese un correo válido (ejemplo@dominio.com).")

            # === Categoría ===
            while True:
                nueva_categoria = input(f"\nCategoría actual: {persona['categoria']}\nNueva categoría: ").lower()
                if not nueva_categoria:
                    break
                elif nueva_categoria in ("amigo", "familiar", "compañero de trabajo", "conocido"):
                    confirmar = input(f"Confirmar cambio de categoría a '{nueva_categoria}'? (S/N): ").lower()
                    if confirmar == "s":
                        persona["categoria"] = nueva_categoria
                    break
                else:
                    print("Error: categoría inválida. Use una de las siguientes: amigo, familiar, compañero de trabajo o conocido.")

            print("\n Contacto actualizado correctamente.")
            return

    print("No se encontró el contacto.")


def ver_lista(contactos):
    print("=== Mostrar resultados ===")
    for i, persona in enumerate(contactos, start=1):
        print (f"{i}. Nombre: {persona['nombre']} ({persona['categoria']}), Teléfono: {persona['telefono']}, Email: {persona['email']}")

def menu(contactos):
    while True:
        try:
            print("===Menú de usuario=== \n")
            print("1. Agregar contacto")
            print("2. Mostrar contactos")
            print("3. Buscar contacto")
            print("4. Eliminar contacto")
            print("5. Editar contacto")
            print("6. Salir")

            opcion = int(input("Ingrese la opción deseada \n>"))
            if 1<= opcion <=6:
                match opcion:
                    case 1:
                        nuevos = ingresar_contactos()
                        contactos.extend(nuevos)
                    case 2:
                        if contactos:
                            ver_lista(contactos)
                        else:
                            print("No hay contactos registrados aún.")
                    case 3:
                        if contactos:
                            buscar_contacto(contactos)
                        else:
                            print("No hay contactos para buscar.")
                    case 4:
                        if contactos:
                            eliminar_contacto(contactos)
                        else:
                            print("No hay contactos para eliminar.")
                    case 5:
                        if contactos:
                            editar_contacto(contactos)
                        else:
                            print("No hay contactos para editar.")
                    case 6:
                        print("Saliendo del programa. ¡Hasta pronto!")
                        break
            else:
                print("Error: Ingrese un número entre 1 y 6")
                continue
        except ValueError:
            print("Error: Ingrese una opción válida.")

def main():
    contactos = cargar_contactos()
    menu(contactos)
    guardar_contactos(contactos)

if __name__ == "__main__":
    main()
