import datetime
import sys
from worker import *
import random
from procal import Calendar



class Schedule:
    dias_del_mes = Calendar.get_days_list_of_month()
    mes = datetime.datetime.now().strftime("%B")
    calendar_dict = Calendar.get_current_calendar_dict()  
    
    def __init__(self, trabajadores:list[Worker],template:dict["mañana": dict[int: dict[str:int, str: str or tuple]], "tarde": dict[int: dict[str:int, str:str or tuple]]] ):
        self.trabajadores = trabajadores
        self.horario = None
        self.template = template

    def obtener_horario(self) -> dict:
        if self.horario == None:
            self.generar_horario()
        return  self.horario

    def generar_horario(self):
        generar_dias_trabajados(self.trabajadores, self.template)
        total_turnos = generar_total_turnos(self.trabajadores)
        result = dict()
        for day in self.template:
            if Calendar.is_weekend_in_current_calendar(day):
                result[day] = None
                continue
            tipo_trabajadores = []
            for turno in self.template[day]:
                tipo_trabajadores.extend([tipo for tipo in self.template[day][turno] ])
            trabajadores_seleccionados = escoger_trabajadores(total_turnos, tipo_trabajadores)
            # print("Dia: ", day, "  --  ", trabajadores_seleccionados)
            result[day] = trabajadores_seleccionados
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
    
    corpo = extraer_lista_trabajadores_por_empresa(trabajadores, "corporativa")
    template = {dia: {"mañana":("junior",), "tarde": ("senior", "junior")} for dia in Calendar.get_days_list_of_month()}
    horario_corpo = Schedule(corpo, template)
    result = horario_corpo.generar_horario()
    
    for row, values in result.items():
        print(row, values)
