def impresionKeys():
    i = {"arbol":"tree", "mesa":"table"}

    for esp, eng in i.items():
        print(esp, "-->", eng)

def busquedaYcreacion():
    archivo = input("Ingrese nombre del archivo")
    try:
        f = open(archivo)
    except FileNotFoundError:
        print("Archivo no encontrado")
    alumnos = {}

    linea = f.readline().strip()
    while linea != "":
        #print(linea)
        igual = linea.find("=")
        carnet = linea[:igual]
        nombre = linea[igual+1:]
        print("Carnet:", carnet, "- Nombre:", nombre)
        alumnos[carnet] = nombre
        linea = f.read().strip()

    while True:
        print()
        print("1. Ingresar Alumno")
        print("2. Modificar Alumno")
        print("3. Eliminar Alumno")
        print("4. Listar todos")
        print("5. Salir")
        op = input("Ingrese su opcion\n")
        if op == 1:
            carnet = input("Ingrese el carnet del alumno")
            if carnet in alumnos:
                print("Error, ya existe el alumno")
            else:
                nombre = input("Ingrese nombre")
                alumnos[carnet] = nombre
                print("Se agrego {} - {}".format(carnet, nombre))
        if op == 2:
            carnet = input("Ingrese el carnet del alumno")
            if carnet in alumnos:
                nombre = input("Ingrese nombre")
                alumnos[carnet] = nombre
                print("Se agrego {} - {}".format(carnet, nombre))
            else:
                print("Error, no existe el carnet")
        if op == 3:
            carnet = input("Ingrese el carnet del alumno")
            if carnet in alumnos:
                nombre = input("Ingrese nombre")
                nombre = alumnos.pop(carnet)
                print("Se elimino {} - {}".format(carnet, nombre))
            else:
                print("Error, no existe el carnet")
        if op == 4:
            for c, n in alumnos.items():
                print(c, "-->", n)
busquedaYcreacion()

#s.strip()