from scipy.ndimage.interpolation import rotate
import pandas as pd
from photutils.detection import find_peaks
import math
from astropy.stats import sigma_clipped_stats

def rotar_imagen(data):
    x = [] # voy a meter en esta lista la posicion de las estrellas mas brillantes en orden descendiente
    y = []
    
    #deteccion de estrellas
    for i in range(len(data)):
        mean, median, std = sigma_clipped_stats(data[i], sigma=3.0)
        threshold = median + (5. * std)
        tbl = find_peaks(data[i], threshold, box_size=11)

        table_to_pandas = tbl.to_pandas() # paso la tabla de astropy a pandas para que sea mas comodo trabajar
        pandas_ordenado = table_to_pandas.sort_values('peak_value', ascending=False) # ordeno los valores de los picos obtenidos de orden descendiente
        pandas_ordenado = pandas_ordenado.reset_index() # reseteo de los indices del archivo de pandas
        x.append(pandas_ordenado['x_peak']) # asigno las coordenadas de cada pico a mi lista x
        y.append(pandas_ordenado['y_peak']) # asigno las coordenadas de cada pico a mi lista y
        
    angulo = [] # defino una lista vacia en la que voy a tener en cuenta el angulo de rotacion que hay que aplicar a cada imagen
    
    for i in range(len(data)):
        #angulo.append(math.degrees(math.atan2(y[i][1] - y[i][0], x[i][1] - x[i][0]))) # calculo el angulo entre dos puntos de la misma imagen
        angulo.append(round(math.degrees(math.atan2(y[i][1] - y[i][0], x[i][1] - x[i][0])))) # calculo el angulo entre dos puntos de la misma imagen
        
    data_derotado = [data[0], ] # aquí uso la funcion rotate(imagen, angulo_de_rotacion) de la biblioteca scipy
    for i in range(1,len(data)):
        if (angulo[0]-angulo[i] < 0):  # Comprobar esto
            data_derotado.append(rotate(data[i], angle=angulo[0]-angulo[i]))
            print(f"La imagen {i} está rotada {angulo[0]-angulo[i]} grados")
        else:
            data_derotado.append(rotate(data[i], angle=angulo[0]-angulo[i]))
            print(f"La imagen {i} está rotada {angulo[0]-angulo[i]} grados")
    return data_derotado