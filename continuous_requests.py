import os
import requests
import time

ecs_backend_url = os.environ.get("ECS_BACKEND_URL")
ecs_backend_port = os.environ.get("ECS_BACKEND_PORT")

while True:
    try:
        # Combinar la URL y el puerto para formar la dirección completa
        url = f"{ecs_backend_url}:{ecs_backend_port}"
        print("Realizando solicitud a:", url)  # Imprimir la URL antes de la solicitud
        response = requests.get(url)
        print("Solicitud exitosa. Código de estado:", response.status_code)
    except Exception as e:
        print("Error al realizar la solicitud:", str(e))

    time.sleep(5)  # o el intervalo que desees entre las solicitudes