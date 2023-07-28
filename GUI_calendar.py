from tkinter import *
from tkcalendar import Calendar

root = Tk()
root.geometry("600x150")
root.configure(background="#003366")
date_window = None
def pick_date(event):
    global date_window
    date_window = Toplevel()
    date_window.grab_set()
    date_window.title('Calendar')
    date_window.geometry('300x250+590+370')
    date_window.configure(background="#336699")

    cal = Calendar(date_window, selectmode="day", date_pattern="dd/mm/yyyy", background="white", foreground="black", selectbackground="#003366", selectforeground="white")
    cal.pack(pady=20)

    submit_btn = Button(date_window, text="Select the Date", command=lambda: grab_date(cal), bg="#003366", fg="white", font=("Helvetica", 12, "bold"))
    submit_btn.place(x=90, y=215)

def grab_date(cal):
    selected_date = cal.get_date()
    date_entry_var.set(selected_date)
    #THIS CODE 👇👇 IS FOR HIDING THE CALENDAR AFTER SELECTING THE DATE
    date_window.destroy()

date_label = Label(root, text="Get Date:", bg="#003366", fg="white", font=("Helvetica", 14, "bold"))
date_label.place(x=200, y=60)

date_entry_var = StringVar()
date_entry = Entry(root, textvariable=date_entry_var, highlightthickness=0, relief=FLAT, bg="White", fg="#003366", font=("Helvetica", 12, "bold"))
date_entry.place(x=300, y=63, width=100)
date_entry.insert(0, "dd/mm/yyyy")

date_entry.bind("<1>", pick_date)

root.mainloop()
