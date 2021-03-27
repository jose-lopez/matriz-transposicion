'''
Created on 16 mar. 2021

@author: jose-lopez
'''
from transposicion.leyenda import Leyenda
from transposicion.matriz import Matriz

if __name__ == '__main__':

    r_leyenda = "data/leyenda_completa.csv"

    # r_matriz = "data/matriz-indicaciones.csv"
    r_matriz = "data/matriz-simplificada.csv"

    r_matriz_v = "data/matriz_vertical_etiquetada.csv"

    r_matriz_h = "data/matriz_horizontal_etiquetada.csv"

    r_codigos_sec = "data/codigos-sec.csv"

    r_codigos_alimentos = "data/etiquetas_alimentos.txt"

    r_codigos_veg_estac = "data/codigos-veg-estacionalidad.txt"

    matriz = Matriz(r_matriz, r_codigos_sec,
                    r_codigos_alimentos, r_codigos_veg_estac)

    # False: No se reporta el estado de las etiquetas
    matriz.procesar_entrevistas(False)

    leyenda = Leyenda(r_leyenda)

    matriz.etiquetar_campos(leyenda)

    # matriz.reporte_vertical(leyenda, r_matriz_v)

    matriz.reporte_horizontal(leyenda, r_matriz_h)
