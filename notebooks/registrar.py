import astroalign
from astropy.io import fits as ft


def imprimir_info(p, ii):
    # Esta función imprime por pantalla la info de la transformación que se aplicará.
    # Aunque es innecesaria, sirve para que el usuario sepa que la máquina está haciendo algo.
    print("\nAlineando imagen {:}".format(ii))
    print("Rotación: {:.2f} grados".format(p.rotation * 180.0 / np.pi))
    print("Factor de escala: {:.2f}".format(p.scale))
    print("Traslación: (x, y) = ({:.2f}, {:.2f})".format(*p.translation))


def registra_lista(lista):
    cantidad=len(lista)
    
    # La primera imagen de la lista será la toma de referencia.
    print("\nComenzando la alineación.")
    print("\nLa toma de referencia es {:}".format(lista[0])) 
    blanco=ft.open(lista[0])
    img_blanco=blanco[0].data
    hdr_blanco=blanco[0].header
    blanco.close()
    del(lista[0]) # Quito la imagen de referencia del listado
    imagenes_alineadas = [img_blanco, ]
    for ii in lista:
        ff=ft.open(ii)
        img_torcida=ff[0].data
        hdr_torcida=ff[0].header
        ff.close()
        p, (pos_img, pos_img_rot) = astroalign.find_transform(img_torcida, img_blanco)
#        imprimir_info(p, ii)
        img_aligned = astroalign.register(img_torcida, img_blanco)
        hdr_torcida.add_comment("Registrado con Astroalign y PyReduc")
        imagenes_alineadas.append(img_aligned[0])
#        ft.writeto(f'imagenes\salidaImagenes\aling{}',img_aligned,header=hdr_torcida,overwrite=True)

    print("\nAlineado realizado con éxito")
    return imagenes_alineadas