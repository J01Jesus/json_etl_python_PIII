# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json

def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON con datos personales y una lista de prendas

    mipersona = {
        "nombre": "Jesus",
        "apellido": "Gonzalez",
        "DNI": "26701556",
        "elementos_vestir": [
            {"prenda": "chaleco", "cantidad": 4},
            {"prenda": "zapato", "cantidad": 12}
        ]
    }

    with open('mi_persona_json.json', 'w') as jsonfile:
        json.dump(mipersona, jsonfile, indent=4)

def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Leer el archivo, convertir a string e imprimir

    with open('mi_persona_json.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)

    print('Mostrar el contenido del archivo mi_persona_json')
    print(json.dumps(json_data, indent=4))

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    
    serializar()
    deserializar()

    print("terminamos")
