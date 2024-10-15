# Editor de Texto en Python

Este programa es un editor de texto básico hecho en Python usando la librería **Tkinter** para la interfaz gráfica.

## Funciones principales:

### 1. Nuevo:
   - Limpia el área de texto y permite al usuario comenzar a escribir un nuevo archivo.

### 2. Abrir:
   - Permite al usuario abrir un archivo de texto (.txt) existente y cargar su contenido en el área de texto.

### 3. Guardar:
   - Si el archivo ya ha sido guardado antes (tiene una ruta asignada), guarda los cambios en ese mismo archivo.
   - Si el archivo es nuevo (sin ruta asignada), llama a la función **Guardar como** para que el usuario elija dónde guardarlo.

### 4. Guardar como:
   - Abre una ventana para que el usuario elija el nombre y la ubicación donde desea guardar el archivo de texto.

### 5. Salir:
   - Cierra la aplicación.

## Estructura del programa:

- Se utiliza un área de texto principal donde el usuario puede escribir o modificar el contenido.
- En la parte inferior hay una barra que muestra mensajes sobre las acciones realizadas (como abrir, guardar, etc.).
- El menú superior contiene todas las opciones mencionadas: **Nuevo**, **Abrir**, **Guardar**, **Guardar como**, y **Salir**.

