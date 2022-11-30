# FILE: views.py

import os
import tkinter as tk

from tkinter import *
from tkinter import ttk

from . import controller

PATH_IMG = os.path.abspath('..') + '\\img'

class RestaurantView:

	HEIGHT, WIDTH = 864, 1536

	BG_01 = '#DDC48E' # Background primary
	BG_02 = '#F37F14' # Background secondary
	BG_03 = '#CF5C36' # Background ternary

	def back_to_map(frame):
		from map.views import MapView
		MapView.show_map(frame)

	def back_to_restaurants(frame):
		RestaurantView.show_restaurant(frame)

	def start(frame, window):
		frame.title('Skyline')
		frame.geometry('1920x1080')
		frame.configure(bg=RestaurantView.BG_01)
		window.place(anchor='center', relx=0.5, rely=0.5)

	# Use case: MELIHAT RESTORAN YANG ADA DI THEME PARK
	def show_restaurant(current_screen):
		# Close current screen
		current_screen.destroy()

		# Initialize view
		frame  = tk.Tk()
		window = tk.Canvas(
			frame,
			height=RestaurantView.HEIGHT,
			width=RestaurantView.WIDTH,
			bg=RestaurantView.BG_01,
			highlightthickness=0
		)
		RestaurantView.start(frame, window)

		# Back button
		back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
		back_btn = tk.Button(window, image=back_img, command=lambda: RestaurantView.back_to_map(frame), bg=RestaurantView.BG_01)
		back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

		# Resto title
		resto_title = tk.Label(window, text='Restoran', font=('Inter Bold', 30), bg=RestaurantView.BG_01)
		resto_title.grid(row=0, column=1)

		restaurants = controller.RestaurantController.get_all_restaurants()

		# List all the restaurants
		for i in range(len(restaurants)):
			container = tk.Canvas(window, bg=RestaurantView.BG_02, highlightthickness=0)
			container.grid(
				row=i+1,
				column=1,
				pady=(0, 40)
			)

			restaurant_name = tk.Label(container, text=restaurants[i][1], justify='left', font=('Inter', 20), bg=RestaurantView.BG_02)
			restaurant_name.grid(
				row=1,
				column=1,
				ipady=22,
				ipadx=500
			)

			btn = tk.Button(container, text='LIHAT MENU', bg=RestaurantView.BG_03, fg='white', font=('Inter', 20), command=lambda j=i: RestaurantView.show_menu_restaurant(frame, restaurants[j][0]))
			btn.grid(row=2, column=1)

		frame.mainloop()

	# Use case: MELIHAT MENU YANG ADA DI RESTORAN
	def show_menu_restaurant(current_screen, restaurant_id):
		# Close current screen
		current_screen.destroy()

		# Initialize view
		frame  = tk.Tk()
		window = tk.Canvas(
			frame,
			height=RestaurantView.HEIGHT,
			width=RestaurantView.WIDTH,
			bg=RestaurantView.BG_01,
			highlightthickness=0
		)
		RestaurantView.start(frame, window)

		# Back button
		back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
		back_btn = tk.Button(window, image=back_img, command=lambda: RestaurantView.back_to_restaurants(frame), bg=RestaurantView.BG_01)
		back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

		# Menu title
		menu_title = tk.Label(window, text='Menu', font=(
			'Inter Bold', 30), bg=RestaurantView.BG_01)
		menu_title.grid(row=0, column=1)

		menus = controller.RestaurantController.get_menu_restaurant(restaurant_id)

		container = tk.Canvas(window, bg=RestaurantView.BG_02, highlightthickness=0)
		container.grid(
            row=1,
        	column=1,
            ipady=300,
        	ipadx=400
            )

		for i in range(len(menus)):
			menu = tk.Label(container, text=menus[i][1], justify='center', font=(
				'Inter', 20), bg=RestaurantView.BG_02)
			menu.grid(row=i+1, column=2)
			gap = tk.Label(container, text=' : ', bg=RestaurantView.BG_02)
			gap.grid(row=i+1, column=3)
			menu_description = tk.Label(container, text=menus[i][3], justify='center', font=(
				'Inter', 20), bg=RestaurantView.BG_02)
			menu_description.grid(row=i+1, column=5)

		frame.mainloop()