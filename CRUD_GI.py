from CRUD_read import leer
from CRUD_update import actualizar
from CRUD_create import agregar
from CRUD_delete import borrar

ruta = r"/home/paelsam/Escritorio/CRUD/docs/Base CRUD.xlsx"
datos = {
    'Titulo': '',
    'Descripcion': '',
    'Estado': '',
    'Fecha Inicio': '',
    'Fecha Finalizacion': ''
}
swith = True

while swith == True:
    print("***************BIENVENIDOS A CRUD***************")
    print("Ingresa la accion que desas realizar: ")
    print("1) Leer Informacion (READ) \n2) Actualizar Informacion (UPDATE) \n3) Agregar Nueva Inforamcion (CREATE) \n4) Borrar Informacion (DELETE) \n5) Salir (EXIT)")
    opciones = input("Ingresa una opcion: ")
    print("\n")
    if opciones == 1 or opciones == str(1):
        print("******Leyendo Informacion******")
        filtro = input("Escribe el Estado que quieres mostrar: ")
        if filtro == "" or filtro != "todo":
            leer(ruta, filtro)
        else:
            leer(ruta, "todo")
        input("Presiona [ENTER] para continuar")
        print("\n")
    elif opciones == 2 or opciones == str(2):
        print("\n")
        print("*******Actualizar Informacion********")
        idToUpdate = int(input("Ingresa el ID de la informacion que deseas actualizar: "))
        print("*********Nuevo Titulo*********")
        datos['Titulo'] = input("Ingresa un nuevo titulo: ")
        print("*********Nueva Descripcion*******")
        datos['Descripcion'] = input("Ingresa una nueva descripcion: ")
        print("*********Nuevo Estado************")
        datos["Estado"] = input("Ingresa un nuevo estado: ")
        print("*********Nueva Fecha de Inicio*******")
        datos["Fecha Inicio"] = input("Ingresa una nueva fecha de inicio: ")
        print("*********Nueva Fecha de Finalizacion*******")
        datos["Fecha Finalizacion"] = input("Ingresa una nueva fecha de finalizacion: ")
        print(actualizar(ruta, idToUpdate, datos))
        input("Presiona [ENTER] para continuar")
        print("\n")
    elif opciones == 3 or opciones == str(3):
        print("\n")
        print("*********Nueva Informacion******* \n")
        print("*********Nuevo Titulo*********")
        datos['Titulo'] = input("Ingresa un nuevo titulo: ")
        print("*********Nueva Descripcion*******")
        datos['Descripcion'] = input("Ingresa una nueva descripcion: ")
        print("*********Nuevo Estado************")
        datos["Estado"] = input("Ingresa un nuevo estado: ")
        print("*********Nueva Fecha de Inicio*******")
        datos["Fecha Inicio"] = input("Ingresa una nueva fecha de inicio: ")
        print("*********Nueva Fecha de Finalizacion*******")
        datos["Fecha Finalizacion"] = input("Ingresa una nueva fecha de finalizacion: ")
        print(agregar(ruta, datos))
        input("Presiona [ENTER] para continuar")
        print("\n")
    elif opciones == 4 or opciones == str(4):
        print("\n")
        print("*******Borrar Informacion********")
        idToUpdate = int(input("Ingresa el ID de la informacion que deseas borrar: "))   
        print(borrar(ruta, idToUpdate))
        input("Presiona [ENTER] para continuar")
        print("\n") 
    elif opciones == 5 or opciones == str(5):
        print("*********Saliendo...**********")
        swith = False
        input("Presiona [ENTER] para continuar")

          
        
        
        