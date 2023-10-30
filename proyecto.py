
import customtkinter
import customtkinter as ctk
import tkinter as tk
import tkinter


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)
# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("Dark")
 
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("dark-blue")   
app = customtkinter.CTk()
app.geometry("400x500")
optionmenu_var = customtkinter.StringVar(value="option 2")  # set initial value


combobox = customtkinter.CTkOptionMenu(master=app,
                                       values=["option 1", "option 2"],
                                       command=optionmenu_callback,
                                       variable=optionmenu_var)
combobox.pack(padx=20, pady=10)


app.mainloop()