import csv
with open('starships.csv', 'r') as naves_csv:
    lector_csv = csv.DictReader(naves_csv)
    
def extraer_nombres_naves(naves_csv):
    nombres_naves = []
    for fila in lector_csv:
        nombres_naves.append(fila['name'])
    return nombres_naves

with open('starships.csv', 'r') as naves_csv:
    lector_csv = csv.DictReader(naves_csv)
    nombres_naves = extraer_nombres_naves(naves_csv)
    print(nombres_naves)