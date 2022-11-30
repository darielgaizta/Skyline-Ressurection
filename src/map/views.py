# FILE: views.py

import os
import tkinter as tk

from tkinter import *
from tkinter import ttk

from restaurant.views import RestaurantView

PATH_IMG = os.path.abspath('..') + '\\img'


class MapView:

    HEIGHT, WIDTH = 864, 1536

    BG_01 = '#DDC48E'  # Background primary
    BG_02 = '#F37F14'  # Background secondary
    BG_03 = '#CF5C36'  # Background ternary

    def back(frame):
        from main import MainView
        MainView.back(frame)

    def start(frame, window):
        frame.title('Skyline')
        frame.geometry('1920x1080')
        frame.configure(bg=MapView.BG_01)
        window.place(anchor='center', relx=0.5, rely=0.5)

    # Use case: MENAMPILKAN PETA SKYLINE
    def show_map(current_screen):
        # Close current screen
        current_screen.destroy()

        # Initialize view
        frame = tk.Tk()
        window = tk.Canvas(
            frame,
            height=MapView.HEIGHT,
            width=MapView.WIDTH,
            bg=MapView.BG_01,
            highlightthickness=0
        )
        MapView.start(frame, window)

        # Logo Skyline
        logo_container = tk.Canvas(
            frame, bg=MapView.BG_03, highlightthickness=0)
        logo_container.grid(row=0, column=0, ipadx=800, ipady=10, pady=(0, 10))
        logo = tk.Label(logo_container, text="SKYLINE", font=(
            "Impact", 40), fg="white", bg="#CF5C36", justify="left")
        logo.grid(row=0, column=0)

        # Back button
        back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
        back_btn = tk.Button(
            window, image=back_img, command=lambda: MapView.back(frame), bg=MapView.BG_01)
        back_btn.grid(row=0, column=0, padx=(0, 10))

        # Map title
        map_title = tk.Label(window, text='PETA SKYLINE', font=(
            'Inter', 30, 'bold'), bg=MapView.BG_01)
        map_title.grid(row=0, column=1)

        # Map image
        map_img = tk.PhotoImage(file=PATH_IMG+'\\map.png')
        map_scr = tk.Label(window, image=map_img)
        map_scr.grid(row=1, column=1, pady=(20, 20))

        # Restaurant button
        restaurant_btn = tk.Button(window, text='Lihat Restoran', bg=MapView.BG_03, fg='white', font=(
            'Inter', 20), command=lambda: RestaurantView.show_restaurant(frame))
        restaurant_btn.grid(row=2, column=1)

        frame.mainloop()
