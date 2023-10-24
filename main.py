from codigos import *

#Doy la bienvenida
print(" ")
print("CO.dificador")
print("DE.codificador")
print("Mc.Multi-Cifrado")
print(" ")


##############
# While
##############

# Argumentos  
argumento = "algo"
lan = ""
lan_aprobado = False
codes = ""
seguir = ""
bandera = 0

# Se muestran los cifrados
print("______________________________________")
print("cifrados disponibles: \n- Morse: M \n- Cesar: C \n- SignoC: S \n- Inverso: I")
print("______________________________________")
print(" ")


while argumento == "algo":
  ####################
  # Toma de cifrados
  ####################

  c_no_registrados = ""  # Caracteres incorrectos

  while lan == "" or lan_aprobado == False:  # Si es la primera vez que se ejecuta el código o los cifrados no están aprobados, accede

    lan = input("Ingrese el cifrado o los cifrados que desea usar: ").upper()

    if lan == "SALIR":
      argumento = ""
      break
    elif lan == "":
      print("- Debe ingresar algo, si desea salir ingrese SALIR -")
    else:
      for c in lan:
        if c in lista_cod_abre:
          codes += c
        else:
          c_no_registrados += c

    if c_no_registrados != "" and codes != "":
      correjir = 1
    else:
      correjir = 0

    while correjir == 1:  # mientras haya ingresado algo correcto y algo incorrecto, accede
      print(" ")
      if len(c_no_registrados) == 1:
        print("_ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _")
        seguir = input(f"- El caracter {c_no_registrados} no está disponible, ¿desea seguir con el resto? ").lower()
      else:
        print("_ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _ . _")
        seguir = input(f"- Los caracteres {c_no_registrados} no están disponibles, ¿desea seguir con el resto? ").lower()
      
      if seguir == "no":
        print("Le pediremos que vuelva a ingresar los cifrados, recuerde que los cifrados disponibles son:")

        # Recuerda por medio de un for los caracteres disponibles y como ingresarlos
        print(" ")
        contador = 0
        print("______________________________________")
        for c in lista_cod_abre:
          print(f"{lista_codigos[contador]}: {c}")
          contador += 1
        print("______________________________________")
        codes = ""
        c_no_registrados = ""
        break
      elif seguir == "si" or seguir == "sí":
        c_no_registrados = ""
        break


    if c_no_registrados != "" and codes == "":  # Si todo lo que ingresó está mal a este punto, accede
      if len(c_no_registrados) == 1:
        print(f"- El caracter ingresado no está disponible -")
      else:
        print(f"- Los caracteres ingresados no estan disponibles -")
      
      # Recuerda por medio de un for los caracteres disponibles y como ingresarlos
      print("Recuerde que los cifrados disponibles son:")
      contador = 0
      print("______________________________________")
      for c in lista_cod_abre:
        print(f"{lista_codigos[contador]}: {c}")
        contador += 1
      print("______________________________________")
      c_no_registrados = ""

    elif c_no_registrados == "" and codes != "":  # Si todo lo que ingresó está bien a este punto, accede
      lan_aprobado = True  # Como ya está bien no vuelve a acceder a este while, mientras lo quiera seguir usando
      seguir = "si"


  ####################
  # Funcionalidad
  ####################
  orden = "1"
  while seguir == "si":
    if codes != "":  # Pregunto si es distinto a nada ya que solo llega acá si los códigos están bien
      # Imprime los códigos ingresados
      if codes != "I":
        print(" ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        if len(codes) == 1:
          print(f"- Usted está por usar el código: {codes}")
        else:
          print(f"- Usted está por usar los códigos: {codes}")
    
        print(" ")
        print("A continuación elija: \n- Si desea codificar: 1 \n- Si desea decodificar: 2 \n- Si desea salir: SALIR")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

        orden = input("¿Qué desea hacer? ")

        pasos = ""
        while len(codes) > 1 and pasos == "":
          print(" ")
          pasos = input("¿Deséa saber como cambia en cada paso? ").lower()
          if pasos == "si" or pasos == "sí":
            pasos = True
          elif pasos == "no":
            pasos = False
          else:
            print("- Debe ingresar \"si\" o \"no\" -")
            pasos = ""

      else:
        orden = "3"

      if orden == "salir":
        argumento = ""  # Para que no se vuela a ejecutar el código
        lan_aprobado = False  # Para que no acceda al siguiente while
        break  # Rompe el while

      elif orden in lista_funciones: # Si la orden existe procede a traducir
        print("______________________________________")
        texto_traducir = input("Ingrese el texto a traducir:\n").lower()
        texto_cambiado = texto_traducir
        texto_intraducible = ""

        if texto_cambiado != "":  # Uso texto cambiado dado que een esta variable almacenaré el texto en todo su proceso
          # Analizo los caracteres ingresados y si están disponibles para luego usarlos
          # Si se quiere codificar, accede
          if orden == "1":
            contador = 0
            for c in codes:
              if c == "M":  # Si el caracter es es correspondiente a MORSE procede a codificar o decodificar
                # Codifica
                if orden == "1":
                  texto_antes = texto_cambiado
                  texto_cambiado = ""

                  for c in texto_antes:
                    if c in diccionario_a_morse:
                      texto_cambiado += diccionario_a_morse[c] 
                    else:
                      texto_intraducible += c

                # Decodifica
                elif orden == "2":
                  lista_texto = texto_cambiado.split(" ")
                  texto_cambiado = ""

                  for i in range(len(lista_texto)):
                    if lista_texto[i] in diccionario_a_comun_M:
                      texto_cambiado += diccionario_a_comun_M[lista_texto[i]]
                    else:
                      texto_intraducible += lista_texto[i]

              elif c == "C":  # Si el caracter es es correspondiente a CESAR procede a codificar o decodificar
                # Codifica
                if orden == "1":
                  texto_antes = texto_cambiado
                  texto_cambiado = ""

                  for c in texto_antes:
                    if c in diccionario_a_cesar:
                      texto_cambiado += diccionario_a_cesar[c] 
                    else:
                      texto_intraducible += c

                # Decodifica
                elif orden == "2":
                  texto_antes = texto_cambiado
                  texto_cambiado = ""

                  for c in texto_antes:
                    if c in diccionario_a_comun_C:
                      texto_cambiado += diccionario_a_comun_C[c] 
                    else:
                      texto_intraducible += c

              elif c == "S":  # Si el caracter es correspondiente a SIGNOC procede a codificar o decodificar
                # Codifica
                if orden == "1":
                  texto_antes = texto_cambiado
                  texto_cambiado = ""

                  for c in texto_antes:
                    if c in diccionario_a_signoC:
                      texto_cambiado += diccionario_a_signoC[c] 
                    else:
                      texto_intraducible += c
                
                # Codifica
                elif orden == "2":
                  texto_antes = texto_cambiado
                  texto_cambiado = ""

                  for c in texto_antes:
                    if c in diccionario_a_comun_S:
                      texto_cambiado += diccionario_a_comun_S[c] 
                    else:
                      texto_intraducible += c

              elif c == "I":  # Si el caracter es correspondiente a INVERSO procede a invertirlo
                if "M" not in codes:
                  texto_invertido = ""

                  for c in texto_cambiado:
                    texto_invertido = c + texto_invertido
                  texto_cambiado = texto_invertido
                else:
                  texto_invertido = ""
                  lista_cambiado = texto_cambiado.split(" ")
                  
                  for c in lista_cambiado:
                    texto_invertido = c + " " +texto_invertido
                  texto_cambiado = texto_invertido
              
              if pasos == True:
                if contador == 0:
                  print(" \n ")
                else:
                  print(" ")
                print(f"- La codificación a {codes[contador]} es: \n{texto_cambiado}")
                contador = contador + 1

          # Sino, como va a decodificar, accede
          elif orden == "2":
            codes_inverso = ""
            for c in codes:
              codes_inverso = c + codes_inverso
            
            contador = 0
            caracteres = ""

            for c in codes_inverso:
              if c == "M":  # Si el caracter es es correspondiente a MORSE procede a codificar o decodificar
                # Codifica
                if orden == "1":
                  texto_antes = texto_cambiado
                  texto_cambiado = ""

                  for c in texto_antes:
                    if c in diccionario_a_morse:
                      texto_cambiado += diccionario_a_morse[c] 
                    else:
                      texto_intraducible += c

                # Decodifica
                elif orden == "2":
                  lista_texto = texto_cambiado.split(" ")
                  texto_cambiado = ""

                  for i in range(len(lista_texto)):
                    if lista_texto[i] in diccionario_a_comun_M:
                      texto_cambiado += diccionario_a_comun_M[lista_texto[i]]
                    else:
                      texto_intraducible += lista_texto[i]

              elif c == "C":  # Si el caracter es es correspondiente a CESAR procede a codificar o decodificar
                # Codifica
                if orden == "1":
                  texto_antes = texto_cambiado
                  texto_cambiado = ""

                  for c in texto_antes:
                    if c in diccionario_a_cesar:
                      texto_cambiado += diccionario_a_cesar[c] 
                    else:
                      texto_intraducible += c

                # Decodifica
                elif orden == "2":
                  texto_antes = texto_cambiado
                  texto_cambiado = ""

                  for c in texto_antes:
                    if c in diccionario_a_comun_C:
                      texto_cambiado += diccionario_a_comun_C[c] 
                    else:
                      texto_intraducible += c

              elif c == "S":  # Si el caracter es correspondiente a SIGNOC procede a codificar o decodificar
                # Codifica
                if orden == "1":
                  texto_antes = texto_cambiado
                  texto_cambiado = ""

                  for c in texto_antes:
                    if c in diccionario_a_signoC:
                      texto_cambiado += diccionario_a_signoC[c] 
                    else:
                      texto_intraducible += c
                
                # Codifica
                elif orden == "2":
                  texto_antes = texto_cambiado
                  texto_cambiado = ""

                  for c in texto_antes:
                    if c in diccionario_a_comun_S:
                      texto_cambiado += diccionario_a_comun_S[c] 
                    else:
                      texto_intraducible += c

              elif c == "I":  # Si el caracter es correspondiente a INVERSO procede a invertirlo
                if "M" not in codes or "M" not in caracteres:
                  texto_invertido = ""

                  for c in texto_cambiado:
                    texto_invertido = c + texto_invertido
                  texto_cambiado = texto_invertido
                else:
                  texto_invertido = ""
                  lista_cambiado = texto_cambiado.split(" ")
                  
                  for c in lista_cambiado:
                    texto_invertido = c + " " +texto_invertido
                  texto_cambiado = texto_invertido

              
              if pasos == True:
                if contador == 0:
                  print(" \n ")
                else:
                  print(" ")
                print(f"- La codificación a cifrado {codes_inverso[contador]} es: \n{texto_cambiado}")
                contador += 1
              
              caracteres += c  # Agrego una variable que contiene los caracteres que ya se analizaron en el for

          # Sino, como solo quiere invertir el texto, accede
          else:
            texto_invertido = ""
            
            for c in texto_cambiado:
              texto_invertido = c + texto_invertido
            texto_cambiado = texto_invertido
        
        ###########################
        # Imprime el texto final  
        ###########################

        print(" \n ")
        print("__________________________________________________________________________")
        # Si se queria codificar accede
        if orden == "1":
          print(f"Este es el texto codificado: \n{texto_cambiado}")
          # Si hay caracteres que no existen accede
          if texto_intraducible != "":
            print(f"No hemos encontrado codificación para los siguientes caracteres: \n{texto_intraducible}")

        # Sino, si se decodificó accede
        elif orden == "2":
          print(f"Este es el texto decodificado: \n{texto_cambiado}")
          # Si hay caracteres inexistentes accede
          if texto_intraducible != "":
            print(f"No hemos encontrado decodificación para los siguientes caracteres: \n{texto_intraducible}")
        elif orden == "3":
          print(" \n ")
          print(f"Este es el texto invertido: \n{texto_cambiado}")
        
        print("__________________________________________________________________________")
        
        texto_antes = ""
        texto_cambiado = ""
        texto_intraducible = ""

        # Hace que el while solo se ejecute 1 vez y tenga que salir del while, siempre y cuando haya ingresado una función correcta
        seguir = "no"

      # Sino, dado que la funcion no existiría envia un error
      else:
        print("- No hemos encontrado la función solicitada -")


  ########################################
  # Reutilización de cifrados correctos
  ########################################

  while codes != "" and lan_aprobado:  # Cuando ya se ingresó uno o varios cifrados correctos accede
    print(" ")
    # Menciona los cifrados en uso y pregunta si se quieren seguir usando
    if len(codes) == 1:
      print("__________________________________________________________________________")
      seguir = input(f"- Usted ha estado usando el cifrado {codes}, ¿desea seguirlo usando? ").lower()
    else:
      print("__________________________________________________________________________")
      seguir = input(f"- Usted ha estado usando los cifrados {codes}, ¿desea seguirlos usando? ").lower()

    if seguir == "":
      print("- Necesitamos que ingreses \"sí\" o \"no\" -")

    elif seguir == "si" or seguir == "sí":
      seguir = "si"  # Permite que pase a codificar ni bien se vuelva a ejecutar el while general
      break
    
    elif seguir == "no":
      lan = ""
      codes = ""
      c_no_registrados = ""
      lan_aprobado = False
      break

    else:
      print("- Necesitamos que ingreses \"sí\" o \"no\" -")

# Termino el programa
print(" ")
print("El programa ha finalizado")
print(". . . . . . . . . . . . . . . . . . . . . .")
print("Usted ha usado la versión 1.4")
print(" ")