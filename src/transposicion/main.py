'''
Created on 16 mar. 2021

@author: jose-lopez
'''
from transposicion.leyenda import Leyenda
from transposicion.matriz import Matriz

if __name__ == '__main__':

    r_leyenda = "data/leyenda_completa.csv"
    # r_matriz = "data/matriz_completa_nueva.csv"
    # r_matriz = "data/matriz_indicaciones_nueva.csv"
    r_matriz = "data/matriz-simplificada.csv"

    r_matriz_v = "data/matriz_vertical_etiquetada.csv"

    r_matriz_h = "data/matriz_horizontal_etiquetada.csv"

    r_codigos_sec = "data/codigos-sec.csv"

    r_codigos_alimentos = "data/etiquetas_alimentos_NUEVA.txt"

    r_codigos_veg_estac = "data/codigos-veg-estacionalidad.txt"

    campo_excep = 2

    num_max_var = 5

    matriz = Matriz(r_matriz, r_codigos_sec,
                    r_codigos_alimentos, r_codigos_veg_estac, campo_excep, num_max_var)

    # False: No se reporta el estado de las etiquetas
    matriz.procesar_entrevistas(False)

    leyenda = Leyenda(r_leyenda)

    matriz.etiquetar_campos(leyenda, True)

    matriz.reporte_vertical(leyenda, r_matriz_v)

    # matriz.reporte_horizontal(leyenda, r_matriz_h)
