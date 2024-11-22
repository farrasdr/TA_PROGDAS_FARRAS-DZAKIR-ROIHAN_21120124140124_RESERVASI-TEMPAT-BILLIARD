import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class Reservation:
    def __init__(self, name, date, time, num_players, table_type, ruangan, stick, price, payment_method):
        self.name = name
        self.date = date
        self.time = time
        self.num_players = num_players
        self.table_type = table_type
        self.ruangan = ruangan
        self.stick = stick
        self.price = price
        self.payment_method = payment_method
        
    def display(self):
        return (f"Detail Reservasi:\n"
                f"Nama: {self.name}\n"
                f"Tanggal: {self.date}\n"
                f"Waktu: {self.time}\n"
                f"Jumlah Pemain: {self.num_players}\n"
                f"Jenis Meja: {self.table_type}\n"
                f"Ruangan Biliar: {self.ruangan}\n"
                f"Stick Biliar: {self.stick}\n"
                f"Harga: Rp{self.price:.2f}\n"
                f"Metode Pembayaran: {self.payment_method}\n")

class ReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Reservasi Biliar")
        self.root.configure(background="#6a0dad")  # Background ungu
        self.reservations = []

        # Harga default
        self.regular_table_price = 50000
        self.vip_table_price = 80000
        self.reguler_ruangan_price = 40000
        self.vip_ruangan_price = 60000
        self.reguler_stick_price = 20000
        self.carbon_stick_price = 35000

        self.create_main_menu()

    def create_main_menu(self):
        main_frame = ttk.Frame(self.root, padding="10 10 10 10", style="Main.TFrame")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text="Sistem Reservasi Biliar", font=("Arial", 16), background="#6a0dad", foreground="white").grid(row=0, column=0, columnspan=2, pady=20)

        self.make_reservation_button = ttk.Button(main_frame, text="Buat Reservasi", command=self.open_make_reservation, style="Main.TButton")
        self.make_reservation_button.grid(row=1, column=0, columnspan=2, pady=10, padx=20, ipadx=10)

        self.view_reservations_button = ttk.Button(main_frame, text="Lihat Reservasi", command=self.open_view_reservations, style="Main.TButton")
        self.view_reservations_button.grid(row=2, column=0, columnspan=2, pady=10, padx=20, ipadx=10)

    def open_make_reservation(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Buat Reservasi")
        self.new_window.configure(background="#8a2be2")  # Background ungu muda
        self.create_reservation_widgets(self.new_window)

    def open_view_reservations(self):
        self.display_reservations(self.root)

    def create_reservation_widgets(self, window):
        window.geometry("600x500")
        main_frame = ttk.Frame(window, padding="10 10 10 10", style="Reservation.TFrame")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Tampilkan daftar harga
        self.display_prices(main_frame)

        # Buat label dan entri untuk detail reservasi
        ttk.Label(main_frame, text="Nama:", style="Reservation.TLabel").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.name_entry = ttk.Entry(main_frame)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.name_entry.bind("<Return>", lambda event: self.date_entry.focus())

        ttk.Label(main_frame, text="Tanggal (DD-MM-YYYY):", style="Reservation.TLabel").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.date_entry = ttk.Entry(main_frame)
        self.date_entry.grid(row=2, column=1, padx=10, pady=5)
        self.date_entry.bind("<Return>", lambda event: self.time_entry.focus())

        ttk.Label(main_frame, text="Waktu (HH:MM):", style="Reservation.TLabel").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.time_entry = ttk.Entry(main_frame)
        self.time_entry.grid(row=3, column=1, padx=10, pady=5)
        self.time_entry.bind("<Return>", lambda event: self.num_players_entry.focus())

        ttk.Label(main_frame, text="Jumlah Pemain:", style="Reservation.TLabel").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.num_players_entry = ttk.Entry(main_frame)
        self.num_players_entry.grid(row=4, column=1, padx=10, pady=5)
        self.num_players_entry.bind("<Return>", lambda event: self.table_type.set("Regular"))

        # Buat opsi untuk jenis meja, ruangan biliar, dan tongkat biliar
        ttk.Label(main_frame, text="Jenis Meja:", style="Reservation.TLabel").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
        self.table_type = tk.StringVar()
        self.table_type.set("Regular")
        ttk.Radiobutton(main_frame, text="Regular", variable=self.table_type, value="Regular", style="Reservation.TRadiobutton").grid(row=5, column=1, sticky=tk.W, padx=10)
        ttk.Radiobutton(main_frame, text="VIP", variable=self.table_type, value="VIP", style="Reservation.TRadiobutton").grid(row=5, column=2, sticky=tk.W, padx=10)

        ttk.Label(main_frame, text="Ruangan Biliar:", style="Reservation.TLabel").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
        self.ruangan = tk.StringVar()
        self.ruangan.set("Ruangan Biliar Reguler")
        ttk.Radiobutton(main_frame, text="Ruangan Biliar Reguler", variable=self.ruangan, value="Ruangan Biliar Reguler", style="Reservation.TRadiobutton").grid(row=6, column=1, sticky=tk.W, padx=10)
        ttk.Radiobutton(main_frame, text="Ruangan Biliar VIP", variable=self.ruangan, value="Ruangan Biliar VIP", style="Reservation.TRadiobutton").grid(row=6, column=2, sticky=tk.W, padx=10)

        ttk.Label(main_frame, text="Stick Biliar:", style="Reservation.TLabel").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
        self.stick = tk.StringVar()
        self.stick.set("Stick Biliar Reguler")
        ttk.Radiobutton(main_frame, text="Stick Biliar Reguler", variable=self.stick, value="Stick Biliar Reguler", style="Reservation.TRadiobutton").grid(row=7, column=1, sticky=tk.W, padx=10)
        ttk.Radiobutton(main_frame, text="Stick Biliar Carbon", variable=self.stick, value="Stick Biliar Carbon", style="Reservation.TRadiobutton").grid(row=7, column=2, sticky=tk.W, padx=10)

        # Payment Method
        ttk.Label(main_frame, text="Metode Pembayaran:", style="Reservation.TLabel").grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)
        self.payment_method = ttk.Combobox(main_frame, values=["Cash", "Transfer", "E-wallet"], state="readonly")
        self.payment_method.set("Cash")
        self.payment_method.grid(row=8, column=1, padx=10, pady=5)

        # Buat tombol untuk membuat reservasi
        self.make_reservation_button = ttk.Button(main_frame, text="Buat Reservasi", command=self.make_reservation, style="Reservation.TButton")
        self.make_reservation_button.grid(row=9, column=0, columnspan=3, pady=10)

        self.reservation_output = tk.Text(main_frame, width=80, height=10)
        self.reservation_output.grid(row=10, column=0, columnspan=4, padx=10, pady=10)
        self.reservation_output.config(state=tk.DISABLED)

    def display_prices(self, window):
        prices = self.get_prices()
        price_list = (f"Daftar Harga:\n"
                      f"Meja Regular: Rp{prices['Meja Regular']:.2f}\n"
                      f"Meja VIP    : Rp{prices['Meja VIP']:.2f}\n"
                      f"Ruangan Biliar Reguler: Rp{prices['Ruangan Biliar Reguler']:.2f}\n"
                      f"Ruangan Biliar VIP: Rp{prices['Ruangan Biliar VIP']:.2f}\n"
                      f"Stick Biliar Reguler: Rp{prices['Stick Biliar Reguler']:.2f}\n"
                      f"Stick Biliar Carbon: Rp{prices['Stick Biliar Carbon']:.2f}\n")

        self.price_label = ttk.Label(window, text=price_list, justify=tk.LEFT, background="#8a2be2", foreground="white")
        self.price_label.grid(row=0, column=0, columnspan=4, sticky=tk.W, padx=10, pady=5)

    def calculate_price(self, table_type, ruangan, stick):
        price = 0.0
        if table_type == "Regular":
            price += self.regular_table_price
        elif table_type == "VIP":
            price += self.vip_table_price
        
        if ruangan == "Ruangan Biliar VIP":
            price += self.vip_ruangan_price
        else:
            price += self.reguler_ruangan_price
        
        if stick == "Stick Biliar Carbon":
            price += self.carbon_stick_price
        else:
            price += self.reguler_stick_price

        return price

    def make_reservation(self):
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        num_players = self.num_players_entry.get()
        table_type = self.table_type.get()
        ruangan = self.ruangan.get()
        stick = self.stick.get()
        payment_method = self.payment_method.get()

        if not name or not date or not time or not num_players:
            messagebox.showerror("Error", "Harap mengisi sesuai kolom.")
            return
    
        try:
            num_players = int(num_players)
            if num_players <= 0:
                messagebox.showerror("Error", "Jumlah pemain harus lebih dari 0.")
                return
        except ValueError:
            messagebox.showerror("Error", "Jumlah pemain harus berupa angka.")
            return
        
        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            messagebox.showerror("Error", "Format tanggal salah. Gunakan format DD-MM-YYYY.")
            return
        
        price = self.calculate_price(table_type, ruangan, stick)
        reservation = Reservation(name, date, time, num_players, table_type, ruangan, stick, price, payment_method)
        self.reservations.append(reservation)
        
        self.reservation_output.config(state=tk.NORMAL)
        self.reservation_output.insert(tk.END, reservation.display() + "\n")
        self.reservation_output.config(state=tk.DISABLED)
        messagebox.showinfo("Sukses", f"Reservasi berhasil dibuat! Total harga: Rp{price:.2f}")

    def display_reservations(self, window):
        if not self.reservations:
            messagebox.showinfo("Reservasi", "Belum ada reservasi yang dibuat.")
            return

        reservations_details = ""
        for index, reservation in enumerate(self.reservations, 1):
            reservations_details += f"Reservasi {index}:\n{reservation.display()}\n"

        top = tk.Toplevel(window)
        top.title("Lihat Reservasi")
        top.configure(background="#8a2be2")
        top.geometry("600x500")
        main_frame = ttk.Frame(top, padding="10 10 10 10", style="Reservation.TFrame")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        reservation_output = tk.Text(main_frame, width=80, height=20)
        reservation_output.insert(tk.END, reservations_details)
        reservation_output.config(state=tk.DISABLED)
        reservation_output.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    def set_prices(self, regular_table_price, vip_table_price, reguler_ruangan_price, vip_ruangan_price, reguler_stick_price, carbon_stick_price):
        self.regular_table_price = regular_table_price
        self.vip_table_price = vip_table_price
        self.reguler_ruangan_price = reguler_ruangan_price
        self.vip_ruangan_price = vip_ruangan_price
        self.reguler_stick_price = reguler_stick_price
        self.carbon_stick_price = carbon_stick_price

    def get_prices(self):
        return {
            "Meja Regular": self.regular_table_price,
            "Meja VIP": self.vip_table_price,
            "Ruangan Biliar Reguler": self.reguler_ruangan_price,
            "Ruangan Biliar VIP": self.vip_ruangan_price,
            "Stick Biliar Reguler": self.reguler_stick_price,
            "Stick Biliar Carbon": self.carbon_stick_price
        }

if __name__ == "__main__":
    root = tk.Tk()

    style = ttk.Style()

    style.configure("Main.TFrame", background="#6a0dad")
    style.configure("Main.TButton", font=("Times New Roman", 12), padding=10)
    style.configure("Reservation.TFrame", background="#8a2be2")
    style.configure("Reservation.TLabel", background="#8a2be2", font=("Aptos Display", 10), foreground="white")
    style.configure("Reservation.TRadiobutton", background="#8a2be2", foreground="white")
    style.configure("Reservation.TButton", font=("forte", 12), padding=10)

    app = ReservationSystem(root)
    root.mainloop()
