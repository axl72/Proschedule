import datetime
import calendar
import random


def get_current_calendar():
    date = datetime.date.today()

    return calendar.monthcalendar(date.year, date.month)


def get_current_calendar_dict():
    """Get a custom calendar content in Dict object"""

    cal = get_current_calendar()

    result = dict()
    for index, day in enumerate(("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")):
        result[day] = [day[index] for day in cal if day[index] != 0]

    return result


def is_hollyday(day):
    # requiere implementation
    return False


def get_count_work_days(calendar_dictionary):
    """Returns the number days that you should work"""

    lista = [list_days for key in calendar_dictionary.keys()
             for list_days in calendar_dictionary[key] if key != "sabado" and key != "domingo"]

    result = list(filter(lambda x: not is_hollyday(x), lista))
    return len(result)


def calculate_days_to_works(num_days):
    junior = 28
    num_days *= 3
    if (num_days - 28) % 3 == 0:
        senior = (num_days - 28)//3
    elif (num_days - 28) % 3 == 2:
        junior = 27
        senior = (num_days - junior)//3
    else:
        senior = (num_days - 28)//3

    return {"senior": senior, "junior": junior}


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

def get_feriados() -> list:
    return []

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


if __name__ == "__main__":
    hola = {"juana": 1, "sergio": 2}

    [print(key, value) for key, value in hola.items()]
    print(hola.values)
    map(lambda x: print(x) if x == "juana" else None, hola.items())
