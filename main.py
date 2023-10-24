########################
# Importaciones
########################

# Tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Cifrados
from lista import *
from cifrados import *


#####################
# Creo el root
#####################

# Creo la ventana base
root = tk.Tk()
root.title("CODE  MC")

root.resizable(0,0)  # Hace que no se pueda modificar el tamaño, ni del alto, ni del ancho
try:
    root.iconbitmap("logo.ico")  # Establece el ícono que tendrá el programa
except:
    pass


#########################
# Variables
#########################

#  Variable que define si ya se configuró la ventana o no
configurado = IntVar()

# Variable que define si se codifica o decodifica
orden = IntVar()

#  Variables para los radiobutton de los menú para modo, tema e idioma
modo_var = IntVar()
tema_var = IntVar()
idioma_var = IntVar()

#  Variables de colores
blanco = "white"
negro = "black"
gris_claro = "grey94"
gris_medio_claro = "grey40"
gris_medio = "grey30"
gris_oscuro = "grey22"
azul_claro = "DodgerBlue2"
azul_medio = "RoyalBlue3"
azul_oscuro = "DodgerBlue3"
rojo_claro = "indian red"
rojo_medio = "crimson"

#  Variables de fuentes
fuente_bold = ("sans", 10, "bold")
fuente_normal = ("sans", 10)


#############################
# Creo las funciones
#############################

def cambiar_valor(archivo_nombre, texto):
    archivo = open(f"preferencias/{archivo_nombre}.txt", "w")

    archivo.write(texto)
    archivo.close()



def lee(archivo_nombre):
    archivo = open(f"preferencias/{archivo_nombre}.txt", "r")

    valor = ""

    for lineas in archivo:
        valor += lineas

    if archivo_nombre == "modo":
        #  Si el archivo fue corrompido lo devuelve al estado predefinido
        if valor != "horizontal" and valor != "vertical":
            cambiar_valor("modo", "vertical")
    elif archivo_nombre == "idioma":
        #  Si el archivo fue corrompido lo devuelve al estado predefinido
        if valor != "español" and valor != "ingles":
            cambiar_valor("idioma", "español")
    else:
        #  Si el archivo fue corrompido lo devuelve al estado predefinido
        if valor != "claro" and valor != "oscuro":
            cambiar_valor("tema", "oscuro")

    archivo.close()



def preferencias_predefinidas():
    #  Intento abrir el archivo para leerlo
    try:
        #  Intenta abrir el archivo de temas para leerlo, si no existe como da error pasa al except
        lee("tema")

        #  A continuación intenta abrir el archivo de modo para leerlo
        lee("modo")

        #  Por último intenta abrir el archivo de idioma para leerlo
        lee("idioma")
    #  Si no existe lo creo y le pongo los valores predefinidos
    except:
        #  Abro los archivos y como no existían se crean automáticamente y se les dan las preferencias predefinidas
        
        #  Preferencia para el tema de color
        cambiar_valor("tema", "claro")

        #  Preferencia para el modo de ventana
        cambiar_valor("modo", "vertical")

        #  Preferencia para el idioma de ventana
        cambiar_valor("idioma", "español")



def cerrar_ventana():
    root.quit()
    root.destroy()



def ayuda():
    if idioma_var.get() == 2:
        messagebox.showinfo("User help", message="This program has the target of cypher content in multiple cyphers, in case of be necesary. For it's use you should know the key letter of the cypher/s that you need and enter them without spaces in the asign place. After that you should push into one of the two options for code or decode, indicating the requierd. Then you are going to be able to enter the message you want to change and push the buttom \"Scramble\" for change your message \n\n In case of have another doubts consult at: ezequiel.signorini@gmail.com")
    else:
        messagebox.showinfo("Ayuda al usuario", message="Este programa tiene el objetivo de cifrar contenido en multiples cifrados, en caso de ser necesario. Para su uso deberá conocer la letra clave del/los cifrado/s que requiere e ingresarlos sin espacios en la casilla asignada. Luego deberá pulsar en una de las dos opciones disponibles ya sea para códificar o para décodificar, indicando la requerida. Entonces podrá ingresar lo que desee modificar y apretar el botón \"Procesar\" para que se procese su información \n \nEn caso de tener otras dudas consultar a: ezequiel.signorini@gmail.com")



