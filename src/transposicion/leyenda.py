'''
Created on 13 mar. 2021

@author: jose-lopez
'''
from copy import deepcopy


class Leyenda:
    '''
    Esta clase modela un objeto que gestiona las \
    etiquetas que describen las variables y sus parametros

    '''

    def __init__(self, ruta_leyenda):
        '''
        Constructor
        '''
        self._ruta_leyenda = ruta_leyenda

        self._leyenda = []

    @property
    def ruta_leyenda(self):
        return self._ruta_leyenda

    @ruta_leyenda.setter
    def ruta_leyenda(self, ruta_leyenda):
        self._ruta_leyenda = ruta_leyenda

    @property
    def leyenda(self):
        return self._leyenda

    @leyenda.setter
    def leyenda(self, leyenda):
        self._leyenda = leyenda

    def cargar_leyenda(self):

        variable_en_proceso = {}
        valores_variable_en_proceso = {}
        # bloque_en_proceso = {}

        variable_activa = False
        contador_lineas_leyenda = 0

        with open(self.ruta_leyenda, 'r', encoding="utf16") as f:
            lines = f.readlines()
            nro_ultima_linea = len(lines)

        for linea in lines:

            contador_lineas_leyenda += 1

            if not linea.startswith(";") and not variable_activa:
                variable_activa = True
                codigo_variable = linea.split(";")[0]
                valor_variable = linea.split(";")[1]
                valores_variable_en_proceso[codigo_variable] = valor_variable
            else:  # Se asignan los valores para la variable en proceso.
                if linea.startswith(";") and variable_activa and not contador_lineas_leyenda == nro_ultima_linea:
                    if not linea.find("=") == -1:
                        registro = linea.split(";")[1]
                        valores_variable_en_proceso[registro.split(
                            "=")[0]] = registro.split("=")[1]
                    else:
                        valores_variable_en_proceso["en_blanco"] = ""
                        print("variable " + codigo_variable +
                              ", sin leyenda en linea: " + str(contador_lineas_leyenda))
                        # exit()
                elif linea.startswith(";") and variable_activa and contador_lineas_leyenda == nro_ultima_linea:
                    if not linea.find("=") == -1:
                        registro = linea.split(";")[1]
                        valores_variable_en_proceso[registro.split(
                            "=")[0]] = registro.split("=")[1]
                        variable_en_proceso[codigo_variable] = valores_variable_en_proceso
                        self.leyenda.append(deepcopy(variable_en_proceso))
                    else:
                        valores_variable_en_proceso["en_blanco"] = ""
                        print("variable " + codigo_variable +
                              ", sin leyenda en linea: " + str(contador_lineas_leyenda))
                        # exit()
                else:  # Se pasa al siguiente bloque variable/valores
                    variable_en_proceso[codigo_variable] = valores_variable_en_proceso
                    self.leyenda.append(deepcopy(variable_en_proceso))
                    variable_en_proceso.clear()
                    valores_variable_en_proceso.clear()
                    codigo_variable = linea.split(";")[0]
                    valor_variable = linea.split(";")[1]
                    valores_variable_en_proceso[codigo_variable] = valor_variable

        return self.leyenda

    def etiquetas_key(self, key):
        etiquetas = None
        for coleccion in self.leyenda:
            if key in coleccion:
                etiquetas = coleccion[key]
        return etiquetas
