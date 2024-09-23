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