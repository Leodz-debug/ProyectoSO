import time
import csv

def leer_memoria():
    with open("/proc/meminfo", "r") as f:
        data = f.readlines()

    mem = {}
    for line in data:
        parts = line.split(":")
        key = parts[0]
        value = parts[1].strip().split()[0]
        mem[key] = int(value)

    return mem

def guardar_csv(filename, datos):
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(datos)

archivo = "../datos/memoria.csv"

with open(archivo, "w") as f:
    f.write("tiempo,mem_total,mem_libre,mem_disponible,mem_usada_pct,swap_total,swap_libre,swap_usada_pct\n")

print("Iniciando monitoreo de memoria... Ctrl+C para detener")

inicio = time.time()

try:
    while True:
        mem = leer_memoria()

        mem_total = mem.get("MemTotal", 0)
        mem_free = mem.get("MemFree", 0)
        mem_avail = mem.get("MemAvailable", 0)

        swap_total = mem.get("SwapTotal", 0)
        swap_free = mem.get("SwapFree", 0)

        mem_used_pct = round(((mem_total - mem_avail) / mem_total) * 100, 2) if mem_total else 0
        swap_used_pct = round(((swap_total - swap_free) / swap_total) * 100, 2) if swap_total else 0

        datos = [
            int(time.time() - inicio),
            mem_total,
            mem_free,
            mem_avail,
            mem_used_pct,
            swap_total,
            swap_free,
            swap_used_pct
        ]

        print(datos)
        guardar_csv(archivo, datos)

        time.sleep(1)

except KeyboardInterrupt:
    print("Monitoreo detenido.")
