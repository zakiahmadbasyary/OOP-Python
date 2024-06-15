from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image, ImageTk

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background image
        self.bg = ImageTk.PhotoImage(file=r"bgfiks.png")  # Add the correct path for your background image here
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=400, y=190, width=750, height=400)

        img1 = Image.open("icon.png")  # Add the correct path for your image here
        img1 = img1.resize((300, 300), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg='white', borderwidth=0)
        lblimg1.place(x=400, y=190, width=400, height=400)

        get_str = Label(frame, text="Get Started", font=("calibri", 24, "bold"), fg="#57a1f8", bg="white")
        get_str.place(x=460, y=30)

        # Username label and entry
        username = Label(frame, text="Username", font=("calibri", 15, "bold"), fg="#57a1f8", bg="white")
        username.place(x=400, y=90)

        self.txtuser = ttk.Entry(frame, font=("calibri", 15, "normal"))
        self.txtuser.place(x=400, y=120, width=270)

        # Password label and entry
        password = Label(frame, text="Password", font=("calibri", 15, "bold"), fg="#57a1f8", bg="white")
        password.place(x=400, y=170)

        self.txtpass = ttk.Entry(frame, font=("calibri", 15, "normal"), show="*")
        self.txtpass.place(x=400, y=200, width=270)

        # Login button
        loginbtn = Button(frame, command=self.login, text="Login", font=("arial", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="#57a1f8", activeforeground="white", activebackground="#57a1f8")
        loginbtn.place(x=400, y=250, width=270, height=35)



    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "ZakiAB" and self.txtpass.get() == "0507":
            messagebox.showinfo("Success", "Welcome!")
            self.open_new_window()  # Memanggil fungsi untuk membuka halaman baru
        elif self.txtuser.get() == "AlihB" and self.txtpass.get() == "alih12":
            messagebox.showinfo("Success", "Welcome!")
            self.open_new_window()  # Memanggil fungsi untuk membuka halaman baru
        elif self.txtuser.get() == "LeoFetri" and self.txtpass.get() == "leo12":
            messagebox.showinfo("Success", "Welcome!")
            self.open_new_window()  # Memanggil fungsi untuk membuka halaman baru
        elif self.txtuser.get() == "AMauluddin" and self.txtpass.get() == "maul17":
            messagebox.showinfo("Success", "Welcome!")
            self.open_new_window()  # Memanggil fungsi untuk membuka halaman baru
        else:
            messagebox.showerror("Invalid", "Invalid username or password")

    def open_new_window(self):
        # Membuat jendela baru
        new_window = tk.Toplevel(self.root)
        new_window.title("Halaman Baru")
        new_window.geometry("400x300")

        # Frame untuk menempatkan gambar dan teks berdampingan
        frame = Frame(new_window)
        frame.pack(pady=20)

        # Menambahkan konten ke jendela baru
        label_text = "Selamat Datang \n" + self.txtuser.get()
        label = Label(frame, text=label_text, font=("times new roman", 15, "bold"))
        label.grid(row=0, column=1, padx=10, pady=10)

        # Membuka dan mengubah ukuran gambar (contoh, jika ada gambar)
        try:
            if self.txtuser.get() == "ZakiAB":
                img1 = Image.open("profilZaki.jpg")
            elif self.txtuser.get() == "AlihB":
                img1 = Image.open("Alih.png")
            elif self.txtuser.get() == "LeoFetri":
                img1 = Image.open("Leo.jpg")
            elif self.txtuser.get() == "AMauluddin":
                img1 = Image.open("maul.jpg")

            img1 = img1.resize((200, 250), Image.LANCZOS)
            photoimage1 = ImageTk.PhotoImage(img1)
            lblimg1 = Label(frame, image=photoimage1)
            lblimg1.image = photoimage1  
            lblimg1.grid(row=0, column=0, padx=10, pady=10)
        except FileNotFoundError:
            print("Gambar tidak ditemukan. Pastikan path gambar benar.")


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
