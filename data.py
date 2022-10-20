import csv


def read_data(filename):
    """Retorna una lista de listas con todo el contenido del csv"""
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)

        return [row for row in csvreader]


def read_data_column(filename, column_name):
    """Returns a list wich content a csv column from a file by column name"""
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)[0].split(";")
        if not column_name in fields:
            raise Exception("Column name was not found")
        index = fields.index(column_name)

        return [(row[0].split(";")[index], row[0].split(";")[-1]) for row in csvreader if row[0].split(";")[index] != '']


if __name__ == "__main__":
    print(*read_data_column("data.txt", "corpo"), sep='\n')
