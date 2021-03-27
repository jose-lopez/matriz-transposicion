'''
Created on 16 mar. 2021

@author: jose-lopez
'''


class Entrevista:

    '''
    Esta clase modela a una entrevista mediante un código
    y cuatro diccionarios: socio-económico-cultural,
    alimentos, vegetación y climático.
    '''

    def __init__(self):
        self.__co_id = ""
        self.__sec = {}
        self.__alimentos = []
        self.__vegetacion = {}
        self.__climatico = {}
        self.__sec_etiq = {}
        self.__alimentos_etiq = []
        self.__vegetacion_etiq = {}
        self.__climatico_etiq = {}

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

    @property
    def sec_etiq(self):
        return self.__sec_etiq

    @sec_etiq.setter
    def sec_etiq(self, sec_etiq):
        self.__sec_etiq = sec_etiq

    @property
    def alimentos_etiq(self):
        return self.__alimentos_etiq

    @alimentos_etiq.setter
    def alimentos_etiq(self, alimentos_etiq):
        self.__alimentos_etiq = alimentos_etiq

    @property
    def vegetacion_etiq(self):
        return self.__vegetacion_etiq

    @vegetacion_etiq.setter
    def vegetacion_etiq(self, vegetacion_etiq):
        self.__vegetacion_etiq = vegetacion_etiq

    @property
    def climatico_etiq(self):
        return self.__climatico_etiq

    @climatico_etiq.setter
    def climatico_etiq(self, climatico_etiq):
        self.__climatico_etiq = climatico_etiq
