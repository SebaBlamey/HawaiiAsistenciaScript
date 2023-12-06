import requests
import argparse

def registrar_asistencia(codigo, rut, nota):
    url = f"https://losvilos.ucn.cl/hawaii/asist.php?c={codigo}&op=m"
    data = {
        'r': rut,
        'n': nota,
    }

    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print("Asistencia registrada")
    else:
        print(f"Error al registrar la asistencia [{response.status_code}]")

def buscar_estudiante(codigo, rut):
    url = f"https://losvilos.ucn.cl/hawaii/asist.php?c={codigo}&op=b"
    data = {'r': rut}

    response = requests.post(url, data=data)

    if response.status_code == 200:
        data = response.json()
        if data['nombre']:
            print(f"Estudiante encontrado: {data['nombre']}")
            return True
        else:
            print("Estudiante no encontrado.")
            return False
    else:
        print(f"Error al buscar el estudiante. [{response.status_code}]")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script para flojos para registrar la asistencia.")
    parser.add_argument("-c", required=True, help="Codigo unico")
    parser.add_argument("-r", required=True, help="Rut del estudiante.")
    parser.add_argument("-nota", help="Nota de la clase (entre 1.0 y 7.0).", default=7.0)

    args = parser.parse_args()

    if buscar_estudiante(args.c,args.r):
        if 1.0 <= float(args.nota) <= 7.0:
            registrar_asistencia(args.c, args.r, args.nota)
        else:
            print("La nota debe estar en el rango de 1.0 a 7.0.")

