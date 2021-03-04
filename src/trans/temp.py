'''
Created on 22 feb. 2021

@author: jose-lopez
'''


class Entrevista:

    '''
    Esta clase modela a una entrevista mediante un código[
    y cuatro diccionarios: socio-económico-cultural,
    alimentos, vegetación y climático.
    '''

    def __init__(self):
        self.__co_id = ""
        self.__sec = {}
        self.__alimentos = {}
        self.__vegetacion = {}
        self.__climatico = {}

    @property
    def co_id(self):
        return self.__co_id

    @co_id.setter
    def co_id(self, co_id):
        self.__co_id = co_id

    @property
    def sec(self):
        return self.__sec

    @sec.setter
    def sec(self, sec):
        self.__sec = sec

    @property
    def alimentos(self):
        return self.__alimentos

    @alimentos.setter
    def alimentos(self, alimentos):
        self.__alimentos = alimentos

    @property
    def vegetacion(self):
        return self.__vegetacion

    @vegetacion.setter
    def vegetacion(self, vegetacion):
        self.__vegetacion = vegetacion

    @property
    def climatico(self):
        return self.__climatico

    @climatico.setter
    def climatico(self, climatico):
        self.__climatico = climatico


matriz = open("data/simplificado-csv-1.csv")
# matriz = open("data/completo.csv")
cods_sec = open("data/codigos-sec.csv", "r")
# cods_sec = open("data/simplificado-csv-1.csv", "r")
codigos_alimentos = open("data/etiquetas_alimentos.txt", "r")
cods_veg_est = open("data/codigos-veg-estacionalidad.csv", "r")
registros = []
procesando_etiquetas = True
etiquetas = ""
codigos_sec = []
codigos = []
codigos_veg_est = []

print("Hola")
