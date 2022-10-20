class Excel:
    """Esta clase representa la instancia de un excel. Requiere el contenido del excel y la ruta donde será generado"""

    def __init__(self, path, content):
        self.path = path
        self.content = content

    def generate_excel(self):
        """Crear un excel con todo el contenido preestablecido"""
        pass
