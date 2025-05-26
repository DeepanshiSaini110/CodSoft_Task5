import tkinter as tk
from tkinter import messagebox, simpledialog

contact_book = {}  
temp_var = None  

def make_contact():
    print("Opening contact creation dialog...")  
    nm = simpledialog.askstring("Create Contact", "Enter Name:")
    if not nm:
        print("No name entered")  
        return
    if nm in contact_book:
        messagebox.showwarning("Warning", f"Contact '{nm}' already exists!")
        return
    try:
        ag = int(simpledialog.askstring("Create Contact", "Enter Age:"))
    except:
        messagebox.showerror("Invalid Input", "Age must be a number.")
        return

    em = simpledialog.askstring("Create Contact", "Enter Email:")
    mob = simpledialog.askstring("Create Contact", "Enter Mobile:")
    add = simpledialog.askstring("Create Contact", "Enter Address:")

    contact_book[nm] = {'age': ag,'email': em,'mobile': mob,'address': add}

    print(f"Contact {nm} saved!")  
    messagebox.showinfo("Success", f"Contact '{nm}' created successfully!")

def see_contact():
    n = simpledialog.askstring("View Contact", "Enter Contact Name:")
    if n in contact_book:
        con = contact_book[n]
        result = f"Name: {n}\nAge: {con['age']}\nMobile: {con['mobile']}\nEmail: {con['email']}\nAddress: {con['address']}"
        messagebox.showinfo("Contact Details", result)
    else:
        print("Lookup failed:", n)  
        messagebox.showerror("Not Found", f"No contact found with name '{n}'")

def change_contact():
    namex = simpledialog.askstring("Update Contact", "Enter Name to Update:")
    if namex in contact_book:
        try:
            age2 = int(simpledialog.askstring("Update Contact", "Enter New Age:"))
        except:
            messagebox.showerror("Invalid Input", "Age must be a number.")
            return
        em2 = simpledialog.askstring("Update Contact", "Enter New Email:")
        mob2 = simpledialog.askstring("Update Contact", "Enter New Mobile:")
        addr2 = simpledialog.askstring("Update Contact", "Enter New Address:")

        contact_book[namex] = {'age': age2,'email': em2,'mobile': mob2,'address': addr2}

        print(f"{namex} updated.") 
        messagebox.showinfo("Updated", f"Contact '{namex}' updated.")
    else:
        messagebox.showerror("Not Found", f"No contact found with name '{namex}'")

def remove_contact():
    nm = simpledialog.askstring("Delete Contact", "Enter Name to Delete:")
    if nm in contact_book:
        ok = messagebox.askyesno("Confirm", f"Really delete '{nm}'?")
        if ok:
            del contact_book[nm]
            messagebox.showinfo("Deleted", f"'{nm}' removed.")
        else:
            print("Deletion cancelled.") 
    else:
        messagebox.showerror("Not Found", f"No contact with name '{nm}'")

def find_contact():
    key = simpledialog.askstring("Search Contact", "Enter Name to Search:")
    if not key:
        return
    matches = []
    for k in contact_book:
        if key.lower() in k.lower():
            data = contact_book[k]
            matches.append(f"{k} - {data['mobile']} | {data['email']}")
    if matches:
        messagebox.showinfo("Search Result", "\n".join(matches))
    else:
        messagebox.showinfo("Not Found", "No match.")

def total_contacts():
    total = len(contact_book)
    print("Counting contacts:", total) 
    messagebox.showinfo("Total Contacts", f"Total: {total}")

def close_program():
    sure = messagebox.askyesno("Exit","Are You Quit The Page")
    if sure:
        print("Exiting app...") 
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Contact Book!")
root.geometry("400x450")
root.config(bg="#1D0902")
root.resizable(False, False)

# Title
lbl = tk.Label(root, text="📒CONTACT BOOK", font=("Arial", 17, "bold"), bg="#0C0700", fg="#FBF6ED")
lbl.pack(pady=30)

# Buttons
fnt = ("Arial", 12)
btns = [("Create Contact", make_contact),("View Contact", see_contact),("Update Contact", change_contact),
    ("Delete Contact", remove_contact),("Search Contact", find_contact),("Count Contacts", total_contacts),
    ("Exit", close_program)
]

# Draw buttons
for txt, fn in btns:
    b = tk.Button(root, text=txt, font=fnt, width=25, command=fn, bg="#FCD69C")
    b.pack(pady=5)

# Run
root.mainloop()
