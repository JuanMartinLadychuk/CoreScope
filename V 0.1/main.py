import psutil
import json
from datetime import datetime

def solicitar_numero(mensaje, tipo='int'):
    while True:
        try:
            valor = input(mensaje)
            if tipo == 'float':
                return float(valor)
            return int(valor)
        except ValueError:
            print(f'\n ERROR: "{valor}" no es un número válido.')

def aplicaciones_top_5():
    print("\n--- TOP 5 APLICACIONES (MÁS RAM) ---")
    procesos = []
    for proc in psutil.process_iter(['name', 'memory_percent']):
        try:
            info = proc.info 
            procesos.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    procesos_ordenados = sorted(procesos, key=lambda p: p['memory_percent'], reverse=True)
    for p in procesos_ordenados[:5]:
        print(f"Programa: {p['name']} | Uso RAM: {p['memory_percent']:.2f}%")

ejecutando = True

try:
    with open("alertas.json", "r") as archivo:
        alertas = json.load(archivo)
except:
    alertas = {}

while ejecutando:
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    opc = solicitar_numero("\n¿Qué desea hacer?: 1. CPU 2. RAM 3. Disco 4. Red 5. Ver Top 5 Procesos 0. Salir: ", tipo="int")
    
    match opc:
        case 1:
            uso_cpu = psutil.cpu_percent(interval=1)
            if uso_cpu > 80:
                print("ALERTA: El uso del CPU es demasiado alto")
                alertas = (f" ALERTA uso de CPU: %{uso_cpu} | Fecha: {ahora}")
                with open('alertas.json', 'w') as archivo: json.dump(alertas, archivo, indent=4)
            elif uso_cpu > 20:
                print("ALERTA: Ten precaución el uso del CPU es moderado")
                alertas = (f" ALERTA uso de CPU: %{uso_cpu} | Fecha: {ahora}")
                with open('alertas.json', 'w') as archivo: json.dump(alertas, archivo, indent=4)
            
            opc_cpu = input("\n 1. Ver porcentaje 2. Volver: ")
            if opc_cpu == "1": print(f'Uso CPU: {uso_cpu}%')

        case 2:
            memoria = psutil.virtual_memory()
            if memoria.percent > 80:
                print("ALERTA: RAM alta")
                alertas = (f" ALERTA RAM: %{memoria.percent} | Fecha: {ahora}")
                with open('alertas.json', 'w') as archivo: json.dump(alertas, archivo, indent=4)
            
            opc_ram = input("\n 1. Disponible 2. Total 3. Volver: ")
            if opc_ram == "1": print(f"Disponible: {memoria.available / (1024**3):.2f} GB")
            elif opc_ram == "2": print(f"Total: {memoria.total / (1024**3):.2f} GB")

        case 3:
            disco = psutil.disk_usage("/")
            if disco.percent > 80:
                print("ALERTA: Disco casi lleno")
                alertas = (f" ALERTA Disco: %{disco.percent} | Fecha: {ahora}")
                with open('alertas.json', 'w') as archivo: json.dump(alertas, archivo, indent=4)
            
            opc_disco = input("\n 1. Usado 2. Total 3. Volver: ")
            if opc_disco == "1": print(f"Usado: {disco.used / (1024**3):.2f} GB")
            elif opc_disco == "2": print(f"Total: {disco.total / (1024**3):.2f} GB")
        
        case 4:
            red = psutil.net_io_counters()
            enviado = red.bytes_sent / (1024**2)
            recibido = red.bytes_recv / (1024**2)
            
            print(f"\n--- TRÁFICO DE RED ---")
            print(f"Datos Enviados: {enviado:.2f} MB")
            print(f"Datos Recibidos: {recibido:.2f} MB")
            
            if enviado > 500:
                print("ALERTA: Estás subiendo muchos datos a la red.")            

        case 5:
            aplicaciones_top_5()

        case 0:
            print("Programa finalizado")
            ejecutando = False