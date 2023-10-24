# Esta versión contiene Tkinter


########################
# Importaciones
########################

# Tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Cifrados
from cifrados.lista import *
from cifrados.cesar import *
from cifrados.morse import *
from cifrados.signoC import *


#####################
# Creo el root
#####################

# Creo la ventana base
root = tk.Tk()
root.title("CO.DE.  M.C.")

ancho_ventana = 320
alto_ventana = 589

x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2  # toma el valor del ancho de la pantalla, lo divide a la mitad para saber cual es el punto central y para que el punto central de la ventana esté a la mitad de la pantalla le resta la mitad del ancho de la ventana
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")
root.geometry(posicion)

root.resizable(0,0)  # Hace que no se pueda modificar el tamaño, ni del alto, ni del ancho
root.iconbitmap("logo.ico")  # Establece el ícono que tendrá el programa

#########################
# Variables
#########################

# Variable que define si se codifica o decodifica
orden = IntVar()
band_ayuda = IntVar()
tema = IntVar()  # Defino una variable que usaré como bandera para los temas
texto_traducir_var = StringVar()
texto_cambiado_var = StringVar()


#############################
# Creo el mensaje de ayuda
#############################

def ayuda():
    contador = 0
    cifrados = ""
    for c in lista_codigos:
        cifrados += lista_codigos[contador]
        cifrados += ": "
        cifrados += lista_cod_abre[contador]
        cifrados += "   "
        if contador == 1 or contador == 3 or contador == 5:
            cifrados += "\n"
        contador += 1

    messagebox.showinfo("Información", message=f"Este programa fue diseñado para simplificar el uso de cifrados y su aplicación a contraseñas o mensajes seguros.\n \nLos cifrados deberán ser ingresados con una letra clave, estos son: \n \n{cifrados}\n \n Al usar morse será necesario poner un espacio despues de cada palabra y separar las palabras con barras, poniendo también un espacio.\n \nEn caso de tener otras dudas consultar a: ezequiel.signorini@gmail.com")


#########################
# Temas de colores
#########################

blanco = "white"
negro = "black"
gris_claro = "grey94"
gris_medio = "grey30"
gris_oscuro = "grey22"
azul_claro = "DodgerBlue2"
azul_medio = "RoyalBlue3"
rojo_claro = "indian red"
rojo_medio = "red3"

def claro():
    # Cambio el color al root
    root.config(bg=gris_claro)
    
    # Cambio el color a los frames
    frame_traducir.config(bg=gris_claro)
    frame_cambiado.config(bg=gris_claro)
    
    # Cambio el color a los elementos
    etiqueta_txt_traducir.config(bg=gris_claro, fg=negro)
    etiqueta_txt_cambiado.config(bg=gris_claro, fg=negro)
    etiqueta_version.config(bg=gris_claro, fg=negro)
    etiqueta_cifrados.config(bg=gris_claro, fg=negro)

    etiqueta_adv_codes.config(bg=gris_claro, fg=rojo_claro)
    etiqueta_adv_code.config(bg=gris_claro, fg=rojo_claro)
    etiqueta_adv_traducir.config(bg=gris_claro, fg=rojo_claro)

    texto_traducir.config(bg=blanco, fg=negro)
    texto_cambiado.config(bg=blanco, fg=negro)
    code.config(bg=blanco, fg=negro)
    co.config(bg=gris_claro, fg=negro)
    de.config(bg=gris_claro, fg=negro)

    # Cambio el color a los botones
    boton_light.config(bg=azul_claro, fg=blanco)
    boton_dark.config(bg=gris_claro, fg=negro)

    boton_ayuda.config(bg=gris_claro, fg=negro)
    boton_code.config(bg=azul_claro, fg=blanco)

    # Cambio el color del frame
    root.config(bg=gris_claro)
    root.config(bg=gris_claro)
    root.config(bg=gris_claro)
    
    tema.set(1)

