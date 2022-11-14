import os
import random
from util import *

class Worker:
    tipo_trabajadores = ('junior', 'senior')
    empresas= ('corporativa', 'pyme', 'empresa', 'negocios')
    dias_trabajar = {'junior': 28}

    def __init__(self, nombre:str, tipo:str, empresa:str,  vacaciones:list[int] = []):
        if not tipo in Worker.tipo_trabajadores:
            message = f'el tipo de trabajador: \'{tipo}\' no está definido, solo puede utilizar los siguientes tipos de trabajador {Worker.tipo_trabajadores}'
            raise Exception(message)
        
        if  not empresa in Worker.empresas:
            message = f'la clase de empresa: \'{empresa}\' no está definida, solo puede utilizar los siguientes nombres de empresas {Worker.empresas}'
            raise Exception(message)
        
        self.tipo = tipo
        self.vacaciones = vacaciones
        self.nombre = nombre
        self.empresa =empresa
        self.dias_trabajados = 0
        self.dias_trabajar = None
    
    def __str__(self):
        #return f"Nombre: {self.nombre}, Empresa: {self.empresa} Tipo: {self.tipo}"
        return f"{self.nombre}"
    
    def agregar_dia_trabajado(self, cantidad : int = 1):
        self.dias_trabajados += 1
    
    def horario_esta_completado(self) -> bool:
        return self.dias_trabajados == self.dias_trabajar
    

def cargar_trabajadores(path:str, file_type:str = None) -> list[Worker]:
    file_name, extension = os.path.splitext(path) 
    if extension == '.csv' or file_type == '.csv':
        with open(path, mode = 'r') as file:
            next(file, None)
            lista_atributos = [[valor.strip('\n') for valor in row.split(';')] for row in file]
            return [Worker(nombre=nombre, tipo=tipo_trabajador, empresa=tipo_empresa) for nombre, tipo_empresa, tipo_trabajador in lista_atributos]

def ordenar_trabajadores(lista_trabajadores: list[Worker]) -> dict[str: list[Worker]]:
    result = {tipo_trabajador : [trabajador for trabajador in lista_trabajadores if trabajador.tipo == tipo_trabajador] for tipo_trabajador in Worker.tipo_trabajadores}
    return result

def extraer_lista_trabajadores_por_empresa(lista_trabajadores: list[Worker], empresa:str) -> list[Worker]:
    if not empresa in Worker.empresas:
        message = f"El tipo de empresa {empresa} no esta definido"
        raise Exception(message)
    result =  [worker for worker in lista_trabajadores if worker.empresa == empresa]
    return result

def obtener_cantidad_trabajadores_tipo(trabajadores):
    result = dict()
    for key in trabajadores:
        result[key] = len(trabajadores[key])
    return result
    
def obtener_cantidad_turnos_trabajador_tipo(trabajadores, cantidad_turnos):
    cantidad_trabajadores_tipo = obtener_cantidad_trabajadores_tipo(trabajadores)
    result = dict()
    for key, value in cantidad_trabajadores_tipo.items():
        result[key] = cantidad_turnos/cantidad_trabajadores_tipo
    return result


def generar_dias_trabajados(lista_trabajadores:list[Worker], template:dict):
    turnos = contar_cantidad_turnos_tipo(template)
    lista_ordenada = ordenar_trabajadores(lista_trabajadores)
    cantidad_trabajadores_por_tipo = obtener_cantidad_trabajadores_tipo(lista_ordenada)

    dias_trabajados = dict()
    total_turnos_asignados = 0
    for key in Worker.tipo_trabajadores:

        total_turnos_asignados += turnos[key]//cantidad_trabajadores_por_tipo[key]
        dias_trabajados[key] = turnos[key]//cantidad_trabajadores_por_tipo[key]

    cantidad_turnos_necesitados = sum(turnos[k] for k in turnos)
    if cantidad_turnos_necesitados > total_turnos_asignados:
        diferencia = cantidad_turnos_necesitados - total_turnos_asignados
        dias_trabajados['junior'] += diferencia
    
    random.shuffle(lista_trabajadores)

    for worker in lista_trabajadores:
        dias = dias_trabajados[worker.tipo]
        worker.dias_trabajar = dias
    
def escoger_trabajadores(lista_turnos_trabajadores:list[Worker], tipo_trabajadores:tuple[str]):
    """Recibe una lista con todos los turnos disponibles y esoce tres trabajadores de acuerdo a los tipos requeridos"""
    trabajadores_escogidos = []
    inicio = random.randint(0, len(lista_turnos_trabajadores) - 1)
    index = inicio
    escoger_cualquiera = False
    for tipo in tipo_trabajadores:
        while(True):
            try:
                w = lista_turnos_trabajadores[index]
            except:
                print(len(lista_turnos_trabajadores))
                print(f"Indice: {index}")
                input()
            # print(tipo, '==', w.tipo)
            # print(w in trabajadores_escogidos)
            # print(w.nombre)
            # print(trabajadores_escogidos)
            # input()
            # print(len(trabajadores_escogidos), '<', len(tipo_trabajadores))
            if (tipo == w.tipo) or (tipo == w.tipo and escoger_cualquiera):
                trabajadores_escogidos.append(w.nombre) 
                lista_turnos_trabajadores.pop(index)
                if index == len(lista_turnos_trabajadores):
                    index = 0
                break
            index = index + 1 
            if index == len(lista_turnos_trabajadores):
                index = 0
            
            if index == inicio:
                if escoger_cualquiera:
                    return trabajadores_escogidos
                escoger_cualquiera = True
    return trabajadores_escogidos

def generar_total_turnos(lista_trabajadores:list[Worker]):
    if lista_trabajadores[0].dias_trabajar == None:
        raise Exception("Primero debes establecer la cantidad de turnos a trabajar para cada chupapinga")
    
    result = []
    for w in lista_trabajadores:
        result.extend([w]*w.dias_trabajar)
    random.shuffle(result)
    return result

if __name__ == "__main__":
    lista = cargar_trabajadores('data.csv')
    print(*lista, sep='\n')
    lista_seleccionada = extraer_lista_trabajadores_por_empresa(lista, 'corporativa')
    lista_seleccionada = ordenar_trabajadores(lista_seleccionada)
    print(obtener_cantidad_trabajadores_tipo(lista_seleccionada))
