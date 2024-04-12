import csv

import keyboard
import pygetwindow as gw
from datetime import datetime

import os

windows_list_map = []

with open("windows_list.csv", "r", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        windows_list_map.append(dict(row))
    print(windows_list_map)


def save_windows_list():
    with open("windows_list.csv", "w", newline="", encoding="utf-8") as csv_file:
        headers = ["code", "title"]
        writer = csv.DictWriter(csv_file, fieldnames=headers)

        writer.writeheader()
        for row in windows_list_map:
            writer.writerow(row)


def save_log(log):
    if os.path.exists("log.csv"):
        with open("log.csv", "a", newline="", encoding="utf-8") as csv_file:
            for register in log:
                writer = csv.writer(csv_file)
                writer.writerow(register)

    else:
        with open("log.csv", "w", newline="", encoding="utf-8") as csv_file:
            headers = ["window_code", "key_code"]
            writer = csv.writer(csv_file)
            writer.writerow(headers)

            for register in log:
                writer.writerow(register)


# Variável global para armazenar o minuto inicial
initial_minute = None

# Função para verificar se passou um minuto desde o início do script
def passou_um_minuto():
    global initial_minute
    
    # Se o minuto inicial não foi definido, define-o agora
    if initial_minute is None:
        initial_minute = datetime.now().minute
        return False  # Não passou um minuto ainda
    
    # Verifica se o minuto atual é diferente do minuto inicial
    actual_minute = datetime.now().minute
    if actual_minute != initial_minute:
        initial_minute = actual_minute  # Atualiza o minuto inicial
        return True  # Passou um minuto
    else:
        return False  # Não passou um minuto ainda



log = []


def on_key_press(event):
    window_title = gw.getActiveWindowTitle()

    if window_title not in [window["title"] for window in windows_list_map]:
        windows_list_map.append(
            {
                "code": len(windows_list_map) + 1,
                "title": str(window_title),
            }
        )
        save_windows_list()

        window_code = len(windows_list_map)
    else:
        window_code = [
            window["code"]
            for window in windows_list_map
            if window["title"] == window_title
        ][0]

    print(
        "Tecla pressionada:",
        str(event.name).upper(),
        "scan_code:",
        event.scan_code,
        "window_code:",
        window_code,
    )
    log.append([event.scan_code, window_code])
    if passou_um_minuto():
        save_log(log)
        print("Passou um minuto, salvando o log e zerando a lista")
    else:
        print("Ainda não passou um minuto")


keyboard.on_press(on_key_press)

keyboard.wait()
