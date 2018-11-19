import numpy as np
from scipy.optimize import minimize

"""
Funcion Mean Standard Error. Desconocemos las coordenadas del punto x. 
Sabemos las coordenadas (localizacion) de los beacons y las distancias
estimadas desde x a los beacons (en terminos de RSSI - fuerza de la senyal recibida).
"""
def mse(x, pares_coordenadas_beacons, distancias_x_a_beacons):
	mse = 0.0
	for par_coordenada_beacon, distancia_x_a_beacon in zip(pares_coordenadas_beacons,distancias_x_a_beacons):
		distancia_calculada = np.sqrt( np.power(x[0]-par_coordenada_beacon[0],2) + np.power(x[1]-par_coordenada_beacon[1],2) )
		mse += np.power(distancia_calculada - distancia_x_a_beacon, 2.0)
	return mse / len(pares_coordenadas_beacons)
	

def main():
	pares_coordenadas_beacons, mac_beacons = [], []
	
	# Anyado algunos beacons para hacer algunas pruebas 
	pares_coordenadas_beacons.append((50.6,20.8))
	mac_beacons.append("50:17:ff:9f:36:c0") #B1

	pares_coordenadas_beacons.append((50.6,35.5))
	mac_beacons.append("0c:68:03:ea:42:10") #B2

	pares_coordenadas_beacons.append((32.8,35.5))
	mac_beacons.append("0c:68:03:d7:11:a0") #B3

	distancias_x_a_beacons = [15.8533,20.7171,13.5484]

	localizacion_inicial = (np.mean([pares_coordenadas_beacons[0][0],pares_coordenadas_beacons[1][0],pares_coordenadas_beacons[2][0]]), 
	np.mean([pares_coordenadas_beacons[0][1],pares_coordenadas_beacons[1][1],pares_coordenadas_beacons[2][1]]))

	resultado = minimize(
		mse,
		localizacion_inicial,
		args=(pares_coordenadas_beacons, distancias_x_a_beacons),
		method='BFGS',
		options={
			'maxiter': 1e+7	#Iteraciones maximas
		}
	)

	print(resultado)

if __name__ == '__main__':
	main()
