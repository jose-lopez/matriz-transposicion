'''
Created on 22 feb. 2021

@author: jose-lopez
'''
import copy

if __name__ == '__main__':
    pass


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


# matriz = open("data/simplificado-csv-msdos.csv", 'r', encoding="utf8")
# matriz = open("data/completo.csv", 'r', encoding="utf8")
# matriz = open("data/registros-matriz-simplificado.csv", 'r', encoding="utf8")
matriz = open("data/registros-matriz-indicaciones.csv", 'r', encoding="utf8")
# etiquetas_matriz = open(
#    "data/etiquetas-matriz-simplificado.csv", 'r', encoding="utf8")
etiquetas_matriz = open(
    "data/etiquetas-matriz-general.csv", 'r', encoding="utf8")
cods_sec = open("data/codigos-sec.csv", 'r', encoding="utf16")
# cods_sec = open("data/simplificado-csv-1.csv", 'r', encoding="utf16")
cods_alimts = open("data/etiquetas_alimentos.txt", 'r')
cods_veg_est = open("data/codigos-veg-estacionalidad.txt",
                    'r', encoding="utf16")
registros = []
procesando_etiquetas = True
etiquetas = ""
codigos_sec = []
codigos_alimentos = []
codigos_veg_est = []
bloque = "SEC"
END = "N_RIO"
entrevistas = []
etiquetas = etiquetas_matriz.readline().split(";")

for linea in cods_sec:
    cdgo_sec = linea.split("=")[0]
    if codigos_sec.count(cdgo_sec) == 0:
        codigos_sec.append(linea.split("=")[0])
    else:
        print("Codigo {} esta repetido".format(cdgo_sec))

for linea in cods_veg_est:
    cdgo_veg_est = linea.split("=")[0]
    if codigos_veg_est.count(cdgo_veg_est) == 0:
        codigos_veg_est.append(linea.split("=")[0])
    else:
        print("Codigo {} esta repetido".format(cdgo_veg_est))

for linea in cods_alimts:
    codigo = linea.split("=")[0]
    if codigos_alimentos.count(codigo) == 0:
        codigos_alimentos.append(linea.split("=")[0])
    else:
        print("Codigo {} esta repetido".format(codigo))

