import datetime
import calendar

class Calendar:
    def __init__(self):
        pass

    @staticmethod
    def get_current_calendar():
        date = datetime.date.today()
        return calendar.monthcalendar(date.year, date.month)
    
    @staticmethod
    def get_current_calendar_dict():
        """Permite obtener las fechas ordenadas por el nombre del días de semana. De esta manera puedes saber que días caen lunes, martes, miercoles, etc."""

        cal = Calendar.get_current_calendar()
        result = dict()
        for index, day in enumerate(("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")):
            result[day] = [day[index] for day in cal if day[index] != 0]

        return result

    @staticmethod
    def is_weekend_in_current_calendar(day:int):
        calendar_dict = Calendar.get_current_calendar_dict()
        return day in calendar_dict["sabado"] or day in calendar_dict["domingo"]

    @staticmethod
    def is_hollyday(day:int):
        """Requieres implementación :("""
        pass

    @staticmethod
    def get_days_list_of_month():
        """Retorna una lista con los días de acuerdo al mes"""
        return [day for row in Calendar.get_current_calendar() for day in row if day != 0]

if __name__ == "__main__":
    print(Calendar.get_current_calendar())