import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x700")  # Increased size to accommodate both tables

        # Database setup
        self.setup_db()

        # Variables for student management
        self.roll_no_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.contact_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        self.address_var = tk.StringVar()

        # Variables for course management
        self.course_code_var = tk.StringVar()
        self.course_name_var = tk.StringVar()
        self.course_credits_var = tk.IntVar()

        # Student Registration Frame
        self.student_registration_frame()
        
        # Course Management Frame
        self.course_management_frame()

        # Display Student Data in Table
        self.student_table_frame()
        self.fetch_students()

        # Display Course Data in Table
        self.course_table_frame()
        self.fetch_courses()

    def setup_db(self):
        """Setup the SQLite database and create tables."""
        conn = sqlite3.connect('student_management.db')
        cur = conn.cursor()
        # Student Table
        cur.execute('''CREATE TABLE IF NOT EXISTS students 
                       (roll_no INTEGER PRIMARY KEY, name TEXT, email TEXT, gender TEXT, contact TEXT, dob TEXT, address TEXT)''')
        # Course Table
        cur.execute('''CREATE TABLE IF NOT EXISTS courses 
                       (course_code TEXT PRIMARY KEY, course_name TEXT, credits INTEGER)''')
        conn.commit()
        conn.close()

    def student_registration_frame(self):
        """Create the frame for student registration."""
        frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="gray")
        frame.place(x=20, y=20, width=450, height=600)

        m_title = tk.Label(frame, text="Student Registration", bg="gray", fg="white", font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        lbl_roll = tk.Label(frame, text="Roll No.", bg="gray", fg="white", font=("times new roman", 15, "bold"))
        lbl_roll.grid(row=1, column=0, pady=5, padx=10, sticky="w")
        txt_roll = tk.Entry(frame, textvariable=self.roll_no_var, font=("times new roman", 13), bd=5, relief=tk.GROOVE)
        txt_roll.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        lbl_name = tk.Label(frame, text="Name", bg="gray", fg="white", font=("times new roman", 15, "bold"))
        lbl_name.grid(row=2, column=0, pady=5, padx=10, sticky="w")
        txt_name = tk.Entry(frame, textvariable=self.name_var, font=("times new roman", 13), bd=5, relief=tk.GROOVE)
        txt_name.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        lbl_email = tk.Label(frame, text="Email", bg="gray", fg="white", font=("times new roman", 15, "bold"))
        lbl_email.grid(row=3, column=0, pady=5, padx=10, sticky="w")
        txt_email = tk.Entry(frame, textvariable=self.email_var, font=("times new roman", 13), bd=5, relief=tk.GROOVE)
        txt_email.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        lbl_gender = tk.Label(frame, text="Gender", bg="gray", fg="white", font=("times new roman", 15, "bold"))
        lbl_gender.grid(row=4, column=0, pady=5, padx=10, sticky="w")
        combo_gender = ttk.Combobox(frame, textvariable=self.gender_var, font=("times new roman", 13), state='readonly')
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        lbl_contact = tk.Label(frame, text="Contact", bg="gray", fg="white", font=("times new roman", 15, "bold"))
        lbl_contact.grid(row=5, column=0, pady=5, padx=10, sticky="w")
        txt_contact = tk.Entry(frame, textvariable=self.contact_var, font=("times new roman", 13), bd=5, relief=tk.GROOVE)
        txt_contact.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        lbl_dob = tk.Label(frame, text="D.O.B", bg="gray", fg="white", font=("times new roman", 15, "bold"))
        lbl_dob.grid(row=6, column=0, pady=5, padx=10, sticky="w")
        txt_dob = tk.Entry(frame, textvariable=self.dob_var, font=("times new roman", 13), bd=5, relief=tk.GROOVE)
        txt_dob.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        lbl_address = tk.Label(frame, text="Address", bg="gray", fg="white", font=("times new roman", 15, "bold"))
        lbl_address.grid(row=7, column=0, pady=5, padx=10, sticky="w")
        txt_address = tk.Entry(frame, textvariable=self.address_var, font=("times new roman", 13), bd=5, relief=tk.GROOVE)
        txt_address.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        # Button Frame for Students
        btn_frame = tk.Frame(frame, bd=4, relief=tk.RIDGE, bg="gray")
        btn_frame.place(x=20, y=430, width=400)

        addbtn = tk.Button(btn_frame, text="Add", width=10, command=self.add_student).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = tk.Button(btn_frame, text="Update", width=10, command=self.update_student).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = tk.Button(btn_frame, text="Delete", width=10, command=self.delete_student).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = tk.Button(btn_frame, text="Clear", width=10, command=self.clear_student).grid(row=0, column=3, padx=10, pady=10)

    def course_management_frame(self):
        """Create the frame for course management."""
        frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="gray")
        frame.place(x=500, y=20, width=450, height=300)

        m_title = tk.Label(frame, text="Course Management", bg="gray", fg="white", font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        lbl_course_code = tk.Label(frame, text="Course Code", bg="gray", fg="white", font=("times new roman", 15, "bold"))
        lbl_course_code.grid(row=1, column=0, pady=5, padx=10, sticky="w")
        txt_course_code = tk.Entry(frame, textvariable=self.course_code_var, font=("times new roman", 13), bd=5, relief=tk.GROOVE)
        txt_course_code.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        lbl_course_name = tk.Label(frame, text="Course Name", bg="gray", fg="white", font=("times new roman", 15, "bold"))
        lbl_course_name.grid(row=2, column=0, pady=5, padx=10, sticky="w")
        txt_course_name = tk.Entry(frame, textvariable=self.course_name_var, font=("times new roman", 13), bd=5, relief=tk.GROOVE)
        txt_course_name.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        lbl_credits = tk.Label(frame, text="Credits", bg="gray", fg="white", font=("times new roman", 15, "bold"))
        lbl_credits.grid(row=3, column=0, pady=5, padx=10, sticky="w")
        txt_credits = tk.Entry(frame, textvariable=self.course_credits_var, font=("times new roman", 13), bd=5, relief=tk.GROOVE)
        txt_credits.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        # Button Frame for Courses
        btn_frame = tk.Frame(frame, bd=4, relief=tk.RIDGE, bg="gray")
        btn_frame.place(x=20, y=200, width=400)

        addbtn = tk.Button(btn_frame, text="Add", width=10, command=self.add_course).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = tk.Button(btn_frame, text="Update", width=10, command=self.update_course).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = tk.Button(btn_frame, text="Delete", width=10, command=self.delete_course).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = tk.Button(btn_frame, text="Clear", width=10, command=self.clear_course).grid(row=0, column=3, padx=10, pady=10)

    def student_table_frame(self):
        """Create a frame to display students' table with scrollbars."""
        table_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="gray")
        table_frame.place(x=20, y=640, width=1150, height=200)  # Positioned below both registration frames

        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("roll_no", "name", "email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll_no", text="Roll No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("address", text="Address")
        self.student_table['show'] = 'headings'

        self.student_table.column("roll_no", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("gender", width=70)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=200)

        self.student_table.pack(fill=tk.BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor_student)

    def course_table_frame(self):
        """Create a frame to display courses' table with scrollbars."""
        table_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="gray")
        table_frame.place(x=500, y=350, width=670, height=200)

        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)

        self.course_table = ttk.Treeview(table_frame, columns=("course_code", "course_name", "credits"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.course_table.xview)
        scroll_y.config(command=self.course_table.yview)

        self.course_table.heading("course_code", text="Course Code")
        self.course_table.heading("course_name", text="Course Name")
        self.course_table.heading("credits", text="Credits")
        self.course_table['show'] = 'headings'

        self.course_table.column("course_code", width=100)
        self.course_table.column("course_name", width=150)
        self.course_table.column("credits", width=100)

        self.course_table.pack(fill=tk.BOTH, expand=1)
        self.course_table.bind("<ButtonRelease-1>", self.get_cursor_course)

    # CRUD operations for students
    def add_student(self):
        if self.roll_no_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            conn = sqlite3.connect('student_management.db')
            cur = conn.cursor()
            try:
                cur.execute("INSERT INTO students (roll_no, name, email, gender, contact, dob, address) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (self.roll_no_var.get(),
                             self.name_var.get(),
                             self.email_var.get(),
                             self.gender_var.get(),
                             self.contact_var.get(),
                             self.dob_var.get(),
                             self.address_var.get()))
                conn.commit()
                self.fetch_students()
                self.clear_student()
                messagebox.showinfo("Success", "Student added successfully.")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Roll number already exists.")
            finally:
                conn.close()

    def update_student(self):
        # Code for updating student
        pass

    def delete_student(self):
        # Code for deleting student
        pass

    def clear_student(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.address_var.set("")

    def fetch_students(self):
        conn = sqlite3.connect('student_management.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', 'end', values=row)
            conn.commit()
        conn.close()

    def get_cursor_student(self, event):
        # Functionality to fill fields when row is selected
        pass

    # CRUD operations for courses
    def add_course(self):
        if self.course_code_var.get() == "" or self.course_name_var.get() == "" or self.course_credits_var.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            conn = sqlite3.connect('student_management.db')
            cur = conn.cursor()
            try:
                cur.execute("INSERT INTO courses (course_code, course_name, credits) VALUES (?, ?, ?)",
                            (self.course_code_var.get(),
                             self.course_name_var.get(),
                             self.course_credits_var.get()))
                conn.commit()
                self.fetch_courses()
                self.clear_course()
                messagebox.showinfo("Success", "Course added successfully.")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Course code already exists.")
            finally:
                conn.close()

    def update_course(self):
        # Code for updating course
        pass

    def delete_course(self):
        # Code for deleting course
        pass

    def clear_course(self):
        self.course_code_var.set("")
        self.course_name_var.set("")
        self.course_credits_var.set("")

    def fetch_courses(self):
        conn = sqlite3.connect('student_management.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM courses")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('', 'end', values=row)
            conn.commit()
        conn.close()

    def get_cursor_course(self, event):
        # Functionality to fill fields when row is selected
        pass

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