def oscuro():
    # Cambio el color al root
    root.config(bg=gris_oscuro)

    # Cambio el color a los frames
    frame_traducir.config(bg=gris_oscuro)
    frame_cambiado.config(bg=gris_oscuro)

    # Cambio el color a los elementos
    etiqueta_txt_traducir.config(bg=gris_oscuro, fg=blanco)
    etiqueta_txt_cambiado.config(bg=gris_oscuro, fg=blanco)
    etiqueta_version.config(bg=gris_oscuro, fg=blanco)
    etiqueta_cifrados.config(bg=gris_oscuro, fg=blanco)

    etiqueta_adv_codes.config(bg=gris_oscuro, fg=rojo_medio)
    etiqueta_adv_code.config(bg=gris_oscuro, fg=rojo_medio)
    etiqueta_adv_traducir.config(bg=gris_oscuro, fg=rojo_medio)

    texto_traducir.config(bg=gris_medio, fg=blanco)
    texto_cambiado.config(bg=gris_medio, fg=blanco)
    code.config(bg=gris_medio, fg=blanco)
    co.config(bg=gris_oscuro, fg=azul_claro)
    de.config(bg=gris_oscuro, fg=azul_claro)

    # Cambio el color a los botones
    boton_light.config(bg=gris_medio, fg=blanco)
    boton_dark.config(bg=azul_medio, fg=blanco)

    boton_ayuda.config(bg=gris_medio, fg=blanco)
    boton_code.config(bg=azul_medio, fg=blanco)

    # Cambio el color del frame
    root.config(bg=gris_oscuro)
    root.config(bg=gris_oscuro)
    root.config(bg=gris_oscuro)
    
    tema.set(2)


########################
# Creo las funciones
########################

def procesar():
    if code.get() == "":
        etiqueta_adv_code.config(text="- Ingrese un cifrado")

        if tema.get() == 1 or tema.get() == 0:  # Se está usando el tema claro o el tema predefinido
            etiqueta_adv_code.config(bg=gris_claro, fg=rojo_claro)
        else:  # Se está usando el tema oscuro
            etiqueta_adv_code.config(bg=gris_oscuro, fg=rojo_medio)
    else:    
        # Analizo el o los cifrados
        codes = StringVar()
        codes_for = ""
        c_no_registrados = 0

        for c in (code.get()).upper():
            if c in lista_cod_abre:
                codes_for += c
            else:
                c_no_registrados += 1
        
        if codes_for != "":
            codes.set(codes_for)
            if c_no_registrados == 0:
                etiqueta_adv_code.config(text="")
            else:
                etiqueta_adv_code.config(text="- Algunos cifrados son incorrectos")
        else:
            etiqueta_adv_code.config(text="- Cifrados incorrectos")

        if tema.get() == 1 or tema.get() == 0:  # Se está usando el tema claro o el tema predefinido
            etiqueta_adv_codes.config(bg=gris_claro, fg=rojo_claro)
        else:  # Se está usando el tema oscuro
            etiqueta_adv_codes.config(bg=gris_oscuro, fg=rojo_medio)



    if orden.get() != 1 and orden.get() != 2:
        etiqueta_adv_codes.config(text="- Elija un valor")

        if tema.get() == 1 or tema.get() == 0:
            etiqueta_adv_codes.config(bg=gris_claro, fg=rojo_claro)
        else:
            etiqueta_adv_codes.config(bg=gris_oscuro, fg=rojo_medio)
    else:
        etiqueta_adv_codes.config(text="")

        if tema.get() == 1 or tema.get() == 0:
            etiqueta_adv_codes.config(bg=gris_claro)
        else:
            etiqueta_adv_codes.config(bg=gris_oscuro)
    
    if texto_traducir.get() == "":  # Se presenta un error en la recepción de lo que posee el Text
        etiqueta_adv_traducir.config(text="- Debe ingresar algo para poderlo cambiar")

        if tema.get() == 1 or tema.get() == 0:
            etiqueta_adv_traducir.config(bg=gris_claro, fg=rojo_claro)
        else:
            etiqueta_adv_traducir.config(bg=gris_oscuro, fg=rojo_medio)
    else:
        etiqueta_adv_traducir.config(text="")

        if tema.get() == 1 or tema.get() == 0:
            etiqueta_adv_codes.config(bg=gris_claro)
        else:
            etiqueta_adv_codes.config(bg=gris_oscuro)


