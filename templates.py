class Template:
    def __init__(self, matrix):
        self.content = Template.transformar_matrix_to_json(matrix)
    
    @staticmethod
    def transformar_matrix_to_json(matrix):
        pass
