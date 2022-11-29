# FILE: views.py

import os
import tkinter as tk

from tkinter import *
from tkinter import ttk

from . import controller

PATH_IMG = os.path.abspath('..') + '\\img'


class TicketView:

    HEIGHT, WIDTH = 864, 1536

    BG_01 = '#DDC48E'  # Background primary
    BG_02 = '#F37F14'  # Background secondary
    BG_03 = '#CF5C36'  # Background ternary

    def back(frame):
        from main import MainView
        MainView.back(frame)

    def back_to_upgrade(frame):
        TicketView.upgrade_ticket(frame)

    def start(frame, window):
        frame.title('Skyline')
        frame.geometry('1920x1080')
        frame.configure(bg=TicketView.BG_01)
        window.place(anchor='center', relx=0.5, rely=0.5)

    # Use case: BELI TIKET
    def buy_ticket(current_screen):
        # Close current screen
        current_screen.destroy()

        # Initialize view
        frame = tk.Tk()
        window = tk.Canvas(
            frame,
            height=TicketView.HEIGHT,
            width=TicketView.WIDTH,
            bg=TicketView.BG_01,
            highlightthickness=0
        )

        TicketView.start(frame, window)

        # Logo Skyline
        logo_container = tk.Canvas(
            frame, bg=TicketView.BG_03, highlightthickness=0)
        logo_container.grid(row=0, column=0, ipadx=800, ipady=10, pady=(0, 10))
        logo = tk.Label(logo_container, text="SKYLINE", font=(
            "Impact", 40), fg="white", bg="#CF5C36", justify="left")
        logo.grid(row=0, column=0)

        # Back button
        back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
        back_btn = tk.Button(window, image=back_img, command=lambda: TicketView.back(
            frame), bg=TicketView.BG_01)
        back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

        # Ticket image
        ticket_img = tk.PhotoImage(file=PATH_IMG+'\\foto_tiket.png')

        # Regular ticket
        reg_ticket_container = tk.Canvas(
            window, bg=TicketView.BG_02, highlightthickness=0)
        reg_ticket_container.grid(
            row=0,
            column=1,
            pady=(0, 10)
        )
        reg_img = tk.Label(reg_ticket_container,
                           image=ticket_img, bg=TicketView.BG_02)
        reg_img.grid(
            row=1,
            column=1,
            ipady=20,
            ipadx=20
        )
        reg_title = tk.Label(reg_ticket_container, text="Regular - ONE DAY TICKET\nRp 150.000\nBisa refund\nBerlaku 7 hari setelah tanggal pembelian",
                             justify='left', font=('Inter', 15), bg=TicketView.BG_02)
        reg_title.grid(
            row=1,
            column=2,
            ipady=20,
            ipadx=70
        )

        # Fastpass ticket
        fst_ticket_container = tk.Canvas(
            window, bg=TicketView.BG_02, highlightthickness=0)
        fst_ticket_container.grid(
            row=2,
            column=1,
            pady=10
        )
        fst_img = tk.Label(fst_ticket_container,
                           image=ticket_img, bg=TicketView.BG_02)
        fst_img.grid(
            row=1,
            column=1,
            ipady=20,
            ipadx=20
        )
        fst_title = tk.Label(fst_ticket_container, text="Fastpass - ONE DAY TICKET\nRp 300.000\nBisa refund\nBerlaku 7 hari setelah tanggal pembelian",
                             justify='left', font=('Inter', 15), bg=TicketView.BG_02)
        fst_title.grid(
            row=1,
            column=2,
            ipady=20,
            ipadx=70
        )

        form_label = tk.Label(window, text='Data Pemesanan', font=(
            'Inter', 15, 'bold'), justify='left', bg=TicketView.BG_01)
        form_label.grid(
            row=4,
            column=1,
            padx=(0, 410),
            pady=20
        )

        # # Form input: email
        email_label = tk.Label(window, text='Email', justify='center', font=(
            'Inter', 10), bg=TicketView.BG_01)
        email_label.grid(
            row=5,
            column=1,
            padx=(0, 540)
        )
        email_entry = ttk.Entry(window, width=100)
        email_entry.grid(
            row=6,
            column=1
        )

        # # Form input: total_tickets
        total_label = tk.Label(window, text='Jumlah tiket', justify='left', font=(
            'Inter', 10), bg=TicketView.BG_01)
        total_label.grid(
            row=7,
            column=1,
            padx=(0, 500)
        )
        total_entry = ttk.Entry(window, width=100)
        total_entry.grid(
            row=8,
            column=1,
            padx=(0, 0)
        )

        # # Submit button
        def submit(): return controller.TicketController.buy_ticket(
            int(total_entry.get()), email_entry.get())
        submit_btn = tk.Button(window, text='Konfirmasi', font=(
            'Inter', 15, 'bold'), command=submit)
        submit_btn.grid(
            row=10,
            column=1,
            padx=(490, 0),
            pady=(15, 0)
        )

        frame.mainloop()

    # Use case: UPGRADE TICKET
    def upgrade_ticket(current_screen):
        # Close current screen
        current_screen.destroy()

        # Initialize view
        frame = tk.Tk()
        window = tk.Canvas(
            frame,
            height=TicketView.HEIGHT,
            width=TicketView.WIDTH,
            bg=TicketView.BG_01,
            highlightthickness=0
        )
        TicketView.start(frame, window)

        # Logo Skyline
        logo_container = tk.Canvas(
            frame, bg=TicketView.BG_03, highlightthickness=0)
        logo_container.grid(row=0, column=0, ipadx=800, ipady=10, pady=(0, 10))
        logo = tk.Label(logo_container, text="SKYLINE", font=(
            "Impact", 40), fg="white", bg="#CF5C36", justify="left")
        logo.grid(row=0, column=0)

        # Back button
        back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
        back_btn = tk.Button(window, image=back_img, command=lambda: TicketView.back(
            frame), bg=TicketView.BG_01)
        back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

        # Search form input
        search_entry = ttk.Entry(window, width=125)
        search_entry.grid(
            row=0,
            column=1,
            columnspan=2
        )

        # Submit button
        def submit():
            ticket = controller.TicketController.search_ticket(
                search_entry.get())
            if not ticket:
                # Show error ticket not found
                TicketView.ticket_not_found(frame)
            # Upgrade ticket is not active because payment is not handled by skyline
            # controller.TicketController.upgrade_ticket(search_entry.get(), ticket[6], 500000)

            # Unpack ticket attributes
            t_id, t_type, t_stat, t_is_paid, t_email, t_regular_code, t_fastpass_code, t_date_added, t_ticket_id = ticket

            # Ticket stat validation
            if t_stat == 'Active':
                # Ticket type validation
                if t_type == 'Regular':
                    TicketView.show_ticket_regular(
                        frame, t_ticket_id, t_fastpass_code)
                else:
                    # Show ticket is already fastpass
                    TicketView.show_ticket_fastpass(frame, t_ticket_id)
            else:
                TicketView.show_ticket_not_active(frame)

        search_img = tk.PhotoImage(file=PATH_IMG+'\\search.png')
        search_btn = tk.Button(window, image=search_img,
                               bg='#CF5C36', command=submit)
        search_btn.grid(row=0, column=3, padx=(10, 0))

        small_text = tk.Label(window, text='Silakan Masukan\nID Tiket Anda', font=(
            'Inter', 30), bg=TicketView.BG_03, fg='white', padx=220, pady=180)
        small_text.grid(row=1, column=1, columnspan=2, pady=(20, 0))

        frame.mainloop()

    # Use case: MENCARI DETAIL TIKET
    def search_ticket(current_screen, ticket_id):
        # Close current screen
        current_screen.destroy()

        # Initialize view
        frame = tk.Tk()
        window = tk.Canvas(
            frame,
            height=TicketView.HEIGHT,
            width=TicketView.WIDTH,
            bg=TicketView.BG_01,
            highlightthickness=0
        )
        TicketView.start(frame, window)

        # Back button
        back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
        back_btn = tk.Button(window, image=back_img, command=lambda: TicketView.back(
            frame), bg=TicketView.BG_01)
        back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

        ticket = controller.TicketController.search_ticket(ticket_id)

        if not ticket:
            # Show error not found screen
            TicketView.ticket_not_found(frame)

        # Unpack ticket attributes
        t_id, t_type, t_stat, t_is_paid, t_email, t_regular_code, t_fastpass_code, t_date_added, t_ticket_id = ticket

        ticket_id_label = tk.Label(window, text=t_ticket_id, justify='left', font=(
            'Inter', 15), bg=TicketView.BG_02)
        ticket_id_label.grid(row=1, column=1)

        frame.mainloop()

    def ticket_not_found(current_screen):
        # Close current screen
        current_screen.destroy()

        # Initialize view
        frame = tk.Tk()
        window = tk.Canvas(
            frame,
            height=TicketView.HEIGHT,
            width=TicketView.WIDTH,
            bg=TicketView.BG_01,
            highlightthickness=0
        )
        TicketView.start(frame, window)

        # Back button
        back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
        back_btn = tk.Button(window, image=back_img, command=lambda: TicketView.back(
            frame), bg=TicketView.BG_01)
        back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

        not_found_text = tk.Label(
            window, text='TIKET TIDAK DITEMUKAN BRADER!', justify='left', font=('Inter', 15))
        not_found_text.grid(row=1, column=1)

        frame.mainloop()

    def show_ticket_regular(current_screen, ticket_id, fastpass_code):
        # Close current screen
        current_screen.destroy()

        # Initialize view
        frame = tk.Tk()
        window = tk.Canvas(
            frame,
            height=TicketView.HEIGHT,
            width=TicketView.WIDTH,
            bg=TicketView.BG_01,
            highlightthickness=0
        )
        TicketView.start(frame, window)

        # Back button
        back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
        back_btn = tk.Button(window, image=back_img, command=lambda: TicketView.back(
            frame), bg=TicketView.BG_01)
        back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

        ticket_regular_text = tk.Label(
            window, text=f'Upgrade Tiket ID {ticket_id} (AKTIF)\nHarga: 150K\nKode Pembayaran: {fastpass_code}\n\nINGET SKYLINE GA HANDLE PEMBAYARAN', justify='left', font=('Inter', 15))
        ticket_regular_text.grid(row=1, column=1)

        frame.mainloop()

    def show_ticket_fastpass(current_screen, ticket_id):
        # Close current screen
        current_screen.destroy()

        # Initialize view
        frame = tk.Tk()
        window = tk.Canvas(
            frame,
            height=TicketView.HEIGHT,
            width=TicketView.WIDTH,
            bg=TicketView.BG_01,
            highlightthickness=0
        )
        TicketView.start(frame, window)

        # Back button
        back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
        back_btn = tk.Button(window, image=back_img, command=lambda: TicketView.back(
            frame), bg=TicketView.BG_01)
        back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

        ticket_fastpass_text = tk.Label(
            window, text=f'Tiket kamu sudah fastpass kok ^_^)~', justify='left', font=('Inter', 15))
        ticket_fastpass_text.grid(row=1, column=1)

        frame.mainloop()

    def show_ticket_not_active(current_screen):
        # Close current screen
        current_screen.destroy()

        # Initialize view
        frame = tk.Tk()
        window = tk.Canvas(
            frame,
            height=TicketView.HEIGHT,
            width=TicketView.WIDTH,
            bg=TicketView.BG_01,
            highlightthickness=0
        )
        TicketView.start(frame, window)

        # Back button
        back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
        back_btn = tk.Button(window, image=back_img, command=lambda: TicketView.back(
            frame), bg=TicketView.BG_01)
        back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

        ticket_not_active_text = tk.Label(
            window, text=f'Tiket kamu belum aktif. Ayo dong aktif jangan pasif terus :(\nJangan hilang di tubes juga ya :)', justify='left', font=('Inter', 15))
        ticket_not_active_text.grid(row=1, column=1)

        frame.mainloop()
