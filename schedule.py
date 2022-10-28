import datetime
from pyclbr import Function
from worker import *
from util import get_current_calendar_dict, get_current_calendar, get_feriados, listas_diferentes2
import random



class Schedule:
    dias_del_mes = [day for row in get_current_calendar()
                    for day in row if day != 0]
    mes = datetime.datetime.now().strftime("%B")
    calendar_dict = get_current_calendar_dict()  
    feriados = get_feriados()
    
    def __init__(self, trabajadores:list[Worker], funcion_comparacion: Function,reglas_dias_trabajados:dict["mañana": dict[int: dict[str:int, str: str or tuple]], "tarde": dict[int: dict[str:int, str:str or tuple]]] = {"mañana": {dia: {"cantidad":1, "tipo":"cualquiera"} for dia in dias_del_mes}, "tarde": {dia: {"cantidad":2, "tipo":("senior", "junior")} for dia in dias_del_mes}}):
        self.trabajadores = trabajadores
        self.funcion_comparacion = funcion_comparacion
        self.reglas_dias_trabajados = reglas_dias_trabajados
        self.horario = None

    @staticmethod
    def dia_no_trabajable(day) -> bool:
        return day in Schedule.calendar_dict["sabado"] or day in Schedule.calendar_dict["domingo"]

    @staticmethod
    def es_feriado(day) -> bool:
        return day in Schedule.feriados
    
    def obtener_horario(self) -> dict:
        if self.horario == None:
            self.generar_horario()
        return  self.horario

    def generar_horario(self) -> dict["mañana": list[list[str]], "tarde": list[list[str]]]:
        result = {"mañana": {}, "tarde": {}}
        trabajadores_ordenados_por_tipo = ordenar_trabajadores(self.trabajadores)

        def escoger_trabajadores(turno:str):
            tipo = self.reglas_dias_trabajados[turno][dia]["tipo"]
            cantidad = self.reglas_dias_trabajados[turno][dia]["cantidad"]

            if  tipo == 'cualquiera':
                result = random.sample(self.trabajadores, cantidad)
            else:
                result = [random.choice(trabajadores_ordenados_por_tipo[t]) for t in tipo]
            return result

        turno_anterior = None
        is_primero = True
        for index, dia in enumerate(Schedule.dias_del_mes):
            for turno in result.keys():
                
                if Schedule.dia_no_trabajable(dia) or Schedule.es_feriado(dia):
                    result[turno][dia] = [None]
                    continue

                if is_primero:
                    trabajadores_seleccionados = escoger_trabajadores(turno)
                    is_primero = False
                else:
                    while True:
                        trabajadores_seleccionados = escoger_trabajadores(turno)
                        #print(*trabajadores_seleccionados," == " ,*result[turno][dia - 1])
                        
                        if result[turno][dia - 1] == None:
                            break
                        
                        # print("comparando", *turno_anterior, *trabajadores_seleccionados)
                        #if self.funcion_comparacion(trabajadores_seleccionados, result[turno][dia - 1]) and self.funcion_comparacion(turno_anterior, trabajadores_seleccionados):
                        #    break
                        if self.funcion_comparacion(turno_anterior, trabajadores_seleccionados):
                            break

                
                turno_anterior = trabajadores_seleccionados
                result[turno][dia] = trabajadores_seleccionados

                for trabajador in trabajadores_seleccionados:
                    trabajador.agregar_dia_trabajado()

                    if trabajador.horario_esta_completado():
                        self.trabajadores.remove(trabajador)
                        trabajadores_ordenados_por_tipo = ordenar_trabajadores(self.trabajadores)
                        #print("Entramos")
                        #print(*self.trabajadores, sep='\t')
                
        self.horario = result
        return result    
    
    def convertir_horario_matrix(self):
        lista = [["Mañana", "Tarde"]] 
        
        for dia in Schedule.dias_del_mes:
            row = []
            for turno in self.horario:
                for value in self.horario[turno][dia]:
                    row.append(value)
            lista.append(row)
        return lista

class CompactSchedule:
    def __init__(self):
        pass

    def generar_schedule(content: list[list[str]]):
        pass

    def generar_contenido_horario(lista_funciones_generadoras_horarios:list, nombre_empresa:str):
        pass

if __name__ == "__main__":
    trabajadores = cargar_trabajadores("data.csv")
    
    corpo = extraer_lista_trabajadores_tipo(trabajadores, "corporativa")

    horario_corpo = Schedule(corpo, listas_diferentes2)
    result = horario_corpo.generar_horario()
 
    # for dia, trabajadores in mañana.items():
    #     print(dia)
    #     for trabajador in trabajadores:
    #         print(trabajador)
    # print()
    # for dia, trabajadores in tarde.items():
    #     print(dia)
    #     for trabajador in trabajadores:
    #         print(trabajador)
    matriz = horario_corpo.convertir_horario_matrix()
 

    for row in matriz:
        for worker in row:
            dias = worker
            try:
                print(f"{dias.nombre} {dias.dias_trabajados}", end= ';')
            except:
                print(dias, end=";")

        
        print()