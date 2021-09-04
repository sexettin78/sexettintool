import time 
import threading
import os
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
os.system("pip install pynput")
print("\033[91m\n Programı kapatmak için ctrl c yapın veya terminali kapatın.Süreyi ona göre ayarlayın.Sorumluluk kabul edilmez. \n")
delay = int(input("Kaç saniyede bir tıklasın? "))
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class ClickMouse(threading.Thread):
	def __init__(self, delay, button):
		super().__init__()
		self.delay = delay
		self.button = button
		self.running = False
		self.program_running = True

	def start_clicking(self):
		self.running = True

	def stop_clicking(self):
		self.running = False

	def exit(self):
		self.stop_clicking()
		self.program_running = False

	def run(self):
		while self.program_running:
			mouse.click(self.button)
			time.sleep(self.delay)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
	if key == start_stop_key:
		if click_thread_running:
			click_thread.stop_clicking()
		else:
			click_thread.start_clicking()
	elif key == exit_key:
		click_thread.exit()
		listener.stop()












