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
