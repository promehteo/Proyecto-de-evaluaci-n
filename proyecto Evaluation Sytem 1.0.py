# Variable de bucle
rep = True

# Definiendo menú 1
def menu_1():
    #aceder a la variable rep 
    global rep
    while rep == True:
        print("""
              Bienvenido al Sistema
              1) Estudiante
              2) Docente""")
        opciones = input("Ingrese su opción: ")
        try:
            opciones = int(opciones)
            if opciones == 1:
                estudiantes_menu(nombres, apellidos, cedulas)
                rep = False
            elif opciones == 2:
                docentes_menu(usuario_docente, contraseña_docente)
                rep = False
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Solo se admiten datos numéricos.")

def estudiantes_menu(nombres, apellidos, cedulas):
    global rep
    #bienvenida al estudiante
    print("Bienvenido estudiante de la 131")
    while rep == True:
        #entrada de datos del estudiante
        
        nombre = input("ingrese su nombre: ")
        apellido = input("ingrese su apellido: ")
        cedula = input("ingrese su cedula: ")
        while True:
            print("1)primer corte,  2)corte,    3)corte,    4)corte")
            cortes = input("ingresa el la evaluacion del corte que deseas: ")
            try:
                cortes = int(cortes)
                if cortes == 1:
                    print("/modulo de primer corte/")
                    rep = False
                    break
                elif cortes == 2:
                    print("/modulo de segundo corte/")
                    rep = False
                    break
                elif cortes == 3:
                    print("/modulo de tercero corte/")
                    rep = False
                    break
                elif cortes == 4:
                    print("/modulo de cuarto corte/")
                    rep = False
                    break
                else:
                    print("opcion invalida")
            except ValueError:
                print("solo se admiten datos numericos")

def docentes_menu(usuario_docente, contraseña_docente):
    intentos = 0
    global rep
    print("bienvenid@ docente")
    while rep == True:
        usuario = input("ingrese su usuario unico: ")
        if usuario in usuario_docente:
            intentos = 0
            contraseña = input("ingrese su contraseña: ")
            if contraseña in contraseña_docente:
                print("/modulo de menu de usuario/")
                break
            elif intentos == 2:
                print("demasiados intentos fallidos.")
                menu_1()
                break
            else:
                intentos = intentos + 1
                print("contraseña incorrecta intente de nuevo")
        elif intentos == 2:
            print("demasiados intentos fallidos")
            print("/modulo de menu 2/")
            break
        else:
            intentos = intentos + 1
            print("usuario incorrecto intente de nuevo")
    
    
    
    
#listas alumnos
nombres = []
apellidos = []
cedulas = []
#listas docentes
usuario_docente = ("martha")
contraseña_docente = ("123")
menu_1()