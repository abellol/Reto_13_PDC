import json

def buscar_deporte(datos:dict, deporte:str):
  for k, v in datos.items():
    for d in v["deportes"]:
      if d == deporte:
        nombre = v["nombres"] + " " + v["apellidos"]
        print(f"{nombre} practica {deporte}")
      else:
        continue
  return (" ")

def rango_edades(datos:dict, lim_1:int, lim_2:int):
  if lim_2 < lim_1:
    aux = lim_1
    lim_1 = lim_2
    lim_2 = aux

  for k, v in datos.items():
    age = v["edad"]
    if age >= lim_1 and age <= lim_2:
      nombre = v["nombres"]+ " " + v["apellidos"]
      print(f"{nombre} esta en el rango de {lim_1} a {lim_2} años, con {age}")
      age = 0
    else: 
      continue
  return(" ")

def menu(opcion:int):
       if opcion == 1:
            dep = input("Ingrese el deporte que desea consultar: ")
            d = dep.capitalize()
            return buscar_deporte(datos, d)
       elif opcion == 2:
            val_1 = int(input("Ingrese la edad minima (es un intervalo cerrado): "))
            val_2 = int(input("Ingrese la edad maxima (es un intervalo cerrado): "))
            return rango_edades(datos, val_1, val_2)

if __name__ == "__main__":     
    archivo = open(r"C:\Users\57320\OneDrive\Escritorio\programacion\PDC 2024\Retos PDC\Reto 13 PDC\prueba.json", "r")
    datos : dict = json.load(archivo)
    archivo.close()

    print("Opciones: \n1. Deporte \n2. Rango de edad")
    opcion = int(input("Ingrese la opcíon por la que desea filtrar: "))
    filtro = menu(opcion)
    print(filtro)



    



