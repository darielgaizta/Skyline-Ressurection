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
            padx=(0, 450),
            pady=20
        )

        # # Form input: email
        email_label = tk.Label(window, text='Email', justify='center', font=(
            'Inter', 10), bg=TicketView.BG_01)
        email_label.grid(
            row=5,
            column=1,
            padx=(0, 570)
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
            padx=(0, 530)
        )
        total_entry = ttk.Entry(window, width=100)
        total_entry.grid(
            row=8,
            column=1,
            padx=(0, 0)
        )
        max_ticket_label = tk.Label(window, text="*Maks pembelian jumlah tiket dalam satu kali pembayaran adalah 10",
                                    font=("Inter", 10, "italic"), bg=TicketView.BG_01, fg="red")
        max_ticket_label.grid(row=9, column=1, padx=(0, 200))

        # # Submit button
        def submit():
            controller.TicketController.buy_ticket(
                int(total_entry.get()), email_entry.get())
            TicketView.buy_success(frame)
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

        ticket = controller.TicketController.search_ticket(ticket_id)

        if not ticket:
            # Show error not found screen
            TicketView.ticket_not_found(frame)

        # Unpack ticket attributes
        t_id, t_type, t_stat, t_is_paid, t_email, t_regular_code, t_fastpass_code, t_date_added, t_ticket_id = ticket

        # Container ticket data
        ticket_data_container = tk.Canvas(
            window, bg=TicketView.BG_03, highlightthickness=0)
        ticket_data_container.grid(row=0, column=1)

        if t_type == 'Regular':
            # Show regular ticket code
            code_label = tk.Label(ticket_data_container, bg=TicketView.BG_03, fg="white",
                                  text=("Kode", t_type, t_regular_code), font=("Inter", 25, "bold"))
        else:
            # Show fastpass ticket code
            code_label = tk.Label(ticket_data_container, bg=TicketView.BG_03, fg="white",
                                  text=("Kode", t_type, t_fastpass_code), font=("Inter", 25, "bold"))
        code_label.grid(row=0, column=0, columnspan=2, pady=(50, 0))

        # Show barcode
        barcode_img = tk.PhotoImage(file=PATH_IMG+"\\barcode.png")
        barcode = tk.Label(ticket_data_container,
                           image=barcode_img, bg=TicketView.BG_03)
        barcode.grid(row=1, column=1, pady=20)

        # Ticket detail container
        detail_ticket_container = tk.Canvas(
            ticket_data_container, bg=TicketView.BG_03, highlightthickness=0)
        detail_ticket_container.grid(row=2, column=1, padx=100, pady=(0, 50))

        # Show ticket life-time
        if t_type == 'Regular':
            ticket_lifetime = tk.Label(
                detail_ticket_container, text="Skyline Reguler - ONE DAY TICKET", justify='left', font=("Inter", 25, "bold"), bg=TicketView.BG_03, fg="white")
            id_label = tk.Label(detail_ticket_container, text=("ID:", t_regular_code),
                                fg="white", bg=TicketView.BG_03, font=("Inter", 25))
        else:
            ticket_lifetime = tk.Label(
                detail_ticket_container, text="Skyline Fastpass - ONE DAY TICKET", justify='left', font=("Inter", 25, "bold"), bg=TicketView.BG_03, fg="white")
            id_label = tk.Label(detail_ticket_container, text=("ID:", t_fastpass_code),
                                fg="white", bg=TicketView.BG_03, font=("Inter", 25))
        ticket_lifetime.grid(row=0, column=0)
        id_label.grid(row=1, column=0)

        # Show ticket status
        status_label = tk.Label(detail_ticket_container, text=("Status:", t_stat),
                                fg="white", bg=TicketView.BG_03, font=("Inter", 25))
        status_label.grid(row=2, column=0)

        if t_is_paid == 0:
            pembayaran_label = tk.Label(detail_ticket_container, text="Pembayaran: Belum Dibayar",
                                        fg="white", bg=TicketView.BG_03, font=("Inter", 25))
        else:
            pembayaran_label = tk.Label(detail_ticket_container, text="Pembayaran: Sudah Dibayar",
                                        fg="white", bg=TicketView.BG_03, font=("Inter", 25))
        pembayaran_label.grid(row=3, column=0)

        email_label = tk.Label(detail_ticket_container, text=("Email:", t_email),
                               fg="white", bg=TicketView.BG_03, font=("Inter", 25))
        email_label.grid(row=4, column=0)

        tanggal_label = tk.Label(detail_ticket_container, text=("Tanggal:", t_date_added),
                                 fg="white", bg=TicketView.BG_03, font=("Inter", 25))
        tanggal_label.grid(row=5, column=0)

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

        # # Search form input
        # search_entry = ttk.Entry(window, width=125)
        # search_entry.grid(
        #     row=0,
        #     column=1,
        #     columnspan=2
        # )

        # Notification container
        notification_container = tk.Canvas(
            window, bg="#CF5C36", highlightthickness=0)
        notification_container.grid(row=0, column=1)

        # Ticket not found notification
        text_ticket_not_found = tk.Label(
            notification_container, fg="#FFFFFF", bg="#CF5C36", font=("Inter Regular", 40, 'bold'), text="Tiket Tidak\n Ditemukan")
        text_ticket_not_found.grid(row=1, column=1, pady=(140, 70), padx=100)

        text_next_step = tk.Label(
            notification_container, fg="#FFFFFF", bg="#CF5C36", font=("Inter Regular", 20), text="Silahkan masukan kembali ID Tiket anda")
        text_next_step.grid(row=2, column=1, pady=(0, 140), padx=100)

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

        # Logo Skyline
        logo_container = tk.Canvas(
            frame, bg=TicketView.BG_03, highlightthickness=0)
        logo_container.grid(row=0, column=0, ipadx=800, ipady=10, pady=(0, 10))
        logo = tk.Label(logo_container, text="SKYLINE", font=(
            "Impact", 40), fg="white", bg="#CF5C36", justify="left")
        logo.grid(row=0, column=0)

        # Back button
        back_img = tk.PhotoImage(file=PATH_IMG+'\\back.png')
        back_btn = tk.Button(window, image=back_img, command=lambda: TicketView.back_to_upgrade(
            frame), bg=TicketView.BG_01)
        back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

        img_ticket = tk.PhotoImage(file=PATH_IMG+"\\Ticket.png")
        tiket = tk.Label(window, image=img_ticket, bg="#DDC48E")
        tiket.grid(row=0, column=1, pady=(0, 20))

        # Ticket type container
        jenis_tiket_container = tk.Canvas(
            window, bg="#CF5C36", highlightthickness=0)
        jenis_tiket_container.grid(row=2, column=1)

        # Ticket type
        text_jenis_tiket = tk.Label(
            jenis_tiket_container, fg="#FFFFFF", bg="#CF5C36", font=("Inter Regular", 35), text="Tipe Tiket : Regular")
        text_jenis_tiket.grid(row=1, column=1, pady=(30, 70), padx=150)

        def upgrade_to_fastpass():
            controller.TicketController.upgrade_ticket(
                ticket_id, fastpass_code)
            TicketView.upgrade_success(frame)

        # Upgrade button to fastpass
        img_button_upgrade = tk.PhotoImage(
            file=PATH_IMG+"\\to_fastpass_btn.png")
        button_upgrade = ttk.Button(
            jenis_tiket_container, image=img_button_upgrade, command=upgrade_to_fastpass)
        button_upgrade.grid(row=2, column=1, pady=(0, 30))

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

        img_ticket = tk.PhotoImage(file=PATH_IMG+"\\Ticket.png")
        tiket = tk.Label(window, image=img_ticket, bg="#DDC48E")
        tiket.grid(row=0, column=1, pady=(0, 20))

        # Ticket type container
        jenis_tiket_container = tk.Canvas(
            window, bg="#CF5C36", highlightthickness=0)
        jenis_tiket_container.grid(row=2, column=1)

        # Ticket type
        text_jenis_tiket = tk.Label(
            jenis_tiket_container, fg="#FFFFFF", bg="#CF5C36", font=("Inter Regular", 35), text="Tipe Tiket : Fastpass")
        text_jenis_tiket.grid(row=1, column=1, pady=(30, 70), padx=100)

        text_tercepat = tk.Label(
            jenis_tiket_container, fg="#FFE600", bg="#CF5C36", font=("Inter Regular", 30), text="Anda berada di jalur tercepat!")
        text_tercepat.grid(row=2, column=1, pady=(30, 70), padx=100)

        frame.mainloop()

    def buy_success(current_screen):
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

        # Notification container
        text_container = tk.Canvas(
            window, bg=TicketView.BG_03, highlightthickness=0)
        text_container.grid(row=0, column=1)

        # Notification
        text1 = tk.Label(text_container, text="Terimakasih", font=(
            "Inter", 35, "bold"), bg="#CF5C36", fg="white")
        text1.grid(row=0, column=1, pady=(150, 20), padx=100)

        text2 = tk.Label(text_container, text="Silahkan lakukan pembayaran\ndengan kode yang tertera\npada email", font=(
            "Inter Regular", 35), bg="#CF5C36", fg="white")
        text2.grid(row=1, column=1, pady=(20, 150), padx=100)

        frame.mainloop()

    def upgrade_success(current_screen):
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
        back_img = tk.PhotoImage(file=PATH_IMG+"\\back.png")
        back_btn = tk.Button(window, image=back_img, command=lambda: TicketView.back(
            frame), bg=TicketView.BG_01)
        back_btn.grid(row=0, column=0, padx=(0, 10), sticky='n')

        # Notification container
        text_container = tk.Canvas(
            window, bg=TicketView.BG_03, highlightthickness=0)
        text_container.grid(row=0, column=1)

        # Notification
        text1 = tk.Label(text_container, text="Request\nUpgradeTerkonfirmasi", font=(
            "Inter", 35, "bold"), bg="#CF5C36", fg="white")
        text1.grid(row=0, column=1, pady=(150, 20), padx=100)

        text2 = tk.Label(text_container, text="Silahkan lakukan pembayaran\ndengan kode yang tertera\npada email", font=(
            "Inter Regular", 35), bg="#CF5C36", fg="white")
        text2.grid(row=1, column=1, pady=(20, 150), padx=100)

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
