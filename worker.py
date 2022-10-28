import os

class Worker:
    tipo_trabajadores = ('junior', 'senior')
    empresas= ('corporativa', 'pyme', 'empresa', 'negocios')
    dias_trabajar = {'junior': 28}

    def __init__(self, nombre:str, tipo:str, empresa:str, dias_trabajar:int,  vacaciones:list = []):
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
        self.dias_trabajar = dias_trabajar
    
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
            return [Worker(nombre=nombre, tipo=tipo_trabajador, empresa=tipo_empresa, dias_trabajar=int(dias)) for nombre, tipo_empresa, tipo_trabajador, dias in lista_atributos]

def ordenar_trabajadores(lista_trabajadores: list[Worker]) -> dict[str: list[Worker]]:
    result = {tipo_trabajador : [trabajador for trabajador in lista_trabajadores if trabajador.tipo == tipo_trabajador] for tipo_trabajador in Worker.tipo_trabajadores}
    return result

def extraer_lista_trabajadores_tipo(lista_trabajadores: list[Worker], empresa:str) -> list[Worker]:
    if not empresa in Worker.empresas:
        message = f"El tipo de empresa {empresa} no esta definido"
        raise Exception(message)
    result =  [worker for worker in lista_trabajadores if worker.empresa == empresa]
    return result


if __name__ == "__main__":
    lista = cargar_trabajadores('data.csv')
    print(*lista, sep='\n')

