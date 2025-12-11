#pip install requests
import requests

def obtener_fecha_api():
    url = "https://timeapi.io/api/Time/current/zone?timeZone=America/Santiago"
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        return data["date"]   # yyyy-mm-dd
    else:
        return None


if __name__ == "__main__":
    fecha = obtener_fecha_api()
    print("Fecha actual:", fecha)
    