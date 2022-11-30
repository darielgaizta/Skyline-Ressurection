import os
import tkinter as tk
from tkinter import ttk

from transport.views import TransportView
from ticket.views import TicketView
from map.views import MapView

PATH_IMG = os.path.abspath('..') + '\\img'


class MainView:

    HEIGHT, WIDTH = 864, 1536

    BG_01 = '#DDC48E'  # Background primary
    BG_02 = '#F37F14'  # Background secondary
    BG_03 = '#CF5C36'  # Background ternary

    def back(frame):
        MainView.home(frame)

    def home(current_screen):
        current_screen.destroy()

        # Initialize frame
        home_screen = tk.Tk()
        home_screen.title('Skyline')
        home_screen.geometry('1920x1080')
        home_screen.configure(bg=MainView.BG_01)

        # Logo Skyline
        logo_container = tk.Canvas(
            home_screen, bg=MainView.BG_03, highlightthickness=0)
        logo_container.grid(row=0, column=0, ipadx=800, ipady=10, pady=(0, 10))
        logo = tk.Label(logo_container, text="SKYLINE", font=(
                        "Impact", 40), fg="white", bg="#CF5C36", justify="left")
        logo.grid(row=0, column=0)

        # Initialize window
        window = tk.Canvas(home_screen, height=MainView.HEIGHT,
                           width=MainView.WIDTH, highlightthickness=0, bg=MainView.BG_01)
        window.place(anchor='center', relx=0.5, rely=0.5)

        # Search input form
        search_entry = ttk.Entry(window, width=100)
        search_entry.grid(row=1, column=1, columnspan=2)
        search_img = tk.PhotoImage(file=PATH_IMG+'\\search.png')
        search_btn = tk.Button(window, image=search_img, bg=MainView.BG_03,
                               command=lambda: TicketView.search_ticket(home_screen, search_entry.get()))
        search_btn.grid(row=1, column=3, padx=(10, 0))

        # Buy ticket button (BELI TIKET)
        buy_ticket_img = tk.PhotoImage(file=PATH_IMG+'\\buy_btn.png')
        buy_ticket_btn = ttk.Button(
            window, image=buy_ticket_img, command=lambda: TicketView.buy_ticket(home_screen))
        buy_ticket_btn.grid(row=3, column=1)

        # Upgrade ticket button (UPGRADE TIKET KE FASTPASS)
        upgrade_img = tk.PhotoImage(file=PATH_IMG+'\\upgrade_btn.png')
        upgrade_btn = ttk.Button(
            window, image=upgrade_img, command=lambda: TicketView.upgrade_ticket(home_screen))
        upgrade_btn.grid(row=3, column=2)

        # Explore ticket button (MELIHAT PETA DAN RESTORAN YANG ADA DI THEME PARK)
        explore_img = tk.PhotoImage(file=PATH_IMG+'\\explore_btn.png')
        explore_btn = ttk.Button(
            window, image=explore_img, command=lambda: MapView.show_map(home_screen))
        explore_btn.grid(row=5, column=1)

        # Transport button
        transport_img = tk.PhotoImage(file=PATH_IMG+'\\transport_btn.png')
        transport_btn = ttk.Button(
            window, image=transport_img, command=lambda: TransportView.show_transports(home_screen))
        transport_btn.grid(row=5, column=2)

        home_screen.mainloop()


def main():
    root = tk.Tk()
    MainView.home(root)


if __name__ == '__main__':
    main()
