'''
Created on 22 feb. 2021

@author: jose-lopez
'''
from copy import deepcopy
from pickle import TRUE
import copy

from transposicion.entrevista import Entrevista


class Matriz:
    '''
    Esta clase modela un objeto que gestiona las \
    entrevistas de la matriz

    '''

    def __init__(self, ruta_matriz, ruta_codigos_sec, ruta_codigos_alimentos, ruta_codigos_veg_estac, campo_excep, num_max_var):
        '''
        Constructor
        '''
        self._entrevistas = []

        self._ruta_matriz = ruta_matriz

        self._ruta_codigos_sec = ruta_codigos_sec

        self._ruta_codigos_alimentos = ruta_codigos_alimentos

        self._ruta_codigos_veg_estac = ruta_codigos_veg_estac

        self._max_nro_variables_por_alimento = 0

        self._alimentos_orden = []

        self._codigos_excep = []

        self._campo_excep = campo_excep

        self._num_max_var = num_max_var

    @property
    def num_max_var(self):
        return self._num_max_var

    @num_max_var.setter
    def num_max_var(self, num_max_var):
        self._num_max_var = num_max_var

    @property
    def campo_excep(self):
        return self._campo_excep

    @campo_excep.setter
    def campo_excep(self, campo_excep):
        self._campo_excep = campo_excep

    @property
    def codigos_excep(self):
        return self._codigos_excep

    @codigos_excep.setter
    def codigos_excep(self, codigos_excep):
        self._codigos_excep = codigos_excep

    @property
    def max_nro_variables_por_alimento(self):
        return self._max_nro_variables_por_alimento

    @max_nro_variables_por_alimento.setter
    def max_nro_variables_por_alimento(self, max_nro_variables_por_alimento):
        self._max_nro_variables_por_alimento = max_nro_variables_por_alimento

    @property
    def alimentos_orden(self):
        return self._alimentos_orden

    @alimentos_orden.setter
    def alimentos_orden(self, alimentos_orden):
        self._alimentos_orden = alimentos_orden

    @property
    def ruta_matriz(self):
        return self._ruta_matriz

    @ruta_matriz.setter
    def ruta_matriz(self, ruta_matriz):
        self._ruta_matriz = ruta_matriz

    @property
    def codigos_sec(self):
        return self._ruta_codigos_sec

    @codigos_sec.setter
    def codigos_sec(self, ruta_codigos_sec):
        self._ruta_codigos_sec = ruta_codigos_sec

    @property
    def codigos_alimentos(self):
        return self._ruta_codigos_alimentos

    @codigos_alimentos.setter
    def codigos_alimentos(self, ruta_codigos_alimentos):
        self._ruta_codigos_alimentos = ruta_codigos_alimentos

    @property
    def codigos_veg_estac(self):
        return self._ruta_codigos_veg_estac

    @codigos_veg_estac.setter
    def codigos_veg_estac(self, ruta_codigos_veg_estac):
        self._ruta_codigos_veg_estac = ruta_codigos_veg_estac

    @property
    def entrevistas(self):
        return self._entrevistas

    @entrevistas.setter
    def entrevistas(self, entrevistas):
        self._entrevistas = entrevistas

    def codigos_matriz_en_codigos_alimentos(self, etiquetas, codigos_alimentos):

        etiquetas_ = []

        for etiqueta in etiquetas:
            if not etiqueta == "AOESV1":
                if etiqueta.endswith("8"):
                    etiquetas_.append(etiqueta)
            else:
                break

        cant_codgs_ausentes = 0

        for variable in etiquetas_:

            etiqueta_no_piso = variable.split(str("8"))[0]
            etiqueta_piso = variable.split(str("_8"))[0]

            codigo_presente = False

            if etiqueta_no_piso in codigos_alimentos:
                codigo_presente = True

            if etiqueta_piso in codigos_alimentos:
                codigo_presente = True

            if not codigo_presente:
                print(
                    "Codigo {} presente en la matriz pero no en la leyanda".format(variable))
                cant_codgs_ausentes += 1

        print("Cantidad de codigos de la matriz no presentes en la leyenda: {}".format(
            cant_codgs_ausentes))

    def codigos_alimentos_en_codigos_matriz(self, etiquetas, codigos_alimentos):
        cant_codigos_p = 0
        cant_codigos_np = 0
        for codigo in codigos_alimentos:
            codigo_piso = codigo + "_1"
            codigo_no_piso = codigo + "1"
            if codigo_piso in etiquetas or codigo_no_piso in etiquetas:
                cant_codigos_p += 1
            else:
                print("Codigo {} no esta en la matriz".format(codigo) + "\n")
                cant_codigos_np += 1
        print("Codigos presentes en la matriz: {}/{}".format(cant_codigos_p,
                                                             len(codigos_alimentos)))
        print("Codigos presentes en la matriz: {}/{}".format(cant_codigos_np,
                                                             len(codigos_alimentos)))

    def procesar_entrevistas(self, reportar_etiquetas):

        matriz = open(self.ruta_matriz, 'r', encoding="utf8")
        cods_sec = open(self.codigos_sec, 'r', encoding="utf16")
        cods_alimts = open(self.codigos_alimentos, 'r')
        cods_veg_est = open(self.codigos_veg_estac,
                            'r', encoding="utf16")
        if reportar_etiquetas:
            reporte = open("reporte_etiquetas.txt", "w")
            reporte.write("Codigo;Variable;Condicion" + "\n")

        codigos_sec = []
        codigos_alimentos = []
        codigos_veg_est = []
        bloque = "SEC"
        # etiquetas = etiquetas_matriz.readline().split(";")
        etiquetas = matriz.readline().split(";")
        reporte = open("reporte_etiquetas.txt", "w")
        reporte.write(str(etiquetas))
        reporte.close()
        nro_variables_por_alimento = 0
        primera_entrevista = True

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

        self.codigos_matriz_en_codigos_alimentos(etiquetas, codigos_alimentos)

        for linea in matriz:

            entrevista = Entrevista()
            bloque_en_proceso = {}
            alimento_cod = ""
            indice_variable = 1  # Numeral esperado para la variable en curso
            procesando_alimentos = False
            inicio_analisis_alimento = False
            campos = linea.split(";")
            alimento_activo = False
            irregularidades = {}
            num_campo = 0
            entrevista.co_id = campos[num_campo]
            alimento_activo = False
            alimento_orden = {}

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
                            alimento_orden["ALIMENTO"] = alimento_cod
                            piso = False
                        elif codigos_alimentos.count(etiqueta_cod_raiz_1) != 0:
                            alimento_cod = etiqueta_cod_raiz_1
                            alimento_orden["ALIMENTO"] = alimento_cod
                            piso = True
                        else:
                            print(
                                etiqueta, " : Etiqueta primer alimento no esta en la lista de alimentos")
                            print(
                                "Por favor corregir matriz o actualizar la lista de los codigos de alimento")
                            exit()
                        if campos[num_campo] == "1":
                            alimento_activo = True
                            bloque_en_proceso["ALIMENTO1"] = alimento_cod
                        nro_variables_por_alimento += 1
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
                                numeral_variable = etiqueta.split(alimento_cod)[
                                    1]
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
                                    # x = indice_variable
                                    # y = int(numeral_variable)
                                    if alimento_activo:
                                        for salto in range(indice_variable, int(numeral_variable)):
                                            bloque_en_proceso[etqta +
                                                              str(salto)] = ""
                                        bloque_en_proceso[etiqueta] = campos[num_campo]
                                    if primera_entrevista:
                                        for salto in range(indice_variable, int(numeral_variable)):
                                            nro_variables_por_alimento += 1
                                        nro_variables_por_alimento += 1
                                    indice_variable = indice_variable + 1 + numero_saltos
                                    num_campo = num_campo + 1
                                elif int(numeral_variable) == indice_variable:
                                    if alimento_activo:
                                        bloque_en_proceso[etiqueta] = campos[num_campo]
                                    if primera_entrevista:
                                        nro_variables_por_alimento += 1
                                    num_campo = num_campo + 1
                                    indice_variable += 1
                            elif numeral_variable.endswith("*"):
                                irregularidades[alimento_cod] = alimento_cod + \
                                    ";" + etiqueta + ";" + "INSERCION *"
                                if alimento_activo:
                                    bloque_en_proceso[etiqueta] = campos[num_campo]
                                if primera_entrevista:
                                    nro_variables_por_alimento += 1
                                num_campo = num_campo + 1
                            else:
                                irregularidades[alimento_cod] = alimento_cod + \
                                    ";" + etiqueta + ";" + "IRREGULAR"
                                if alimento_activo:
                                    bloque_en_proceso[etiqueta] = campos[num_campo]
                                if primera_entrevista:
                                    nro_variables_por_alimento += 1
                                num_campo = num_campo + 1
                                indice_variable += 1
                        elif not etiqueta.startswith(alimento_cod) \
                                and not cambio_alimento:
                            irregularidades[alimento_cod] = alimento_cod + \
                                ";" + etiqueta + ";" + "IRREGULAR"
                            if alimento_activo:
                                bloque_en_proceso[etiqueta] = campos[num_campo]
                            if primera_entrevista:
                                nro_variables_por_alimento += 1
                            num_campo = num_campo + 1
                            indice_variable += 1
                        else:
                            if len(bloque_en_proceso) != 0:
                                entrevista.alimentos.append(
                                    copy.deepcopy(bloque_en_proceso))
                                bloque_en_proceso.clear()

                            alimento_activo = False

                            if primera_entrevista:
                                alimento_orden["nro_variables"] = nro_variables_por_alimento
                                self.alimentos_orden.append(
                                    deepcopy(alimento_orden))
                                alimento_orden.clear()
                                if nro_variables_por_alimento > self.max_nro_variables_por_alimento:
                                    self.max_nro_variables_por_alimento = nro_variables_por_alimento
                                if nro_variables_por_alimento >= self.num_max_var:
                                    print("Alimento: {} posee {} variables".format(
                                        alimento_cod, nro_variables_por_alimento))
                                    self.codigos_excep.append(alimento_cod)
                                nro_variables_por_alimento = 0

                            if codigos_alimentos.count(etiqueta_cod_raiz) != 0:
                                alimento_cod = etiqueta_cod_raiz
                                if campos[num_campo] == "1":
                                    alimento_activo = True
                                    bloque_en_proceso["ALIMENTO1"] = alimento_cod
                                if primera_entrevista:
                                    alimento_orden["ALIMENTO"] = alimento_cod
                                    nro_variables_por_alimento += 1
                                num_campo = num_campo + 1
                                indice_variable = 2
                                piso = False
                            elif codigos_alimentos.count(etiqueta_cod_raiz_1) != 0:
                                alimento_cod = etiqueta_cod_raiz_1
                                if campos[num_campo] == "1":
                                    alimento_activo = True
                                    bloque_en_proceso["ALIMENTO1"] = alimento_cod
                                if primera_entrevista:
                                    alimento_orden["ALIMENTO"] = alimento_cod
                                    nro_variables_por_alimento += 1
                                num_campo = num_campo + 1
                                indice_variable = 2
                                piso = True
                            cambio_alimento = False
                elif etiqueta == "AOESV1":
                    if len(bloque_en_proceso) != 0:
                        entrevista.alimentos.append(
                            copy.deepcopy(bloque_en_proceso))
                    if primera_entrevista:
                        alimento_orden["nro_variables"] = nro_variables_por_alimento
                        self.alimentos_orden.append(
                            deepcopy(alimento_orden))
                        if nro_variables_por_alimento > self.max_nro_variables_por_alimento:
                            self.max_nro_variables_por_alimento = nro_variables_por_alimento
                        if nro_variables_por_alimento >= self.num_max_var:
                            print("Alimento: {} posee {} variables".format(
                                alimento_cod, nro_variables_por_alimento))
                            self.codigos_excep.append(alimento_cod)
                        primera_entrevista = False
                        alimento_orden.clear()
                    bloque_en_proceso.clear()
                    bloque = "VEGETACION"
                    bloque_en_proceso[etiqueta] = campos[num_campo]
                    num_campo = num_campo + 1
                elif etiqueta != "ESTACIONALIDAD" and bloque == "VEGETACION":
                    if codigos_veg_est.count(etiqueta) == 0:
                        irregularidades[etiqueta] = "Etiqueta " + \
                            etiqueta + "no esta en la entrevistas"
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
                            etiqueta + "no esta en la entrevistas"
                    campos[num_campo] = campos[num_campo].replace(
                        "\n", "")
                    bloque_en_proceso[etiqueta] = campos[num_campo].replace(
                        "\n", "")
                    entrevista.climatico = copy.deepcopy(bloque_en_proceso)

            # Entrevista actual se agrega a las entrevistas procesadas
            self.entrevistas.append(copy.deepcopy(entrevista))

        if reportar_etiquetas:
            for value in irregularidades.values():
                print(value)
                reporte.write(value + "\n")

        if reportar_etiquetas:
            reporte.close()
        matriz.close()
        cods_sec.close()
        cods_alimts.close()
        cods_veg_est.close()

        return self.entrevistas

    def etiquetar_campos(self, leyenda, etiquetar_variables):

        leyenda.cargar_leyenda()

        # etiquetas = leyenda.etiquetas_key("RESID")

        nro_entrevista = 0

        for entrevista in self.entrevistas:

            nro_entrevista += 1

            # print("Entrevista: " + entrevista.co_id)

            seccion = "SEC"

            bloques = [entrevista.sec, entrevista.vegetacion,
                       entrevista.climatico, entrevista.alimentos]

            for bloque in bloques:

                bloque_ = {}

                if seccion != "Alimentos":

                    for key, value in bloque.items():
                        etiquetas = leyenda.etiquetas_key(key)
                        if not value.isspace() and etiquetas is not None:
                            if value.strip() in etiquetas.keys():
                                etiqueta_value = etiquetas[value.strip()]
                            else:
                                print(
                                    "Advertencia: En la entrevista {} el valor {} en la variable {} no tiene etiqueta asignada".format(nro_entrevista, value, key))
                                etiqueta_value = value
                        else:
                            etiqueta_value = value

                        if etiquetas is not None:
                            if key.strip() in etiquetas.keys():
                                key_etiq = etiquetas[key.strip()]
                                bloque_[key_etiq] = etiqueta_value
                            else:
                                bloque_[key] = etiqueta_value
                        else:
                            bloque_[key] = etiqueta_value

                else:

                    bloque_ = []
                    alimento_etiq = {}

                    for alimento in bloque:

                        caso_especial = True

                        num_variable_alimento = 1

                        for key, value in alimento.items():
                            if not len(alimento) == self.num_max_var:
                                alimento_etiq["ALIMENTO" +
                                              str(num_variable_alimento)] = value
                            else:
                                if num_variable_alimento == (self.campo_excep + 1) and caso_especial:
                                    alimento_etiq["ALIMENTO" +
                                                  str(self.campo_excep) + "*"] = value
                                    num_variable_alimento -= 1
                                    caso_especial = False
                                else:
                                    alimento_etiq["ALIMENTO" +
                                                  str(num_variable_alimento)] = value

                            num_variable_alimento += 1

                        for key, value in alimento_etiq.items():
                            etiquetas = leyenda.etiquetas_key(key)
                            if not value.isspace() and etiquetas is not None:
                                if value.strip() in etiquetas.keys():
                                    etiqueta_value = etiquetas[value.strip()]
                                else:
                                    print(
                                        "Advertencia: En la entrevista {} el valor {} en la variable {} no tiene etiqueta asignada".format(nro_entrevista, value, key))
                                    #print("Se mantiene el valor presente en la variable")
                                    etiqueta_value = value
                            else:
                                etiqueta_value = value

                            alimento_etiq[key] = etiqueta_value

                        diferencia_variables = self.max_nro_variables_por_alimento - \
                            len(alimento)

                        if diferencia_variables > 0:
                            for indice in range(diferencia_variables):
                                key = "ALIMENTO" + \
                                    str(len(alimento) + indice + 1)
                                alimento_etiq[key] = ""
                        elif diferencia_variables < 0:
                            print("En el alimento {} hay mas variables que max. numero de variables".format(
                                alimento_etiq["ALIMENT01"]))
                            print(
                                "Debe revisarse el codigo con el que se procesan las entrevistas")
                            print(
                                "Se recomienda contactar al programador")
                            exit()

                        bloque_.append(deepcopy(alimento_etiq))
                        alimento_etiq.clear()

                if seccion == "SEC":
                    entrevista.sec_etiq = deepcopy(bloque_)
                    seccion = "Vegetacion"
                    # print("** Informacion SEC:")
                    # print(entrevista.sec_etiq.items())
                elif seccion == "Vegetacion":
                    entrevista.vegetacion_etiq = deepcopy(bloque_)
                    seccion = "Climatico"
                    # print("** Informacion vegetacion:")
                    # print(entrevista.vegetacion_etiq.items())
                elif seccion == "Climatico":
                    entrevista.climatico_etiq = deepcopy(bloque_)
                    seccion = "Alimentos"
                    # print("** Informacion climatica:")
                    # print(entrevista.climatico_etiq.items())
                elif seccion == "Alimentos":
                    entrevista.alimentos_etiq = deepcopy(bloque_)

    def reporte_vertical(self, leyenda, r_matriz):

        matriz_v = open(
            r_matriz, 'w', encoding="utf8")

        variables_sec = ""
        variables_alimentos = ""
        variables_veg = ""
        variables_climatico = ""
        registro_sec = ""
        registro_veg = ""
        registro_climatico = ""

        primera_entrevista = True

        leyenda.cargar_leyenda()

        for entrevista in self.entrevistas:

            bloques = [entrevista.sec_etiq, entrevista.vegetacion_etiq,
                       entrevista.climatico_etiq, entrevista.alimentos_etiq]

            variables_vertical = ""

            if primera_entrevista:

                for key in entrevista.sec_etiq.keys():
                    variables_sec = variables_sec + key + ";"

                etiquetas_alimento = leyenda.etiquetas_key("ALIMENTO")
                for indice in range(self.num_max_var - 1):
                    etiqueta = etiquetas_alimento["ALIMENTO" + str(indice + 1)]
                    variables_alimentos = variables_alimentos + etiqueta + ";"

                for key in entrevista.vegetacion_etiq.keys():
                    variables_veg = variables_veg + key + ";"

                for key in entrevista.climatico_etiq.keys():
                    if not key == "N_RIO" and not key == "Nivel del Rio Orinoco":
                        variables_climatico = variables_climatico + key + ";"
                    else:
                        variables_climatico = variables_climatico + key + "\n"
                        primera_entrevista = False

                # Encabezado de la matriz en vertical
                variables_vertical = variables_sec + variables_alimentos + \
                    variables_veg + variables_climatico

                # Se imprime en archivo encabezado de la matriz en vertical
                matriz_v.write(variables_vertical)

            # Se reporta la matriz en vertical

            seccion = "SEC"

            for bloque in bloques:
                registro = ""
                if not seccion == "Alimentos":
                    for key, value in bloque.items():
                        key_strip = key.strip()
                        if not key == "N_RIO" and not key_strip == "Nivel del Rio Orinoco":
                            registro = registro + value + ";"
                        else:
                            registro = registro + value + "\n"
                else:
                    alimentos = []
                    etiquetas_alimentos = leyenda.etiquetas_key("ALIMENTO1")
                    for alimento in bloque:
                        caso_especial = True
                        num_variable_alimento = 1
                        nombre_alimento = alimento["ALIMENTO1"]
                        codigo_alimento = ""

                        for codigo, nombre in etiquetas_alimentos.items():
                            if nombre == nombre_alimento:
                                codigo_alimento = codigo
                                break

                        for key, value in alimento.items():
                            if codigo_alimento not in self.codigos_excep:
                                if not num_variable_alimento == len(alimento):
                                    registro = registro + value + ";"
                            else:
                                if num_variable_alimento == self.campo_excep:
                                    pass
                                elif num_variable_alimento == (self.campo_excep + 1) and caso_especial:
                                    registro = registro + value + ";"
                                    caso_especial = False
                                else:
                                    registro = registro + value + ";"
                            num_variable_alimento += 1

                        alimentos.append(registro)
                        registro = ""

                if seccion == "SEC":
                    registro_sec = deepcopy(registro)
                    seccion = "Vegetacion"
                    # print("** Informacion SEC:")
                    # print(registro_sec)
                elif seccion == "Vegetacion":
                    registro_veg = deepcopy(registro)
                    seccion = "Climatico"
                    # print("** Informacion vegetacion:")
                    # print(registro_veg)
                elif seccion == "Climatico":
                    registro_climatico = deepcopy(registro)
                    seccion = "Alimentos"
                    # print("** Informacion climatica:")
                    # print(registro_climatico)
                elif seccion == "Alimentos":
                    registro_alimentos = deepcopy(alimentos)
                    # print("** Informacion alimentos:")
                    # print(registro_alimentos)

            # Se define el registro general para la entrevsta en curso
            for registro_alimento in registro_alimentos:
                entrevista_etiq = registro_sec + registro_alimento + \
                    registro_veg + registro_climatico
                print(entrevista_etiq)

                # Se imprime la entrevista en curso en la matriz vertical
                matriz_v.write(entrevista_etiq)

        matriz_v.close()

    def reporte_horizontal(self, leyenda, r_matriz):

        matriz_h = open(
            r_matriz, 'w', encoding="utf8")

        variables_sec = ""
        variables_alimentos = ""
        variables_veg = ""
        variables_climatico = ""
        registro_sec = ""
        registro_veg = ""
        registro_climatico = ""

        leyenda.cargar_leyenda()

        primera_entrevista = True

        # Se obtienen los nombres largos para todos los alimentos
        etiquetas_alimentos = leyenda.etiquetas_key("ALIMENTO1")

        for entrevista in self.entrevistas:

            bloques = [entrevista.sec_etiq, entrevista.vegetacion_etiq,
                       entrevista.climatico_etiq, entrevista.alimentos_etiq]

            variables_horizontal = ""
            entrevista_etiq = ""

            if primera_entrevista:

                for key in entrevista.sec_etiq.keys():
                    variables_sec = variables_sec + key + ";"

                # Se obtienen los nombres largos para las posibles variables de
                # un alimento
                etiquetas_alimento = leyenda.etiquetas_key("ALIMENTO")
                for alimento_v in self.alimentos_orden:
                    codigo = alimento_v["ALIMENTO"]
                    value = alimento_v["nro_variables"]
                    if codigo not in self.codigos_excep:
                        for indice in range(int(value)):
                            variable = "ALIMENTO" + str(indice + 1)
                            variables_alimentos = variables_alimentos + \
                                etiquetas_alimento[variable] + ";"
                    else:
                        for indice in range(int(value)):
                            if indice < 2:
                                variable = "ALIMENTO" + str(indice + 1)
                                variables_alimentos = variables_alimentos + \
                                    etiquetas_alimento[variable] + ";"
                            elif indice == 2:
                                variable = "ALIMENTO" + str(indice) + "*"
                                variables_alimentos = variables_alimentos + \
                                    etiquetas_alimento[variable] + ";"
                            else:
                                variable = "ALIMENTO" + str(indice)
                                variables_alimentos = variables_alimentos + \
                                    etiquetas_alimento[variable] + ";"

                for key in entrevista.vegetacion_etiq.keys():
                    variables_veg = variables_veg + key + ";"

                for key in entrevista.climatico_etiq.keys():
                    if not key == "N_RIO" and not key == "Nivel del Rio Orinoco":
                        variables_climatico = variables_climatico + key + ";"
                    else:
                        variables_climatico = variables_climatico + key + "\n"
                        primera_entrevista = False

                # Encabezado de la matriz en horizontal
                variables_horizontal = variables_sec + variables_alimentos + \
                    variables_veg + variables_climatico

                # Se imprime en archivo encabezado de la matriz en horizontal
                matriz_h.write(variables_horizontal)

            # Se reporta la entrevista en curso en la matriz en horizontal

            seccion = "SEC"

            for bloque in bloques:

                registro = ""
                if not seccion == "Alimentos":
                    for key, value in bloque.items():
                        key_strip = key.strip()
                        if not key == "N_RIO" and not key_strip == "Nivel del Rio Orinoco":
                            registro = registro + value + ";"
                        else:
                            registro = registro + value + "\n"
                else:

                    for alimento_v in self.alimentos_orden:
                        key = list(alimento_v.values())[0]
                        nro_variables = list(alimento_v.values())[1]
                        key_value = etiquetas_alimentos[key]
                        for alimento in entrevista.alimentos_etiq:
                            if key_value in alimento.values():
                                cont_variables = 1
                                for value in alimento.values():
                                    if cont_variables <= nro_variables:
                                        registro = registro + value + ";"
                                        cont_variables += 1
                                break
                        else:
                            registro = registro + "0" + ";"
                            for variable in range(nro_variables - 1):
                                registro = registro + "0" + ";"

                if seccion == "SEC":
                    registro_sec = deepcopy(registro)
                    seccion = "Vegetacion"
                    # print("** Informacion SEC:")
                    # print(registro_sec)
                elif seccion == "Vegetacion":
                    registro_veg = deepcopy(registro)
                    seccion = "Climatico"
                    # print("** Informacion vegetacion:")
                    # print(registro_veg)
                elif seccion == "Climatico":
                    registro_climatico = deepcopy(registro)
                    seccion = "Alimentos"
                    # print("** Informacion climatica:")
                    # print(registro_climatico)
                elif seccion == "Alimentos":
                    registro_alimentos = deepcopy(registro)
                    # print("** Informacion alimentos:")
                    # print(registro_alimentos)

            # Se define el registro general para la entrevsta en curso
            entrevista_etiq = registro_sec + registro_alimentos + \
                registro_veg + registro_climatico
            print(entrevista_etiq)

            # Se imprime la entrevista en curso en la matriz vertical
            matriz_h.write(entrevista_etiq)

        matriz_h.close()
