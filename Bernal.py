from os import system
system ("cls")

import random

import statistics
#geometric_mean([coleccion])





trabajadores=['Juan Perrez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernandez','Miguel Zanchez','Isabel Gómez','Francisco Díaz','Elena Fernandez']
sueldos=[]

def asignar_sueldos():
    for i in range(10):
         sueldo_aleatorio=random.randint(300000,2500000)
         sueldos.append(sueldo_aleatorio)
         print(trabajadores[0],sueldo_aleatorio, trabajadores[1],sueldo_aleatorio,trabajadores[2],sueldo_aleatorio,
               trabajadores[3],sueldo_aleatorio, trabajadores[4],sueldo_aleatorio, trabajadores[5],sueldo_aleatorio,
               trabajadores[6],sueldo_aleatorio, trabajadores[7],sueldo_aleatorio, trabajadores[8],sueldo_aleatorio,
               trabajadores[9],sueldo_aleatorio,)


def clasificar_sueldos():
     print('''
Nombre      Sueldo
''')
     for sueldo in sueldos:
         if sueldos <= 800000:
          print(f'''
{trabajadores} {sueldo}
''')
          if sueldos > 800000 and sueldos <=2000000:
              print(f'''
{trabajadores} {sueldo}
''')
              if sueldos>2000001:
                  print(f'''
{trabajadores} {sueldo}
''')
                  break


#def ver_estadisticas():





#def reporte_de_sueldos():


while True:
    print('''
1. Asignar sueldo aleatorio
2. Clasificar sueldos
3. Ver estadísticas
4. Reporte de sueldos

5. Salir

''')
    op = input("Seleccione una opción: ")
    match op:
        case "1":
            asignar_sueldos()

        case "2":
            clasificar_sueldos()

        case "3":
              ver_estadisticas()
              

        case "4":
              reporte_de_sueldos

        case "5":
              print("finalizando programa...\nDesarrollado por: Juan Bernal\nRun: 16.005.202-3")
              break
