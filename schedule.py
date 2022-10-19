import datetime
import data
from util import *


def generate_schedule():
    month_days = [day for row in get_current_calendar()
                  for day in row if day != 0]
    month = datetime.datetime.now().strftime("%B")
    calendar = get_current_calendar_dict()

    days_to_work = get_count_work_days(calendar)
    days_to_work = calculate_days_to_works(days_to_work)

    print(days_to_work)

    workers = data.read_data_column("data.txt", "corpo")

    def column(x): return [worker[x] for worker in workers]

    workers_name = column(0)

    workers_dict = {k: [v, x] for (k, v, x) in zip(
        workers_name, [0]*len(workers), column(-1))}

    print(workers_dict)
    result = list()
    for day in month_days:
        worker = get_worker_of_the_day(workers_dict, days_to_work)
        worker2 = get_worker_of_the_day(workers_dict, days_to_work)
        worker3 = get_worker_of_the_day(workers_dict, days_to_work)
        if day in calendar["sabado"] or day in calendar["domingo"]:
            result.append([f"{day}-{month[:3]}", "", "", ""])
            continue
        result.append([f"{day}-{month[:3]}", worker, worker2, worker3])

    return result


if __name__ == "__main__":
    #print(*get_current_calendar_dict()["miercoles"], sep='\n')
    print(*generate_schedule(), sep='\n')
    ab: str = 'adverb'
    sum(i for i in range(10) if i % 2 == 0)
    list1 = ["yellow", "gray", "brown"]
    list2 = list1[:]  # create a copie using slicing