###############################
# Creo el contenido del root
###############################

# Boton para usar el tema claro
boton_light = Button(root, text="claro", bg=azul_claro, fg=blanco, width="7", command=claro)  # FRAME TEMAS
boton_light.place(x=180, y=10)

# Boton para usar el tema oscuro
boton_dark = Button(root, text="Oscuro", width="7", command=oscuro)  # FRAME TEMAS
boton_dark.place(x=240, y=10)


#####################
# CO.DE.
#####################

# Creo la etiqueta
etiqueta_cifrados = Label(root, text="Elija los cifrados", bg=gris_claro)  # FRAME CIFRADO
etiqueta_cifrados.place(x=35, y=70)

# Creo el entry de los cifrados que va a usar
code = Entry(root, width=17)  # FRAME CIFRADO
code.place(x=30, y=90)

# Creo una etiqueta que será cambiada como alerta en caso de ser necesario
etiqueta_adv_code = Label(root, text="", bg=gris_claro, pady=5)  # FRAME CONTENIDO
etiqueta_adv_code.place(x=30, y=110)

# Radiobuttons para elegir si se codifica o decodifica
co = Radiobutton(root, text="Codificar    ", value=1, variable=orden)  # FRAME CIFRADO
co.place(x=180, y=70)

de = Radiobutton(root, text="Decodificar", value=2, variable=orden)  # FRAME CIFRADO
de.place(x=180, y=90)


# Creo una etiqueta que será cambiada como alerta en caso de ser necesario
etiqueta_adv_codes = Label(root, text="", bg=gris_claro, pady=5)  # FRAME CONTENIDO
etiqueta_adv_codes.place(x=180, y=110)


# Creo el frame en donde estará el texto a traducir
frame_traducir = Frame(root)
frame_traducir.place(x=30, y=150)

# Creo la etiqueta de referencia al texto que se traducirá
etiqueta_txt_traducir = Label(frame_traducir, text="Ingrese el texto a cambiar")  # FRAME CONTENIDO
etiqueta_txt_traducir.grid(row=0, column=0)

# Creo el text en donde ingresará el texto a traducir
texto_traducir = Text(frame_traducir, width=30, height=8)  # FRAME CONTENIDO
texto_traducir.grid(row=1, column=0)

scroll_vertical_1 = Scrollbar(frame_traducir, command=texto_traducir.yview)  # FRAME CONTENIDO
texto_traducir.config(yscrollcommand=scroll_vertical_1.set)
scroll_vertical_1.grid(row=1, column=1, sticky=NSEW)

etiqueta_adv_traducir = Label(frame_traducir, text="", pady=5)
etiqueta_adv_traducir.grid(row=2, column=0)


# Creo un frame para el texto cambiado
frame_cambiado = Frame(root)
frame_cambiado.place(x=30, y=350)

# Creo la etiqueta de referencia al texto cambiado
etiqueta_txt_cambiado = Label(frame_cambiado, text="Texto cambiado")  # FRAME CONTENIDO
etiqueta_txt_cambiado.grid(row=0, column=0)

# Creo el text en donde se mostrará el texto cambiado
texto_cambiado = Text(frame_cambiado, width=30, height=8)  # FRAME CONTENIDO
texto_cambiado.grid(row=1, column=0)

scroll_vertical_2 = Scrollbar(frame_cambiado, command=texto_cambiado.yview)  # FRAME CONTENIDO
texto_cambiado.config(yscrollcommand=scroll_vertical_2.set)
scroll_vertical_2.grid(row=1, column=1, sticky=NSEW)


# Creo el boton el cual hará que se codifique el texto
boton_code = Button(root, text="Procesar", bg=azul_claro, fg=blanco, command=procesar)  # FRAME CONTENIDO
boton_code.place(x=130, y=520)


########################
# Finalizo el programa
########################

etiqueta_version = Label(root, text="Versión 1.5", bg=gris_claro)  # FRAME AY VER
etiqueta_version.place(x=10, y=555)

boton_ayuda = Button(root, text="Ayuda", bg=gris_claro, fg=negro, command=ayuda)  # FRAME AY VER
boton_ayuda.place(x=260, y=550)

root.mainloop()