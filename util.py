from procal import Calendar
import random






def get_count_work_days(calendar_dictionary):
    """Returns the number days that you should work"""

    lista = [list_days for key in calendar_dictionary.keys()
             for list_days in calendar_dictionary[key] if key != "sabado" and key != "domingo"]

    result = list(filter(lambda x: not is_hollyday(x), lista))
    return len(result)





def generate_workers_of_the_day(workers_dict, days_to_work):
    workers = list(workers_dict.keys())
    aux = []
    for worker in workers:
        type_work = workers_dict[worker][-1]
        num_days = days_to_work[type_work]
        aux.extend([worker]*num_days)
        random.shuffle(aux)
    workers = aux
    return workers
    worker_of_the_day = workers.pop(random.randint(0, len(workers) - 1))
    workers_dict[worker_of_the_day][0] += 1
    return worker_of_the_day


def listas_diferentes(lista1:list, lista2:list) -> bool:
    for valor1 in lista1:
        if valor1 in lista2:
            return False
    return True

def listas_diferentes2(lista1: list, lista2: list) -> bool:
    for valor1 in lista1:
        if valor1 != lista2[0]:
            return True
    return False



def contar_cantidad_turnos_tipo(diccionario:dict):
    result = dict()
    for day, value in diccionario.items():
        for turno in value:
            tipo = value[turno]

            for t in tipo:
                if t in result:
                    result[t] += 1
                else:
                    result[t] = 0
    return result

if __name__ == "__main__":
    hola = {"juana": 1, "sergio": 2}

    # [print(key, value) for key, value in hola.items()]
    # print(hola.values)
    # map(lambda x: print(x) if x == "juana" else None, hola.items())
    dias_del_mes = Calendar.get_days_list_of_month()
    diccionario = {"mañana": {dia: {"cantidad":1, "tipo":"junior"} for dia in dias_del_mes if not Calendar.is_weekend_in_current_calendar(dia)}, "tarde": {dia: {"cantidad":2, "tipo":("senior", "junior")} for dia in dias_del_mes if not Calendar.is_weekend_in_current_calendar(dia)}}
    print(contar_cantidad_turnos_tipo(diccionario))