from astropy.stats import sigma_clipped_stats
from photutils.detection import find_peaks
import numpy as np

def shift_image(X, dx, dy):
    X = np.roll(X, dy, axis=0)
    X = np.roll(X, dx, axis=1)
    if dy>0:
        X[:dy, :] = 0
    elif dy<0:
        X[dy:, :] = 0
    if dx>0:
        X[:, :dx] = 0
    elif dx<0:
        X[:, dx:] = 0
    return X

def desplazar_imagen(data):
    x = [] #hago una nueva lista vacia para meter de nuevo las coordenadas de las estrellas
    y = []
    
    for i in range(len(data)):
        mean, median, std = sigma_clipped_stats(data[i], sigma=3.0)
        threshold = median + (5. * std)
        tbl = find_peaks(data[i], threshold, box_size=11) 
        x.append(tbl[np.where(tbl['peak_value'] == tbl['peak_value'].max())[0][0]]['x_peak']) #solo me hace falta un punto, el mas brillante de cada imagen para desplazarla
        y.append(tbl[np.where(tbl['peak_value'] == tbl['peak_value'].max())[0][0]]['y_peak'])
    
    data_shift = [data[0], ]
    
    for i in range(1, len(data)):
        data_shift.append(shift_image(data[i], x[0]-x[i], y[0]-y[i])) #mediante la funcion shift_image desplazo cada imagen con respecto la primera
        print(f"La imagen {i} se ha desplazado en (x, y) = ({x[0]-x[i]}, {y[0]-y[i]})")
    return data_shift