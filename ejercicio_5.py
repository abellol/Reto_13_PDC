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