def caracteres_no_disponibles():
    if idioma_var.get() == 2:
        messagebox.showinfo("Unaviable letters", message="Some cyphers don't have scrambling for special letter, in case of morse for example you can't use simbols and other caracters")
    else:
        messagebox.showinfo("Caracteres no disponibles", message="Algunos cifrados no permiten el uso de ciertos caracteres especiales, morse por ejemplo no permite el uso de símbolos y otros caracteres especiales")



def ver_cifrados():
    cifrados = ""
    for value in range(len(lista_codigos)):
        cifrados += lista_codigos[value]
        cifrados += ": "
        cifrados += lista_cod_abre[value]
        cifrados += "   "
        if value == 1 or value == 3 or value == 5:
            cifrados += "\n"

    if idioma_var.get() == 2:
        messagebox.showinfo("Cyphers and information about them", message=f"The available cyphers are: \n\n{cifrados} \n\n When using Morse you're going to need to put a space after every letter and separate the words with slashes, putting a space bettween to. \n When putting the cyphers to use make sure of use the key letter for avoid mistakes. \n In case of have more doubts check help.")
    else:   
        messagebox.showinfo("Cifrados e información de los mismos", message=f"Los cifrados disponibles son: \n\n{cifrados} \n\n Al usar morse será necesario poner un espacio despues de cada caracter y separar las palabras con barras, poniendo también un espacio de por medio.\n Al ingresar los cifrados a usar asegúrese de usar la letra clave para evitar posibles errores.\n En caso de tener más dudas revisar ayuda")



def copiar():
    root.clipboard_clear()
    root.clipboard_append(str(texto_cambiado.get(1.0, "end-1c")))



