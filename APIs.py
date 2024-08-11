import requests

def cargar_API():
    informacion=requests.get("https://www.swapi.tech/api/")
    return informacion.json()

