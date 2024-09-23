# Reto 13: Diccionarios

### Soy Alejandro Bello y pertenezco al grupo de "Fenomenoides", adjunto nuestro logo: 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

A continuación se muestra la solución planteada al reto:

## 1. Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
### Solucion:
```python
def ordenar (diccionario:dict) -> dict:
  aux = []
  lista = []
  for k, i in prueba.items():
    aux.append(i)
    aux.append(k)
    lista.append(aux)
    aux = []
  lista.sort()
  for element in lista:
    aux = element[0]
    element[0] = element[1]
    element[1] = aux
  diccionario = dict(lista)
  return diccionario

if __name__ == "__main__":
    prueba = {1: "Y", 
            "b": "X",
            "c" : "Z", 
            "d" : "D"}

    print(ordenar(prueba))
```
## 2. Desarrollar una funci�on que reciba dos diccionarios como par�ametros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.
#### Solución:
```python
def mezclar_diccionarios(dict_1:dict, dict_2:dict):
	#verifica si hay llaves repetidas en ambos diccionarios y asigna en ambos el valor del primero en ambas claves
	for key in dict_1:
		if key in dict_2:
			dict_2[key] = dict_1[key]
	dict_1.update(dict_2)
	return dict_1

if __name__ == "__main__":
	dict_x = {"calculo" : 42,
		   			"electronica" : 45,
						"tmb" : 43,
						"dibujo basico" : 50}
	dict_y = {"catedra de induccion" : 42,
		   			"calculo" : 50,
						"tmb" : 20}

	x = mezclar_diccionarios(dict_y, dict_x)
	print(x)


	# Descomentar para probar ambos casos
	# x = mezclar_diccionarios(dict_x, dict_y)
	# print(x)
```
## 3. Dado el JSON:
```JSON
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "D��az Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["F�utbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```
Cree un programa que lea de un archivo con dicho JSON y:
+ Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
+ Imprima los nombres completos (nombre y apellidos) de las personas que est�en en un rango de edades dado por el usuario.

### Solución:
```python
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
```
## 4. El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:
```python
import json

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)
```
Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt', así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busqye el nivel de lluvia, si es vientos, la velocidad del viento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.

### Solución: 

