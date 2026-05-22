import tkinter as tk
from tkinter import messagebox

# ---------------- Main Window ----------------

root = tk.Tk()
root.title("Login System")
root.geometry("420x500")
root.resizable(False, False)


# ---------------- Helper Function ----------------

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# ---------------- User Registration Function ----------------

def register_user(username, email, password):
    with open("users.txt", "a") as file:
        file.write(username + "," + email + "," + password + "\n")


# ---------------- Login Checking Function ----------------

def check_login(username, password):
    try:
        with open("users.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 3:
                    saved_username = data[0]
                    saved_password = data[2]

                    if username == saved_username and password == saved_password:
                        return True

        return False

    except FileNotFoundError:
        return False


# ---------------- Signup Window ----------------

def signup_window():
    clear_window()
    root.title("Signup")

    tk.Label(
        root,
        text="Signup",
        font=("Arial", 24, "bold")
    ).pack(pady=25)

    tk.Label(root, text="Username").pack(pady=5)
    username_entry = tk.Entry(root, width=30)
    username_entry.pack(pady=5)

    tk.Label(root, text="Email").pack(pady=5)
    email_entry = tk.Entry(root, width=30)
    email_entry.pack(pady=5)

    tk.Label(root, text="Password").pack(pady=5)
    password_entry = tk.Entry(root, width=30, show="*")
    password_entry.pack(pady=5)

    def signup():
        username = username_entry.get().strip()
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if username == "" or email == "" or password == "":
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        if "@" not in email or "." not in email:
            messagebox.showwarning("Email Error", "Please enter a valid email address!")
            return

        register_user(username, email, password)

        messagebox.showinfo("Success", "Signup successful! Please login.")
        login_window()

    tk.Button(
        root,
        text="Signup",
        width=22,
        command=signup
    ).pack(pady=15)

    tk.Button(
        root,
        text="Back to Login",
        width=22,
        command=login_window
    ).pack(pady=5)


# ---------------- Login Window ----------------

def login_window():
    clear_window()
    root.title("Login System")

    tk.Label(
        root,
        text="Login",
        font=("Arial", 24, "bold")
    ).pack(pady=35)

    tk.Label(root, text="Username").pack(pady=5)
    username_entry = tk.Entry(root, width=30)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password").pack(pady=5)
    password_entry = tk.Entry(root, width=30, show="*")
    password_entry.pack(pady=5)

    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if username == "" or password == "":
            messagebox.showwarning("Input Error", "Please enter username and password!")
            return

        if check_login(username, password):
            messagebox.showinfo("Success", "Login successful!")
            welcome_window(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    tk.Button(
        root,
        text="Login",
        width=22,
        command=login
    ).pack(pady=15)

    tk.Button(
        root,
        text="Go to Signup",
        width=22,
        command=signup_window
    ).pack(pady=5)


# ---------------- Welcome / Dashboard Window ----------------

def welcome_window(username):
    clear_window()
    root.title("Dashboard")

    tk.Label(
        root,
        text="Welcome " + username,
        font=("Arial", 22, "bold")
    ).pack(pady=35)

    tk.Button(
        root,
        text="Student Manager",
        width=25,
        command=lambda: student_manager_window(username)
    ).pack(pady=10)

    tk.Button(
        root,
        text="Option 1",
        width=25,
        command=option_one
    ).pack(pady=10)

    tk.Button(
        root,
        text="Option 2",
        width=25,
        command=option_two
    ).pack(pady=10)

    tk.Button(
        root,
        text="Logout",
        width=25,
        command=login_window
    ).pack(pady=20)


# ---------------- Option 1 Function ----------------

def option_one():
    messagebox.showinfo("Option 1", "You selected Option 1.")


# ---------------- Option 2 Function ----------------

def option_two():
    messagebox.showinfo("Option 2", "You selected Option 2.")


# ---------------- Student Manager Window ----------------

def student_manager_window(username):
    clear_window()
    root.title("Student Manager")

    tk.Label(
        root,
        text="Student Manager",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    tk.Label(root, text="Enter Student Name").pack(pady=10)

    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)

    # Add Student Function
    def add_student():
        name = entry.get().strip()

        if name == "":
            messagebox.showwarning("Input Error", "Name cannot be empty!")
            return

        try:
            with open("students.txt", "a") as file:
                file.write(name + "\n")

            messagebox.showinfo("Success", "Student added successfully!")
            entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # View Students Function
    def view_students():
        try:
            with open("students.txt", "r") as file:
                data = file.read()

            if data == "":
                messagebox.showinfo("Students", "No students found!")
            else:
                messagebox.showinfo("Student List", data)

        except FileNotFoundError:
            messagebox.showinfo("Students", "No students found yet!")

    tk.Button(
        root,
        text="Add Student",
        width=22,
        command=add_student
    ).pack(pady=10)

    tk.Button(
        root,
        text="View Students",
        width=22,
        command=view_students
    ).pack(pady=10)

    tk.Button(
        root,
        text="Back to Dashboard",
        width=22,
        command=lambda: welcome_window(username)
    ).pack(pady=10)

    tk.Button(
        root,
        text="Logout",
        width=22,
        command=login_window
    ).pack(pady=10)


# ---------------- Start Application ----------------

login_window()
root.mainloop()