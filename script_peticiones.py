import requests
import threading

# URL de Envoy que en el token para las peticiones
ENVOY_URL = "http://127.0.0.1:10000/api/auth/token/"

# URl e la API categorias para relizar las peticones
API_URL = "http://127.0.0.1:10000/api/categorias/"

# Credenciales del usuario
USER_CREDENTIALS = {
    "username": "tenis",
    "password": "t3n817_3#23"
}

# Número de peticiones y número de hilos a usar
TOTAL_REQUESTS = 150000
NUM_HILOS = 8  # Ajusta el número de hilos según la capacidad del sistema


def obtener_token():
    """Solicita el token JWT y lo retorna"""
    response = requests.post(ENVOY_URL, json=USER_CREDENTIALS)

    if response.status_code == 200:
        token = response.json().get("access")
        print(f" Token obtenido correctamente: {token[:10]}...")  
        return token
    else:
        print(f" Error al obtener el token: {response.text}")
        return None


def realizar_peticion(token, num_peticion):
    """Realiza una petición a la API con el token"""
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        print(f" [{num_peticion}] Status: 200, petición enviada")
    else:
        print(f" [{num_peticion}] Status: {response.status_code}, Response: {response.text}")


def ejecutar_peticion_hilos(token):
    """Ejecuta las peticiones en paralelo usando hilos"""
    hilos = []

    for i in range(1, TOTAL_REQUESTS + 1):
        hilo = threading.Thread(target=realizar_peticion, args=(token, i))
        hilos.append(hilo)
        hilo.start()

        # Limitar el número de hilos simultáneos para evitar saturar el sistema
        if len(hilos) >= NUM_HILOS:
            for hilo in hilos:
                hilo.join()  # Esperar a que terminen los hilos antes de crear más
            hilos = []  # Reiniciar la lista de hilos


if __name__ == "__main__":
    token = obtener_token()

    if token:
        ejecutar_peticion_hilos(token)
    else:
        print(" No se pudo obtener el token. Verifica las credenciales o el servidor.")
