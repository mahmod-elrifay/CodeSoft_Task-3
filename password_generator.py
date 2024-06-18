from tkinter import *
import customtkinter
import random

def password():
    entry2.delete(0,END)
    v = int(entry1.get())
    passs = ""
    for i in range (v):
        passs += chr(random.randint(33,126))
    entry2.insert(0,passs)

# Set the color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

form = customtkinter.CTk()
# set window deminsions
form.geometry("350x200")
# set window title
form.title("Password Genrator")
# Make window unresizable
form.resizable(False,False)

# Set font to all objects
font = customtkinter.CTkFont(family="Bahnschrift",size=14)

# Main Frame
frame = customtkinter.CTkFrame(master=form,width=330,height=180)
frame.pack(pady=10)

# Entry that takes a length of password 
entry1 = customtkinter.CTkEntry(frame,corner_radius=8,width=190,fg_color="#212121",font=font,placeholder_text=("   Enter password length"),border_color="#383838")
entry1.place(relx=0.5,rely=0.15,anchor=CENTER)

# Generate button
btn = customtkinter.CTkButton(frame,corner_radius=20,text="Generate",font=font,width=230,fg_color="#282828",hover_color="#383838",command=password)
btn.place(relx=0.5,rely=0.35,anchor=CENTER)

# Entry that shows the password
entry2 = customtkinter.CTkEntry(frame,font=font,fg_color="#212121",corner_radius=15,width=170,placeholder_text="Password will appear here",border_color="#383838")
entry2.place(relx=0.5, rely=0.64, anchor=CENTER)

form.mainloop()