```python
import json
from datetime import datetime
from pprint import pprint

def obtener_fechas(fechas: dict):
    # Función para pasar fechas de UTC a algo más legible
    for key in fechas:
        x = fechas[key]
        fechas[key] = datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S')
    return fechas

def hallar_TmpMin(datos: dict):
    # Acceder a todas las claves que tienen información relevante
    fechas: dict = datos.get("dt")
    tmpmax: dict = datos.get("tmpMax")
    tmpmin: dict = datos.get("tmpMin")
    humedad = datos.get("humidity")
    fechas_normales: dict = obtener_fechas(fechas.copy())  # Usar copia para no modificar el JSON original
    alerta_tmpmin: dict = datos.get("alertTmpMin")
    for k in alerta_tmpmin:
        # Verificar que haya un evento ese día
        if alerta_tmpmin[k] == "X":
            # acceder a todas las variables relacionadas al fenómeno
            maxi = tmpmax[k]
            mini = tmpmin[k]
            humidity = humedad[k]
            # Retornar un string con toda la información de cada suceso
            return f"\tAlerta de bajas temperaturas\nHay alerta de bajas temperaturas el día {fechas_normales[k]}, con una minima de {mini} y una maxima de {maxi}. Habrá una humedad de {humidity}\n"
    return None

def hallar_precip(datos: dict):
    fechas: dict = datos.get("dt")
    humedad = datos.get("humidity")
    prcp = datos.get("prcp")
    recomendacion = datos.get("recomendaciones")
    fechas_normales: dict = obtener_fechas(fechas.copy())  
    alerta_precip: dict = datos.get("alertPrecip")
    clima: dict = datos.get("weather")
    for k in alerta_precip:
        if alerta_precip[k] == "X":
            humidity = humedad[k]
            description = clima[k][0]["description"]
            precipitacion = prcp[k]
            reco = recomendacion["lluvias"]
            return f"\t Alerta de precipitación\nHay alerta de {description} el día {fechas_normales[k]}, con una humedad de {humidity} y el nivel de precipitación es de {precipitacion}.\nRecomendaciones: {reco}\n"
    return None

def hallar_TmpMax(datos: dict):
    fechas: dict = datos.get("dt")
    tmpmax: dict = datos.get("tmpMax")
    tmpmin: dict = datos.get("tmpMin")
    humedad = datos.get("humidity")
    fechas_normales: dict = obtener_fechas(fechas.copy())  
    alerta_tmpmax: dict = datos.get("alertTmpMax")
    for k in alerta_tmpmax:
        if alerta_tmpmax[k] == "X":
            humidity = humedad[k]
            maxi = tmpmax[k]
            mini = tmpmin[k]
            return f"\t Alerta de altas temperaturas\nHay alerta de altas temperaturas el día {fechas_normales[k]}, con una maxima de {maxi} y una minima de {mini}.Habrá una hunmedad de {humidity}\n"
    return None



def hallar_VelViento(datos: dict):
    fechas: dict = datos.get("dt")
    velviento = datos.get("velViento")
    direccion = datos.get("dirViento")
    humedad = datos.get("humidity")
    fechas_normales: dict = obtener_fechas(fechas.copy())  
    alerta_velviento: dict = datos.get("alertVelViento")
    for k in alerta_velviento:
        if alerta_velviento[k] == "X":
            velocidad = velviento[k]
            dire = direccion[k]
            humidity = humedad[k]
            return f"\tAlerta velocidad del viento\nHay alerta de velocidad de viento el día {fechas_normales[k]} con una velocidad de {velocidad}, con una dirección de {dire}°. Habrá una humedad de {humidity}\n"
    return None

def hallar_alertAlertas(datos: dict):
    fechas: dict = datos.get("dt")
    fechas_normales: dict = obtener_fechas(fechas.copy())  
    alerta_alertas: dict = datos.get("alertAlertas")
    for k in alerta_alertas:
        if alerta_alertas[k] == "X":
            return f"Hay alertas el día {fechas_normales[k]}\n"
    return f"no hay alertas de alertas"

def hallar_alertas(datos: dict):
    precip = hallar_precip(datos)
    tmpmax = hallar_TmpMax(datos)
    tmpmin = hallar_TmpMin(datos)
    velviento = hallar_VelViento(datos)
    alertas = hallar_alertAlertas(datos)
    return (f"{precip}\n{tmpmax}\n{tmpmin}\n{velviento}\n{alertas}")

if __name__ == "__main__":
  # Cargar archivo
  jsonString = '''
  {\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
  '''
  data: dict = json.loads(jsonString)

  # Ejecutar y mostrar la función principal
  x = hallar_alertas(data)
  print(x)
```

## 5. A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.
### Solucion:
```python
import requests
from pprint import pprint

def Imprimir_Json(Json):

    '''
        Esta función imprime el json pedido por la api de manera ordenada

        Args:
            La función recibe un diccionario que es el json como Json

        Returns:
            La función no retorna valor o elemento a la función que la llamo sino imprime de manera ordenada el diccionario
    '''

    for k,v in Json.items():
        if isinstance(v, list): #verificar si esta como elemento lista
            if isinstance(v[0], dict): # verificar si es un diccionario
                print(f"Llave: {k}, Valor(Otro diccionario): \n")
                for i,j in v[0].items():
                    print(f"Llave: {i} , Valor: {j}")
        else:
            print(f"Llave: {k} , Valor: {v}")

url=["https://dog.ceo/api/breeds/image/random", "https://official-joke-api.appspot.com/random_joke", "https://api.nationalize.io/?name=alejandro"]
for i in range(len(url)):
    print(url[i])
    Api=requests.get(url[i])
    if Api.status_code == 200:
        Api=Api.json()
        Imprimir_Json(Api)
        print("\n")
    else:
        print('Error en la solicitud, detalles:',Api.text)

```

