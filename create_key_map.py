import keyboard
import csv

key_list_map = []
print("Pressione todas as teclas que deseja registrar.")
print("As teclas possuem códigos independentes, porém podem ter o mesmo nome, como as teclas de teclado numérico.")
print("Para distinguir no mapeamento, será adicionado um marcador 'Auxiliar' no nome da tecla no mapeamento.")
print("Pressione CTRL + C ou feche a janela para salvar os registros e parar o script.")


def on_key_press(event):
    if event.scan_code not in [register["scan_code"] for register in key_list_map]:
        if event.name not in [register["name"] for register in key_list_map]:
            key_list_map.append({"scan_code": event.scan_code, "name": str(event.name).upper()})
        else:
            key_list_map.append({"scan_code": event.scan_code, "name": str(event.name).upper() + " Auxiliar"})

    with open("key_map.csv", "w", newline="") as csv_file:
        headers = ["scan_code", "name"]
        writer = csv.DictWriter(csv_file, fieldnames=headers )

        writer.writeheader()
        for row in key_list_map:
            writer.writerow(row)

    print("                                                                     ", end="\r")
    print("Tecla pressionada:", str(event.name).upper(), "scan_code:", event.scan_code, end="\r")

keyboard.on_press(on_key_press)


# Mantenha o script em execução
keyboard.wait()