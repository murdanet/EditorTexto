from tkinter import *  # Importamos todas las funciones y clases del módulo tkinter para crear la interfaz gráfica
from tokenize import String  # Importamos String del módulo tokenize, aunque no es necesario en este contexto
from tkinter import \
    filedialog as FileDialog  # Importamos el módulo filedialog con el alias FileDialog para facilitar la selección de archivos
from io import open  # Importamos open para trabajar con archivos

# Variable global que almacenará la ruta del archivo abierto o guardado
ruta = ""  # Se utilizará para almacenar la ruta de un fichero


# Función para crear un nuevo archivo
def nuevo():
    global ruta  # Declaramos que la variable ruta es global
    mensaje.set("Nuevo fichero")  # Cambiamos el mensaje en la interfaz
    ruta = ""  # Reseteamos la ruta del archivo
    texto.delete(1.0, "end")  # Borramos el contenido del área de texto
    root.title(ruta + " - Editor de texto")  # Actualizamos el título de la ventana


# Función para abrir un archivo de texto
def abrir():
    global ruta  # Declaramos que la variable ruta es global
    mensaje.set("Abrir fichero")  # Cambiamos el mensaje en la interfaz
    ruta = FileDialog.askopenfilename(
        initialdir='.',  # Carpeta inicial
        filetype=(("Ficheros de texto", "*.txt"),),  # Filtramos solo los archivos de texto
        title="Abrir un fichero de texto"  # Título de la ventana emergente de selección de archivos
    )

    if ruta != "":  # Si se seleccionó un archivo (ruta no vacía)
        fichero = open(ruta, 'r')  # Abrimos el archivo en modo lectura
        contenido = fichero.read()  # Leemos el contenido del archivo
        texto.delete(1.0, 'end')  # Borramos cualquier contenido previo en el área de texto
        texto.insert('insert', contenido)  # Insertamos el contenido del archivo en el área de texto
        fichero.close()  # Cerramos el archivo
        root.title(ruta + " - Editor de texto")  # Actualizamos el título de la ventana


# Función para guardar un archivo
def guardar():
    global ruta  # Declaramos que la variable ruta es global
    mensaje.set("Guardar fichero")  # Cambiamos el mensaje en la interfaz

    if ruta != "":  # Si ya existe una ruta (archivo previamente abierto o guardado)
        contenido = texto.get(1.0,
                              'end-1c')  # Obtenemos el contenido del área de texto sin el último carácter de salto de línea
        fichero = open(ruta, 'w+')  # Abrimos el archivo en modo escritura
        fichero.write(contenido)  # Escribimos el contenido en el archivo
        fichero.close()  # Cerramos el archivo
        mensaje.set("El fichero se ha guardado correctamente")  # Actualizamos el mensaje
    else:
        guardar_como()  # Si no hay ruta (archivo nuevo), llamamos a guardar_como para guardar en una nueva ubicación


# Función para guardar un archivo nuevo o con un nombre diferente
def guardar_como():
    global ruta  # Declaramos que la variable ruta es global
    mensaje.set("Guardar fichero como")  # Cambiamos el mensaje en la interfaz
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w",
                                       defaultextension=".txt")  # Mostramos el cuadro de diálogo para guardar
    if fichero is not None:  # Si se seleccionó una ubicación para guardar
        ruta = fichero.name  # Guardamos la ruta seleccionada
        contenido = texto.get(1.0, 'end-1c')  # Obtenemos el contenido del área de texto
        fichero = open(ruta, 'w+')  # Abrimos el archivo en modo escritura
        fichero.write(contenido)  # Escribimos el contenido en el archivo
        fichero.close()  # Cerramos el archivo
        mensaje.set("El fichero se ha guardado correctamente")  # Actualizamos el mensaje
    else:
        mensaje.set("Guardado cancelado")  # Si se cancela el guardado, se muestra un mensaje
        ruta = ""  # Se resetea la ruta


# Configuración de la ventana principal
root = Tk()  # Creamos la ventana principal
root.title("Editor de Texto")  # Asignamos un título a la ventana

# Configuración del menú superior
menubar = Menu(root)  # Creamos la barra de menú
filemenu = Menu(menubar, tearoff=0)  # Creamos el menú desplegable "Archivo"
filemenu.add_command(label="Nuevo", command=nuevo)  # Opción para crear un nuevo archivo
filemenu.add_command(label="Abrir", command=abrir)  # Opción para abrir un archivo
filemenu.add_command(label="Guardar", command=guardar)  # Opción para guardar un archivo
filemenu.add_command(label="Guardar como", command=guardar_como)  # Opción para guardar un archivo con otro nombre
filemenu.add_separator()  # Añade una línea separadora en el menú
filemenu.add_command(label="Salir", command=root.quit)  # Opción para salir del editor
menubar.add_cascade(menu=filemenu, label="Archivo")  # Añadimos el menú desplegable a la barra de menú

# Configuración del área de texto central
texto = Text(root)  # Creamos el widget de área de texto
texto.pack(fill="both", expand=1)  # Expandimos el área de texto para llenar la ventana
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))  # Configuramos los márgenes y la fuente

# Configuración del monitor de mensajes inferior
mensaje = StringVar()  # Creamos una variable de tipo String para los mensajes
mensaje.set("Bienvenido a tu editor")  # Mensaje inicial
monitor = Label(root, textvar=mensaje, justify="left")  # Creamos una etiqueta para mostrar el mensaje
monitor.pack(side="left")  # Ubicamos la etiqueta en la parte inferior izquierda

# Asignamos el menú a la ventana
root.config(menu=menubar)

# Bucle principal de la aplicación para que la ventana se mantenga abierta
root.mainloop()