def centrar_ventana():
    #  Si el modo es vertical accede
    if modo_var.get() == 1:
        if configurado.get() == 0:
            ancho_ventana = 320
            alto_ventana = 570

            x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2  # toma el valor del ancho de la pantalla, lo divide a la mitad para saber cual es el punto central y para que el punto central de la ventana esté a la mitad de la pantalla le resta la mitad del ancho de la ventana
            y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
        else:
            ancho_ventana = 320
            alto_ventana = 550

            x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2  # toma el valor del ancho de la pantalla, lo divide a la mitad para saber cual es el punto central y para que el punto central de la ventana esté a la mitad de la pantalla le resta la mitad del ancho de la ventana
            y_ventana = root.winfo_screenheight() // 2 - (alto_ventana + 20) // 2

    else:
        if configurado.get() == 0:
            ancho_ventana = 605
            alto_ventana = 370

            x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2  # toma el valor del ancho de la pantalla, lo divide a la mitad para saber cual es el punto central y para que el punto central de la ventana esté a la mitad de la pantalla le resta la mitad del ancho de la ventana
            y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
        else:
            ancho_ventana = 605
            alto_ventana = 350

            x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2  # toma el valor del ancho de la pantalla, lo divide a la mitad para saber cual es el punto central y para que el punto central de la ventana esté a la mitad de la pantalla le resta la mitad del ancho de la ventana
            y_ventana = root.winfo_screenheight() // 2 - (alto_ventana + 20) // 2


    posicion = str(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")
    root.geometry(posicion)



def tema_claro():
    archivo = open(f"preferencias/tema.txt", "r")

    valor = ""

    for lineas in archivo:
        valor += lineas

    archivo.close()


    #  Si el tema estaba en oscuro o no se había configurado lo cambia
    if valor == "oscuro" or configurado.get() == 0:
        # Cambio el color al root
        root.config(bg=gris_claro)
        
        # Cambio el color a los frames
        frame_traducir.config(bg=gris_claro)
        frame_cambiado.config(bg=gris_claro)
        
        # Cambio el color a los elementos
        etiqueta_txt_traducir.config(bg=gris_claro, fg=negro)
        etiqueta_txt_cambiado.config(bg=gris_claro, fg=negro)
        etiqueta_cifrados.config(bg=gris_claro, fg=negro)

        etiqueta_adv_codes.config(bg=gris_claro, fg=rojo_claro)
        etiqueta_adv_code.config(bg=gris_claro, fg=rojo_claro)
        etiqueta_adv_traducir.config(bg=gris_claro, fg=rojo_claro)

        texto_traducir.config(bg=blanco, fg=negro, insertbackground=negro, highlightcolor=azul_claro, highlightbackground=gris_claro, highlightthickness=2)
        texto_cambiado.config(bg=blanco, fg=negro, insertbackground=negro, highlightcolor=azul_claro, highlightbackground=gris_claro, highlightthickness=2)
        code.config(bg=blanco, fg=negro, insertbackground=negro, highlightcolor=azul_claro, highlightbackground=gris_claro, highlightthickness=2)
        codificar.config(bg=gris_claro, fg=negro)
        decodificar.config(bg=gris_claro, fg=negro)
        
        boton_procesar.config(bg=azul_claro, fg=blanco, activeforeground=blanco, activebackground=azul_medio)
        boton_copiar.config(bg=blanco, fg=negro, activeforeground=azul_medio, activebackground=gris_claro)
        
        #  Cambio la escritura de tema
        cambiar_valor("tema", "claro")



def tema_oscuro():
    archivo = open(f"preferencias/tema.txt", "r")

    valor = ""

    for lineas in archivo:
        valor += lineas

    archivo.close()


    #  Si el tema estaba en claro o no se había configurado lo cambia
    if valor == "claro" or configurado.get() == 0:
        # Cambio el color al root
        root.config(bg=gris_oscuro)

        # Cambio el color a los frames
        frame_traducir.config(bg=gris_oscuro)
        frame_cambiado.config(bg=gris_oscuro)

        # Cambio el color a los elementos
        etiqueta_txt_traducir.config(bg=gris_oscuro, fg=gris_claro)
        etiqueta_txt_cambiado.config(bg=gris_oscuro, fg=gris_claro)
        etiqueta_cifrados.config(bg=gris_oscuro, fg=gris_claro)

        etiqueta_adv_codes.config(bg=gris_oscuro, fg=rojo_medio)
        etiqueta_adv_code.config(bg=gris_oscuro, fg=rojo_medio)
        etiqueta_adv_traducir.config(bg=gris_oscuro, fg=rojo_medio)

        texto_traducir.config(bg=gris_medio, fg=gris_claro, insertbackground=gris_claro, highlightcolor=azul_medio, highlightbackground=gris_medio, highlightthickness=2)
        texto_cambiado.config(bg=gris_medio, fg=gris_claro, insertbackground=gris_claro, highlightcolor=azul_medio, highlightbackground=gris_medio, highlightthickness=2)
        code.config(bg=gris_medio, fg=gris_claro, insertbackground=gris_claro, highlightcolor=azul_medio, highlightbackground=gris_medio, highlightthickness=2)
        codificar.config(bg=gris_oscuro, fg=azul_medio)
        decodificar.config(bg=gris_oscuro, fg=azul_medio)

        boton_procesar.config(bg=azul_medio, fg=gris_claro, activeforeground=gris_claro, activebackground=azul_oscuro)
        boton_copiar.config(bg=gris_medio, fg=gris_claro, activeforeground=gris_claro, activebackground=gris_medio_claro)
        
        #  Cambio la escritura del tema
        cambiar_valor("tema", "oscuro")



def modo_vertical():
    #  Cambio el tamaño de la ventana
    ancho_ventana = 320
    alto_ventana = 550
    
    #  Corroboro si es la primera vez que se llama a la función, si es así centra la ventana, sino solo le da la geometría
    if configurado.get() == 1:
        root.geometry(f"{str(ancho_ventana)}x{str(alto_ventana)}")
    else:
        centrar_ventana()
        configurado.set(1)

    #  Cambio la posición de los widgets

    #  Frames (texts y sus widgets)
    frame_traducir.place(x=30, y=110)
    frame_cambiado.place(x=30, y=300)

    #  Entry para los cifrados (todos sus widgets)
    etiqueta_cifrados.place(x=30, y=20)
    code.place(x=30, y=40)
    code.config(width=17)
    etiqueta_adv_code.place(x=30, y=65)

    #  Radiobutton para cifrar o decifrar (todos sus widgets)
    codificar.place(x=180, y=20)
    decodificar.place(x=180, y=40)
    etiqueta_adv_codes.place(x=180, y=65)

    #  Botones
    boton_copiar.place(x=178, y=500)
    boton_procesar.place(x=32, y=500)

    #  Cambio la escritura del modo
    cambiar_valor("modo", "vertical")



def modo_horizontal():
    #  Cambio el tamaño de la ventana
    ancho_ventana = 605
    alto_ventana = 350
    
    #  Corroboro si es la primera vez que se llama a la función, si es así centra la ventana, sino solo le da la geometría
    if configurado.get() == 1:
        root.geometry(f"{str(ancho_ventana)}x{str(alto_ventana)}")
    else:
        centrar_ventana()
        configurado.set(1)

    #  Cambio la posición de los widgets

    #  Frames (texts y sus widgets)
    frame_traducir.place(x=30, y=90)
    frame_cambiado.place(x=310, y=90)

    #  Entry para saber los cifrados (todos sus widgets)
    etiqueta_cifrados.place(x=30, y=10)
    code.place(x=30, y=30)
    code.config(width=40)
    etiqueta_adv_code.place(x=30, y=55)

    #  Radiobutton para cifrar o decifrar (todos sus widgets)
    codificar.place(x=300, y=30)
    decodificar.place(x=400, y=30)
    etiqueta_adv_codes.place(x=300, y=55)

    #  Botones
    boton_copiar.place(x=323, y=300)
    boton_procesar.place(x=150, y=300)

    #  Cambio la escritura del modo
    cambiar_valor("modo", "horizontal")



def idioma_español():
    archivo = open(f"preferencias/idioma.txt", "r")

    valor = ""

    for lineas in archivo:
        valor += lineas

    archivo.close()


    #  Si el idioma estaba en inglés
    if valor == "ingles":
        #  Cambio el idioma del menú principal
        barra_menu.entryconfig("Encryptions", label="Cifrados")
        barra_menu.entryconfig("Preferences", label="Preferencias")
        barra_menu.entryconfig("Help", label="Ayuda")

        #  Cambio el idioma del menú tema
        temas_menu.entryconfig("Light", label="Claro")
        temas_menu.entryconfig("Dark", label="Oscuro")

        #  No cambio el idioma del menú modo dado que el significado en español y en inglés es el mismo
        #  No cambio el idioma del menú idioma dado que el significado debe ser nativo del idioma

        #  Cambio el idioma del menú preferencias
        preferencias_menu.entryconfig("Themes", label="Temas")
        preferencias_menu.entryconfig("Mode", label="Modo")
        preferencias_menu.entryconfig("Languaje", label="Idioma")

        #  Cambio el idioma del menú ayuda
        ayuda_menu.entryconfig("Way to use", label="Modo de uso")
        ayuda_menu.entryconfig("Unaviable letters", label="Caracteres no disponibles")


        #  Cambio el idioma de los widgets
        
        #  Etiqueta de cifrados a usar
        etiqueta_cifrados.config(text="Elija los cifrados")

        # Radiobuttons
        codificar.config(text="Codificar    ")  # FRAME CIFRADO

        decodificar.config(text="Decodificar")  # FRAME CIFRADO

        # Etiqueta de referencia al texto que se traducirá
        etiqueta_txt_traducir.config(text="Ingrese el texto a cambiar")

        # Etiqueta de referencia al texto cambiado
        etiqueta_txt_cambiado.config(text="Texto cambiado")

        boton_procesar.config(text="Procesar", padx=34)  # FRAME CONTENIDO

        boton_copiar.config(text="Copiar", padx=36)


        #  Cambio el valor del archivo
        cambiar_valor("idioma", "español")



def idioma_ingles():
    archivo = open(f"preferencias/idioma.txt", "r")

    valor = ""

    for lineas in archivo:
        valor += lineas

    archivo.close()


    #  Si el idioma estaba en español
    if valor == "español":
        #  Cambio el idioma del menú principal
        barra_menu.entryconfig("Cifrados", label="Encryptions")
        barra_menu.entryconfig("Preferencias", label="Preferences")
        barra_menu.entryconfig("Ayuda", label="Help")

        #  Cambio el idioma del menú tema
        temas_menu.entryconfig("Claro", label="Light")
        temas_menu.entryconfig("Oscuro", label="Dark")

        #  No cambio el idioma del menú modo dado que el significado en español y en inglés es el mismo
        #  No cambio el idioma del menú idioma dado que el significado debe ser nativo del idioma

        #  Cambio el idioma del menú preferencias
        preferencias_menu.entryconfig("Temas", label="Themes")
        preferencias_menu.entryconfig("Modo", label="Mode")
        preferencias_menu.entryconfig("Idioma", label="Languaje")

        #  Cambio el idioma del menú ayuda
        ayuda_menu.entryconfig("Modo de uso", label="Way to use")
        ayuda_menu.entryconfig("Caracteres no disponibles", label="Unaviable letters")


        #  Cambio el idioma de los widgets
        
        #  Etiqueta de cifrados a usar
        etiqueta_cifrados.config(text="Choose cyphers")

        # Radiobuttons
        codificar.config(text="Code    ")  # FRAME CIFRADO

        decodificar.config(text="Encode")  # FRAME CIFRADO

        # Etiqueta de referencia al texto que se traducirá
        etiqueta_txt_traducir.config(text="Enter text to change")

        # Etiqueta de referencia al texto cambiado
        etiqueta_txt_cambiado.config(text="changed text")

        boton_procesar.config(text="Change", padx=36)  # FRAME CONTENIDO

        boton_copiar.config(text="Copy", padx=40)


        #  Cambio el valor del archivo
        cambiar_valor("idioma", "ingles")



#  Llamo a la función que se asegura de que los archivos de preferencias existan
preferencias_predefinidas()



################################
# Creo la funcion procesar
################################

def procesar():
    #  Si no ingresó ningun cifrado notifico al usuario
    if code.get() == "":
        if idioma_var.get() == 2:
            etiqueta_adv_code.config(text="- Enter a cypher")
        else:
            etiqueta_adv_code.config(text="- Ingrese un cifrado")
    # Sino Analizo el o los cifrados
    else:
        #  Creo un string var que almacenará los cifrados que sean correctos
        codes = StringVar()
        #  Creo una variable para los cifrados que no sean correctos y otra para los que si lo sean, de esta forma voy a poder analizar el texto ingresado
        c_correctos = ""
        c_no_registrados = 0

        #  Hago un for que recorra cada caracter de los cifrados ingresados y analizo si se refieren a un cifrado o no
        for c in (code.get()).upper():
            if c in lista_cod_abre:
                c_correctos += c
            else:
                c_no_registrados += 1
        
        
        #  Si hay cifrados correctos
        if c_correctos != "":
            #  Si el usuario ingresó algún cifrado correcto y ninguno incorrecto asigno a codes esos cifrados
            if c_no_registrados == 0:
                codes.set(c_correctos)
                etiqueta_adv_code.config(text="")
            #  Sino le informo al usuario
            else:
                #  Si el modo es el por defecto
                if modo_var.get() == 1:
                    if idioma_var.get() == 2:
                        etiqueta_adv_code.config(text="- Some cyphers are\nwrong")
                    else:
                        etiqueta_adv_code.config(text="- Algunos cifrados \nson incorrectos")
                #  Como el modo es horizontal usa todo el espacio
                else:
                    if idioma_var.get() == 2:
                        etiqueta_adv_code.config(text="- Some cyphers are wrong")
                    else:
                        etiqueta_adv_code.config(text="- Algunos cifrados son incorrectos")
        #  Sino como todos los cifrados son incorrectos notifico al usuario
        else:
            if idioma_var.get() == 2:
                etiqueta_adv_code.config(text="- The cyphers are wrong")
            else:
                etiqueta_adv_code.config(text="- Cifrados incorrectos")


    #  Veo si eligió o no si quiere cifrar o decifrar
    if orden.get() != 1 and orden.get() != 2 and codes.get() != "I":
        if idioma_var.get() == 2:
            etiqueta_adv_codes.config(text="- Choose a value")
        else:
            etiqueta_adv_codes.config(text="- Elija un valor")
    else:
        etiqueta_adv_codes.config(text="")


    #  Asigno lo que haya escrito el usuario a contenido
    contenido = (texto_traducir.get(1.0, "end-1c")).lower() #  Con el end-1c le digo que voy a leer el contenido del text desde el primer caracter hasta el anteultimo
    
    #  Si ingresó un texto a cambiar
    if contenido != "":
        etiqueta_adv_traducir.config(text="")
        texto_intraducible = ""

        #  Si ingresó un cifrado (considerando que sea correcto en base a lo analizado)
        if codes.get() != "":
            #  Modifica el texto

            # Si se quiere codificar, accede
            if orden.get() == 1:
                #  Creo una variable que almacene los cifrados que ya fueron usados
                cifrados_usados = ""

                for c in codes.get():
                    texto_intraducible = ""
                    #  Agrego el cifrado actual
                    cifrados_usados += str(c)

                    #  Si el caracter es es correspondiente a MORSE procede a codificar
                    if c == "M":
                        texto_modificado = ""

                        for c in contenido:
                            if c in diccionario_a_morse:
                                texto_modificado += diccionario_a_morse[c] 
                            else:
                                texto_intraducible += c
                        
                        contenido = texto_modificado

                    #  Si el caracter es es correspondiente a CESAR procede a codificar
                    elif c == "C":
                        texto_modificado = ""

                        for c in contenido:
                            if c in diccionario_a_cesar:
                                texto_modificado += diccionario_a_cesar[c] 
                            else:
                                texto_intraducible += c
                        
                        contenido = texto_modificado

                    #  Si el caracter es correspondiente a SIGNOC procede a codificar
                    elif c == "S":
                        texto_modificado = ""
                        
                        for c in contenido:
                            if c in diccionario_a_signoC:
                                texto_modificado += diccionario_a_signoC[c] 
                            else:
                                texto_intraducible += c
                        
                        contenido = texto_modificado
                    
                    # Sino como el caracter es correspondiente a INVERSO procede a invertirlo
                    else:
                        #  Si morse no está en los cifrados que ya fueron usados, solo invierte por caracter
                        if "M" not in cifrados_usados:
                            texto_invertido = ""
                            
                            for c in contenido:
                                texto_invertido = c + texto_invertido
                            
                            contenido = texto_invertido
                        #  Sino separa los caracteres por espacios para luego invertir el texto
                        else:
                            texto_invertido = ""
                            lista_cambiado = texto_modificado.split(" ")
                            
                            for c in lista_cambiado:
                                texto_invertido = c + " " +texto_invertido
                            
                            contenido = texto_invertido

            # Sino, como va a decodificar, accede
            elif orden.get() == 2:
                #  Creo una variable que almacene los cifrados que ya fueron usados
                cifrados_usados = ""

                for c in codes.get():
                    texto_intraducible = ""
                    #  Agrego el cifrado actual
                    cifrados_usados += str(c)

                    #  Si el caracter es es correspondiente a MORSE procede a decodificar
                    if c == "M":
                        lista_texto = contenido.split(" ")
                        texto_modificado = ""

                        for c in range(len(lista_texto)):
                            if lista_texto[c] in diccionario_a_comun_M:
                                texto_modificado += diccionario_a_comun_M[lista_texto[c]]
                            else:
                                texto_intraducible += lista_texto[c]
                        
                        contenido = texto_modificado

                    #  Si el caracter es es correspondiente a CESAR procede a decodificar
                    elif c == "C":
                        texto_modificado = ""

                        for c in contenido:
                            if c in diccionario_a_comun_C:
                                texto_modificado += diccionario_a_comun_C[c] 
                            else:
                                texto_intraducible += c
                        
                        contenido = texto_modificado

                    #  Si el caracter es correspondiente a SIGNOC procede a decodificar
                    elif c == "S":
                        texto_modificado = ""

                        for c in contenido:
                            if c in diccionario_a_comun_S:
                                texto_modificado += diccionario_a_comun_S[c] 
                            else:
                                texto_intraducible += c
                        
                        contenido = texto_modificado

                    # Sino como el caracter es correspondiente a INVERSO procede a invertirlo
                    else:
                        if "M" not in cifrados_usados:
                            texto_invertido = ""

                            for c in contenido:
                                texto_invertido = c + texto_invertido
                            
                            contenido = texto_invertido
                        else:
                            texto_invertido = ""
                            lista_cambiado = texto_modificado.split(" ")
                            
                            for c in lista_cambiado:
                                texto_invertido = c + " " +texto_invertido
                            
                            contenido = texto_invertido

            #  Como solo quiere invertir accede
            else:
                if codes.get() == "I":
                    texto_invertido = ""
                    
                    for c in contenido:
                        texto_invertido = c + texto_invertido
                    
                    contenido = texto_invertido

            #  Si en el cifrado se encontró algún caracter que no está disponible, lo notifica
            if texto_intraducible != "":
                if idioma_var.get() == 2:
                    etiqueta_adv_traducir.config(text="- Some letters aren't avaiable       \n   check help for more information")
                else:
                    etiqueta_adv_traducir.config(text="- Algunos caracteres no estan disponibles\nrevise ayuda para más información       ")
            
            texto_cambiado.config(state=NORMAL)
            texto_cambiado.delete(1.0, "end")
            texto_cambiado.insert(1.0, contenido)
            texto_cambiado.config(state=DISABLED)

    else:
        if idioma_var.get() == 2:
            etiqueta_adv_traducir.config(text="- You need to write something for change it")
        else:
            etiqueta_adv_traducir.config(text="- Debe ingresar algo para poderlo cambiar")



####################
#  Hago el menú
####################

barra_menu = Menu(root)
root.config(menu=barra_menu)


#  Creo el menu de preferencias
preferencias_menu = Menu(barra_menu, tearoff=0)

#  Creo el menú temas (claro/oscuro)
temas_menu = Menu(barra_menu, tearoff=0)

#  Creo las "funciones" dentro del menú temas
temas_menu.add_radiobutton(label="Claro", command=tema_claro, value=1, variable=tema_var)
temas_menu.add_radiobutton(label="Oscuro", command=tema_oscuro, value=2, variable=tema_var)

#  Asigno el valor a la variable de temas desde el archivo
try:
    #  Intento leer el archivo de tema
    tema = open("preferencias/tema.txt", "r")

    valor = ""
    for lineas in tema:
        valor += lineas

    if valor == "oscuro":
        tema_var.set(2)

    else:
        tema_var.set(1)
except:
    #  Sino como el archivo de tema no existe o está corrompido le paso los valores predefinidos
    tema_var.set(1)


#  Creo el menú modo (vertical/horizontal)
modo_menu = Menu(barra_menu, tearoff=0)

#  Creo las "funciones" dentro del menú modo
modo_menu.add_radiobutton(label="Vertical", command=modo_vertical, value=1, variable=modo_var)
modo_menu.add_radiobutton(label="Horizontal", command=modo_horizontal, value=2, variable=modo_var)

#  Asigno el valor a la variable de modo desde el archivo
try:
    #  Intento leer el archivo de modo
    modo = open("preferencias/modo.txt", "r")

    valor = ""

    for lineas in modo:
        valor += lineas

    if valor == "horizontal":
        modo_var.set(2)
    else:
        modo_var.set(1)
except:
    #  Sino como el archivo de modo no existe o está corrompido le paso los valores predefinidos
    modo_var.set(1)


#  Creo el menú idioma (español/ingles)
idioma_menu = Menu(preferencias_menu, tearoff=0)

idioma_menu.add_radiobutton(label="Español  ES", command=idioma_español, value=1, variable=idioma_var)
idioma_menu.add_radiobutton(label="English  EN", command=idioma_ingles, value=2, variable=idioma_var)

#  Asigno el valor a la variable de idioma desde el archivo
try:
    #  Intento leer el archivo de idioma
    modo = open("preferencias/idioma.txt", "r")

    valor = ""

    for lineas in modo:
        valor += lineas

    if valor == "ingles":
        idioma_var.set(2)
    else:
        idioma_var.set(1)
except:
    #  Sino como el archivo de idioma no existe o está corrompido le paso los valores predefinidos
    idioma_var.set(1)

#  Agrego los menú de preferencias
preferencias_menu.add_cascade(label="Temas", menu=temas_menu)
preferencias_menu.add_cascade(label="Modo", menu=modo_menu)
preferencias_menu.add_cascade(label="Idioma", menu=idioma_menu)


#  Creo el menú ayuda
ayuda_menu = Menu(barra_menu, tearoff=0)

# Creo las "funciones" dentro del menú ayuda
ayuda_menu.add_command(label="Modo de uso", command=ayuda)
ayuda_menu.add_separator()
ayuda_menu.add_command(label="Caracteres no disponibles", command=caracteres_no_disponibles)


#  Agreo la opción cifrados para visualizar los cifrados disponibles
barra_menu.add_command(label="Cifrados", command=ver_cifrados)

#  Agrego los submenus al menu del root
barra_menu.add_cascade(label="Preferencias", menu=preferencias_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)


###############################
# Creo el contenido del root
###############################

# Creo la etiqueta
etiqueta_cifrados = Label(root, text="Elija los cifrados")  # FRAME CIFRADO

# Creo el entry de los cifrados que va a usar
code = Entry(root)  # FRAME CIFRADO
code.focus_set()

# Creo una etiqueta que será cambiada como alerta en caso de ser necesario
etiqueta_adv_code = Label(root)  # FRAME CONTENIDO

# Radiobuttons para elegir si se codifica o decodifica
codificar = Radiobutton(root, text="Codificar    ", value=1, variable=orden)  # FRAME CIFRADO

decodificar = Radiobutton(root, text="Decodificar", value=2, variable=orden)  # FRAME CIFRADO


# Creo una etiqueta que será cambiada como alerta en caso de ser necesario
etiqueta_adv_codes = Label(root)  # FRAME CONTENIDO


# Creo el frame en donde estará el texto a traducir
frame_traducir = Frame(root)

# Creo la etiqueta de referencia al texto que se traducirá
etiqueta_txt_traducir = Label(frame_traducir, text="Ingrese el texto a cambiar")  # FRAME CONTENIDO
etiqueta_txt_traducir.grid(row=0, column=0, sticky="w")

# Creo el text en donde ingresará el texto a traducir
texto_traducir = Text(frame_traducir, width=30, height=8)  # FRAME CONTENIDO
texto_traducir.grid(row=1, column=0)

scroll_vertical_1 = Scrollbar(frame_traducir, command=texto_traducir.yview)  # FRAME CONTENIDO
texto_traducir.config(yscrollcommand=scroll_vertical_1.set)
scroll_vertical_1.grid(row=1, column=1, sticky=NSEW)

etiqueta_adv_traducir = Label(frame_traducir)
etiqueta_adv_traducir.grid(row=2, column=0, sticky="w")


# Creo un frame para el texto cambiado
frame_cambiado = Frame(root)

# Creo la etiqueta de referencia al texto cambiado
etiqueta_txt_cambiado = Label(frame_cambiado, text="Texto cambiado")  # FRAME CONTENIDO
etiqueta_txt_cambiado.grid(row=0, column=0, sticky="w")

# Creo el text en donde se mostrará el texto cambiado
texto_cambiado = Text(frame_cambiado, width=30, height=8)  # FRAME CONTENIDO
texto_cambiado.grid(row=1, column=0)

scroll_vertical_2 = Scrollbar(frame_cambiado, command=texto_cambiado.yview)  # FRAME CONTENIDO
texto_cambiado.config(yscrollcommand=scroll_vertical_2.set)
scroll_vertical_2.grid(row=1, column=1, sticky=NSEW)


# Creo el boton el cual hará que se codifique el texto
boton_procesar = Button(root, text="Procesar", command=procesar, padx=36)  # FRAME CONTENIDO

boton_copiar= Button(root, text="Copiar", command=copiar, pady=1, padx=40)



#  Asigno el idioma de los widgets desde los archivos
try:
    #  Intento leer el archivo de idioma
    tema = open("preferencias/idioma.txt", "r")

    valor = ""

    for lineas in tema:
        valor += lineas

    if valor == "ingles":
        #  Cambio el idioma de los elementos del menú
        barra_menu.entryconfig("Cifrados", label="Encryptions")
        barra_menu.entryconfig("Preferencias", label="Preferences")
        barra_menu.entryconfig("Ayuda", label="Help")

        #  Cambio el idioma del menú tema
        temas_menu.entryconfig("Claro", label="Light")
        temas_menu.entryconfig("Oscuro", label="Dark")

        #  No cambio el idioma del menú modo dado que el significado en español y en inglés es el mismo

        #  Cambio el idioma del menú idioma
        #  No cambio el idioma del menú idioma dado que el significado debe ser nativo del idioma

        #  Cambio el idioma del menú preferencias
        preferencias_menu.entryconfig("Temas", label="Themes")
        preferencias_menu.entryconfig("Modo", label="Mode")
        preferencias_menu.entryconfig("Idioma", label="Languaje")

        #  Cambio el idioma del menú ayuda
        ayuda_menu.entryconfig("Modo de uso", label="Way to use")
        ayuda_menu.entryconfig("Caracteres no disponibles", label="Unaviable letters")


        #  Cambio el idioma de los widgets
        
        #  Etiqueta de cifrados a usar
        etiqueta_cifrados.config(text="Choose cyphers")

        # Radiobuttons
        codificar.config(text="Code    ")  # FRAME CIFRADO

        decodificar.config(text="Encode")  # FRAME CIFRADO

        # Etiqueta de referencia al texto que se traducirá
        etiqueta_txt_traducir.config(text="Enter text to change")

        # Etiqueta de referencia al texto cambiado
        etiqueta_txt_cambiado.config(text="changed text")

        boton_procesar.config(text="Change", padx=36)  # FRAME CONTENIDO

        boton_copiar.config(text="Copy", padx=40)
except:
    #  Sino como el archivo de idioma no existe o está corrompido dejo los valores predefinidos (aplicados con anterioridad)
    pass


#  Asigno los estilos de los widgets desde los archivos
try:
    #  Intento leer el archivo de tema
    tema = open("preferencias/tema.txt", "r")

    valor = ""

    for lineas in tema:
        valor += lineas

    if valor == "oscuro":
        tema_oscuro()
    else:
        tema_claro()
except:
    #  Sino como el archivo de tema no existe o está corrompido le paso los valores predefinidos
    tema_claro()

#  Asigno las posiciones de los widgets desde los archivos
try:
    #  Intento leer el archivo de modo
    modo = open("preferencias/modo.txt", "r")

    valor = ""

    for lineas in modo:
        valor += lineas

    if valor == "horizontal":
        modo_horizontal()
    else:
        modo_vertical()
except:
    #  Sino como el archivo de modo no existe o está corrompido le paso los valores predefinidos
    modo_vertical()


root.mainloop()
