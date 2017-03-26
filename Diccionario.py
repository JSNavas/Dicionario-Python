import os

diccionario = []


def crearArchivo():
    archivo = open("Terminos.txt", "a")
    archivo.close()


def cargarArchivo():
    archivo = open("Terminos.txt", "r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            diccionario.append(linea)
            linea = archivo.readline()
    archivo.close()


def escribirArchivo():
    archivo = open("Terminos.txt", "w")
    diccionario.sort()

    for elemento in diccionario:
        archivo.write(elemento + '\n')
    archivo.close()


def AgregarAlDicionario():
    validarTermino = False
    while validarTermino == False:
        os.system("clear")
        print "\t\t\t       [  DICCIONARIO  ]"
        print "\t\t\t       -----------------\n"
        print " NUEVO TERMINO: "
        termino = raw_input("\n Termino: ")

        if(len(termino) == 0):
            raw_input('\n\t\t      Los campos no pueden estar vacios!')
            validarTermino = False
        else:
            validarTermino = True

    validarSignificado = False
    while validarSignificado == False:
        significado = raw_input(" Significado: ")
        if(len(significado) == 0):
            raw_input('\n\t\t      Los campos no pueden estar vacios!')
            validarSignificado = False
        else:
            validarSignificado = True

    if(termino and significado):
        print "\n Desea guardar este termino?"
        print " (s/n)\n"

        op = raw_input(" Opcion > ")

        if(op.lower() == 's'):
            diccionario.append(termino + ": " + significado)
            escribirArchivo()
            print "\n 'Termino guardado'"


def MostrarDicionario():
    os.system("clear")
    print "\t\t\t       [  DICCIONARIO  ]"
    print "\t\t\t       -----------------\n"

    DicionarioVacio = True

    for elemento in diccionario:
        print " " + elemento
        DicionarioVacio = False

    if DicionarioVacio == True:
        print " 'Su dicionario esta vacio'"


def BuscarEnDiccionario():
    os.system("clear")
    print "\t\t\t[  BUSCAR EN EL DICCIONARIO  ]"
    print "\t\t\t------------------------------"

    buscar = raw_input(" Buscar termino: ")
    print " -------------------------------------------------------------------------------"
    encontrado = True
    for elemento in diccionario:
        arreglo = elemento.split(":")

        terminos = str(arreglo[0])
        if buscar[0] in terminos[0]:
            encontrado = True
            
            print "\n (%s):%s" % (arreglo[0], arreglo[1])
            print " -------------------------------------------------------------------------------"
            
        else:
            encontrado = False

    if (encontrado == False):
        print "\n No se ha encontrado ningun resultado!"



def EliminarDelDiccionario():
    os.system("clear")
    print "\t\t\t[  ELIMINAR DEL DICCIONARIO  ]"
    print "\t\t\t------------------------------"

    eliminar = raw_input(" Buscar termino a eliminar: ")
    for elemento in diccionario:
        encontrado = True
        arreglo = elemento.split(":")

        if eliminar.lower() == arreglo[0].lower():
            encontrado = True;
            print " -------------------------------------------------------------------------------"
            print "\n Termino: %s" % arreglo[0]
            print " Significado:%s" % arreglo[1]
            print " -------------------------------------------------------------------------------"

            print "\n Seguro que desea eliminar este termino?"
            print " (s/n)\n"

            validar = raw_input(" Opcion > ")

            if validar.lower() == 's':
                diccionario.remove(elemento)
                print "\n 'Termino eliminado'"
                escribirArchivo()
                break

            else:
                break
        else:
            encontrado = False;

    if (encontrado == False):
        print "\n No se ha encontrado ese termino en el diccionario!"


crearArchivo()
cargarArchivo()

menu = True

while menu == True:
    os.system("clear")

    print "\t\t\t         [DICCIONARIO]"
    print "\t\t\t         -------------\n"
    print " 1. AGREGAR AL DICCIONARIO"
    print " 2. MOSTRAR DICCIONARIO"
    print " 3. BUSCAR EN EL DICCIONARIO"
    print " 4. ELIMINAR TERMINO"
    print " 5. SALIR\n"
    opMenu = raw_input(" Opcion > ")

    if opMenu == "1":
        os.system("clear")

        opAgregar = True
        while opAgregar == True:

            AgregarAlDicionario()

            print
            print " (v) Volver al menu"
            print " (a) Agregar otro termino"
            print " (s) Salir"
            print
            opcion = raw_input(" Opcion > ")

            if opcion == 'v':
                opAgregar = False
                menu = True

            elif opcion == 'a':
                opAgregar = True

            elif opcion == 's':
                print "\n 'Ha salido de la agenda' \n"
                opAgregar = False
                menu = False

            else:
                opAgregar = False
                menu = True

    if opMenu == "2":

        MostrarDicionario()

        print
        print " (v) Volver al menu"
        print " (s) Salir"
        print
        opcion = raw_input(" Opcion > ")

        if opcion == 'v':
            opAgregar = False
            menu = True

        elif opcion == 's':
            print "\n 'Ha salido de la agenda' \n"
            opAgregar = False
            menu = False

        else:
            opBuscar = False
            menu = True

    if opMenu == "3":
        os.system("clear")

        opBuscar = True
        while opBuscar == True:
            BuscarEnDiccionario()
            print "\n (v) Volver al menu"
            print " (b) Buscar otro termino"
            print " (s) Salir"
            print
            opcion = raw_input(" Opcion > ")

            if opcion == 'v':
                opBuscar = False
                menu = True

            elif opcion == 'b':
                opBuscar = True

            elif opcion == 's':
                print "\n 'Ha salido de la agenda' \n"
                opBuscar = False
                menu = False

            else:
                break

    if opMenu == "4":
        # os.system("clear")

        opEliminar = True
        while opEliminar == True:

            EliminarDelDiccionario()

            print
            print " (v) Volver al menu"
            print " (e) Eliminar otro termino"
            print " (s) Salir"
            print
            opcion = raw_input(" Opcion > ")

            if opcion == 'v':
                opEliminar = False
                menu = True

            elif opcion == 'e':
                opEliminar = True

            elif opcion == 's':
                print "\n 'Ha salido de la agenda' \n"
                opEliminar = False
                menu = False

            else:
                opEliminar = False
                menu = True

    if opMenu == "5":
        print "\n 'Ha salido de la agenda' \n"
        break
