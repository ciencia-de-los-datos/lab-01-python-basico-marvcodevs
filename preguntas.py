"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import re
from collections import defaultdict


def pregunta_01():
    suma = 0
    with open('data.csv', 'r') as f:
        for linea in f:
            elementos = linea.strip().split()
            if len(elementos) >= 2:
                valor = elementos[1]
                try:
                    suma += int(valor)
                except ValueError:
                    continue
    return suma


def pregunta_02():
    with open('data.csv', 'r') as file:
        apariciones = {}
        for linea in file:
            match = re.match(r'(\w)\s+(\d+)', linea)
            if match:
                letra = match.group(1)
                if letra in apariciones:
                    apariciones[letra] += 1
                else:
                    apariciones[letra] = 1
    return sorted(list(apariciones.items()))


def pregunta_03():
    tuplas = []
    with open('data.csv', 'r') as f:
        for linea in f:
            componentes = re.split(r'\s+', linea.strip())
            primera_columna = componentes[0]
            segunda_columna = int(componentes[1])
            tupla = (primera_columna, segunda_columna)
            tuplas.append(tupla)

    sumatoria_tuplas = {}
    for tupla in tuplas:
        letra, numero = tupla
        if letra in sumatoria_tuplas:
            sumatoria_tuplas[letra] += numero
        else:
            sumatoria_tuplas[letra] = numero
    tuplas_ordenadas = sorted(sumatoria_tuplas.items(), key=lambda x: x[0])

    return tuplas_ordenadas


def pregunta_04():
    registros_por_mes = defaultdict(int)

    with open('data.csv', 'r') as f:
        for linea in f:
            match = re.search(r'\d{4}-\d{2}-\d{2}', linea)
            if match:
                fecha = match.group(0)
                mes = fecha.split('-')[1]
                registros_por_mes[mes] += 1
    registros_ordenados = sorted(registros_por_mes.items())

    return registros_ordenados


def pregunta_05():
    max_min_por_letra = {}

    with open('data.csv', 'r') as f:
        for linea in f:
            componentes = linea.split()
            letra = componentes[0]
            valor_columna_2 = int(componentes[1])
            if letra in max_min_por_letra:
                max_valor, min_valor = max_min_por_letra[letra]
                max_min_por_letra[letra] = (max(max_valor, valor_columna_2), min(min_valor, valor_columna_2))
            else:
                max_min_por_letra[letra] = (valor_columna_2, valor_columna_2)
    lista_tuplas = [(letra,) + valores for letra, valores in max_min_por_letra.items()]

    return sorted(lista_tuplas)


def pregunta_06():
    min_max_por_clave = {}

    with open('data.csv', 'r') as f:
        for linea in f:
            componentes = linea.split()
            diccionario = componentes[4]

            pares_clave_valor = diccionario.split(',')
            for par in pares_clave_valor:
                clave, valor_str = par.split(':')
                valor = int(valor_str)

                if clave in min_max_por_clave:
                    min_valor, max_valor = min_max_por_clave[clave]
                    min_max_por_clave[clave] = (min(min_valor, valor), max(max_valor, valor))
                else:
                    min_max_por_clave[clave] = (valor, valor)

    lista_tuplas = [(clave, min_max_por_clave[clave][0], min_max_por_clave[clave][1]) for clave in min_max_por_clave]
    lista_tuplas_ordenadas = sorted(lista_tuplas)

    return lista_tuplas_ordenadas
    

def pregunta_07():
    asociaciones = defaultdict(list)

    with open('data.csv', 'r') as f:
        for linea in f:
            componentes = linea.split()
            valor_columna_1 = int(componentes[1])
            letra_columna_0 = componentes[0]
            asociaciones[valor_columna_1].append(letra_columna_0)
    lista_tuplas_ordenadas = sorted(asociaciones.items())

    return lista_tuplas_ordenadas


def pregunta_08():
    asociaciones = defaultdict(set)

    with open('data.csv', 'r') as f:
        for linea in f:
            componentes = linea.split()
            valor_columna_1 = int(componentes[1])
            letra_columna_0 = componentes[0]
            asociaciones[valor_columna_1].add(letra_columna_0)
    lista_tuplas_ordenadas = sorted(asociaciones.items())

    return [(valor, sorted(list(letras))) for valor, letras in lista_tuplas_ordenadas]


def pregunta_09():
    conteo_registros = defaultdict(int)

    with open('data.csv', 'r') as f:
        for linea in f:
            componentes = linea.split()
            diccionario_columna_5 = componentes[4]
            pares_clave_valor = diccionario_columna_5.split(',')
            for par in pares_clave_valor:
                clave = par.split(':')[0]
                conteo_registros[clave] += 1
    conteo_registros_ordenado = dict(sorted(conteo_registros.items()))

    return conteo_registros_ordenado


def pregunta_10():
    resultados = []

    with open('data.csv', 'r') as f:
        for linea in f:
            componentes = linea.split()
            letra_columna_1 = componentes[0]
            cantidad_columna_4 = len(componentes[3].split(','))
            cantidad_columna_5 = len(componentes[4].split(','))
            tupla_resultado = (letra_columna_1, cantidad_columna_4, cantidad_columna_5)
            resultados.append(tupla_resultado)

    return resultados


def pregunta_11():
    suma_letras = defaultdict(int)

    with open('data.csv', 'r') as f:
        for linea in f:
            componentes = linea.split()
            letras_columna_4 = componentes[3].split(',')
            suma_columna_2 = int(componentes[1])

            for letra in letras_columna_4:
                suma_letras[letra] += suma_columna_2
    suma_letras_ordenadas = dict(sorted(suma_letras.items()))

    return suma_letras_ordenadas


def pregunta_12():
    suma_letras = defaultdict(int)

    with open('data.csv', 'r') as f:
        for linea in f:
            componentes = linea.split()
            letra_columna_1 = componentes[0]
            valores_columna_5 = componentes[4].split(',')
            for valor in valores_columna_5:
                suma_letras[letra_columna_1] += int(valor.split(':')[1])
    suma_letras_ordenado = dict(sorted(suma_letras.items()))

    return suma_letras_ordenado