for linea in matriz:

    entrevista = Entrevista()
    bloque_en_proceso = {}
    alimento_cod = ""
    indice_variable = 1  # Numeral esperado para la variable en curso
    alimentos = []  # Contendra los alimentos que el entrevistado vende
    procesando_alimentos = False
    inicio_analisis_alimento = False
    campos = linea.split(";")
    alimento_activo = False

    if procesando_etiquetas:
        # Se reporta estado de las etiquetas de las variables

        irregularidades = {}
        reporte = open("reporte_etiquetas.txt", "w")
        reporte.write("Codigo;Variable;Condicion" + "\n")
        num_campo = 0
        entrevista.co_id = campos[num_campo]
        alimento_activo = False

        for etiqueta in etiquetas:

            if etiqueta != "SALIDA" and not procesando_alimentos:
                if codigos_sec.count(etiqueta) == 0:
                    irregularidades[etiqueta] = "Etiqueta SOC {} no esta en la leyenda".format(
                        etiqueta)
                bloque_en_proceso[etiqueta] = campos[num_campo]
                num_campo = num_campo + 1
            elif etiqueta == "SALIDA":
                bloque_en_proceso[etiqueta] = campos[num_campo]
                num_campo = num_campo + 1
                # Se guarda en la entrevista el bloque SEC.
                entrevista.sec = copy.deepcopy(bloque_en_proceso)
                bloque_en_proceso.clear()
                # bloque_en_proceso[etiqueta] = campos[num_campo]Inicia
                # analisis de etiquetas de alimentos
                bloque = "ALIMENTOS"
                procesando_alimentos = True
                inicio_analisis_alimento = True
                cambio_alimento = False
            elif bloque == "ALIMENTOS" and etiqueta != "AOESV1":

                etiqueta_cod_raiz = etiqueta.split(str("1"))[0]
                etiqueta_cod_raiz_1 = etiqueta.split(str("_1"))[0]

                if inicio_analisis_alimento:

                    if codigos_alimentos.count(etiqueta_cod_raiz) != 0:
                        alimento_cod = etiqueta_cod_raiz
                        piso = False
                    elif codigos_alimentos.count(etiqueta_cod_raiz_1) != 0:
                        alimento_cod = etiqueta_cod_raiz_1
                        piso = True
                    else:
                        print(
                            etiqueta, " : Etiqueta primer alimento no esta en la lista de alimentos")
                        print(
                            "Por favor corregir matriz o actualizar la lista de los codigos de alimento")
                        exit()
                    if campos[num_campo] == "1":
                        alimento_activo = True
                        bloque_en_proceso[alimento_cod] = alimento_cod
                    num_campo = num_campo + 1
                    inicio_analisis_alimento = False
                    indice_variable += 1
                else:
                    # Este bloque procesa la totalidad de los alimentos.

                    if etiqueta_cod_raiz == alimento_cod or \
                            etiqueta_cod_raiz_1 == alimento_cod:
                        if indice_variable > 9:
                            cambio_alimento = False
                    elif codigos_alimentos.count(etiqueta_cod_raiz) != 0 or \
                            codigos_alimentos.count(etiqueta_cod_raiz_1) != 0:
                        cambio_alimento = True

                    if etiqueta.startswith(alimento_cod) \
                            and not cambio_alimento:
                        if not piso:
                            numeral_variable = etiqueta.split(alimento_cod)[1]
                            etqta = alimento_cod
                        else:
                            list_numeral_variable = etiqueta.split(
                                alimento_cod + "_")
                            if len(list_numeral_variable) > 1:
                                numeral_variable = list_numeral_variable[1]
                            else:
                                numeral_variable = list_numeral_variable[0]
                            etqta = alimento_cod + "_"

                        if numeral_variable.isdigit():
                            if int(numeral_variable) != indice_variable:
                                numero_saltos = int(
                                    numeral_variable) - indice_variable
                                irregularidades[alimento_cod] = alimento_cod + \
                                    ";" + etiqueta + ";" + "SALTO"
                                x = indice_variable
                                y = int(numeral_variable)
                                if alimento_activo:
                                    for salto in range(x, y):
                                        bloque_en_proceso[etqta +
                                                          str(salto)] = "SALTO"
                                    bloque_en_proceso[etiqueta] = campos[num_campo]
                                indice_variable = indice_variable + 1 + numero_saltos
                                num_campo = num_campo + 1
                            elif int(numeral_variable) == indice_variable:
                                if alimento_activo:
                                    bloque_en_proceso[etiqueta] = campos[num_campo]
                                num_campo = num_campo + 1
                                indice_variable += 1
                        elif numeral_variable.endswith("*"):
                            irregularidades[alimento_cod] = alimento_cod + \
                                ";" + etiqueta + ";" + "INSERCION *"
                            if alimento_activo:
                                bloque_en_proceso[etiqueta] = campos[num_campo]
                            num_campo = num_campo + 1
                        else:
                            irregularidades[alimento_cod] = alimento_cod + \
                                ";" + etiqueta + ";" + "IRREGULAR"
                            if alimento_activo:
                                bloque_en_proceso[etiqueta] = campos[num_campo]
                            num_campo = num_campo + 1
                            indice_variable += 1
                    elif not etiqueta.startswith(alimento_cod) \
                            and not cambio_alimento:
                        irregularidades[alimento_cod] = alimento_cod + \
                            ";" + etiqueta + ";" + "IRREGULAR"
                        if alimento_activo:
                            bloque_en_proceso[etiqueta] = campos[num_campo]
                        num_campo = num_campo + 1
                        indice_variable += 1
                    else:
                        if len(bloque_en_proceso) != 0:
                            entrevista.alimentos.append(
                                copy.deepcopy(bloque_en_proceso))
                            bloque_en_proceso.clear()

                        alimento_activo = False

                        if codigos_alimentos.count(etiqueta_cod_raiz) != 0:
                            alimento_cod = etiqueta_cod_raiz
                            if campos[num_campo] == "1":
                                alimento_activo = True
                                bloque_en_proceso[alimento_cod] = alimento_cod
                            num_campo = num_campo + 1
                            indice_variable = 2
                            piso = False
                        elif codigos_alimentos.count(etiqueta_cod_raiz_1) != 0:
                            alimento_cod = etiqueta_cod_raiz_1
                            if campos[num_campo] == "1":
                                alimento_activo = True
                                bloque_en_proceso[alimento_cod] = alimento_cod
                            num_campo = num_campo + 1
                            indice_variable = 2
                            piso = True
                        cambio_alimento = False
            elif etiqueta == "AOESV1":
                if len(bloque_en_proceso) != 0:
                    entrevista.alimentos.append(
                        copy.deepcopy(bloque_en_proceso))
                    bloque_en_proceso.clear()
                bloque = "VEGETACION"
                bloque_en_proceso[etiqueta] = campos[num_campo]
                num_campo = num_campo + 1
            elif etiqueta != "ESTACIONALIDAD" and bloque == "VEGETACION":
                if codigos_veg_est.count(etiqueta) == 0:
                    irregularidades[etiqueta] = "Etiqueta " + \
                        etiqueta + "no esta en la leyenda"
                bloque_en_proceso[etiqueta] = campos[num_campo]
                num_campo = num_campo + 1
            elif etiqueta == "ESTACIONALIDAD":
                bloque = "CLIMATICO"
                entrevista.vegetacion = copy.deepcopy(bloque_en_proceso)
                bloque_en_proceso.clear()
                bloque_en_proceso[etiqueta] = campos[num_campo]
                num_campo = num_campo + 1
            else:  # Solo resta N_RIO
                etiqueta = etiqueta.replace("\n", "")
                if codigos_veg_est.count(etiqueta) == 0:
                    irregularidades[etiqueta] = "Etiqueta " + \
                        etiqueta + "no esta en la leyenda"
                campos[num_campo] = campos[num_campo].replace(
                    "\n", "")
                bloque_en_proceso[etiqueta] = campos[num_campo].replace(
                    "\n", "")
                entrevista.climatico = copy.deepcopy(bloque_en_proceso)

        # Entrevista actual se agrega a las entrevistas procesadas
        entrevistas.append(copy.deepcopy(entrevista))

for value in irregularidades.values():
    print(value)
    reporte.write(value + "\n")

reporte.close()
matriz.close()
etiquetas_matriz.close()
cods_sec.close()
cods_alimts.close()
cods_veg_est.close()
