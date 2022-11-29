# FILE: views.py

import os
import tkinter as tk

from tkinter import *
from tkinter import ttk

from . import controller

PATH_IMG = os.path.abspath('..') + '\\img'

class TransportView:

	HEIGHT, WIDTH = 864, 1536

	BG_01 = '#DDC48E' # Background primary
	BG_02 = '#F37F14' # Background secondary
	BG_03 = '#CF5C36' # Background ternary

	def back(frame):
		from main import MainView
		MainView.back(frame)

	def start(frame, window):
		frame.title('Skyline')
		frame.geometry('1920x1080')
		frame.configure(bg=TransportView.BG_01)
		window.place(anchor='center', relx=0.5, rely=0.5)

	# Use case MELIHAT JADWAL TRANSPORTASI UMUM
	def show_transports(current_screen):
		# Close current screen
		current_screen.destroy()

		# Initialize view
		frame  = tk.Tk()
		window = tk.Canvas(
			frame,
			height=TransportView.HEIGHT,
			width=TransportView.WIDTH,
			bg=TransportView.BG_01,
			highlightthickness=0
		)
		TransportView.start(frame, window)

		# Back button
		back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
		back_btn = tk.Button(window, image=back_img, command=lambda: TransportView.back(frame), bg=TransportView.BG_01)
		back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

		transports = controller.TransportController.get_all_transports()

		containers, transport_names, buttons = [], [], []

		for i in range(len(transports)):
			container = tk.Canvas(window, bg=TransportView.BG_02, highlightthickness=0)
			container.grid(
				row=i,
				column=1,
				pady=(0, 10)
			)
			containers.append(container)

			transport_name = tk.Label(container, text=transports[i][1], justify='left', font=('Inter', 15), bg=TransportView.BG_02)
			transport_name.grid(
				row=1,
				column=1,
				ipady=20,
				ipadx=50
			)
			transport_names.append(transport_name)

		frame.mainloop()
