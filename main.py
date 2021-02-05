import decimal
import time
import threading
import random

from pynput import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import pyautogui
import pyperclip

delay = float(decimal.Decimal(random.randrange(1, 2)) / 100)
start_stop_key = KeyCode(char='`')
exit_key = KeyCode(char='c')
start = False


class Fossil(threading.Thread):
    def __init__(self):
        super(Fossil, self).__init__()
        self.running = False
        self.program_running = True
        self.resonators = 10
        self.fossils = 11
        self.movey = [0, 65, 130, 195, 260]
        self.inventory = 5

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                for y in range(self.inventory):

                    for x in range(1, self.resonators):
                        pyautogui.keyDown('shift')
                        pyautogui.click()

                        pyautogui.keyUp('shift')
                        pyautogui.hotkey('enter')

                        pyautogui.moveRel(65 * x, 0)
                        # time.sleep(.05)
                        pyautogui.click()

                        pyautogui.moveRel(0 - 65 * x, 0)

                    pyautogui.moveRel(-65, 0)
                    pyautogui.click()

                    for y in range(1, self.fossils):
                        pyautogui.moveRel(65, 0)
                        pyautogui.click()
                    pyautogui.moveRel(-585, 65)

                click_thread.stop_clicking()
                time.sleep(0.1)


click_thread = Fossil()
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
