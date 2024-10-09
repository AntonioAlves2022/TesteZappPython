import tkinter
from tkinter import *
import keyboard
import pywhatkit as pwk
import time
from _datetime import datetime

def btn_clicked():
    print("Button Clicked")

window = Tk()

window.geometry("320x480")
window.title("Zapi Zapi")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 480,
    width = 320,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    150.0, 234.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    164.0, 133.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 27.0, y = 117,
    width = 274.0,
    height = 30)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    164.0, 262.5,
    image = entry1_img)

entry1 = Text(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 27.0, y = 188,
    width = 274.0,
    height = 147)

# Dados para o Envio


def send_message():
    telefone = '+55' + entry0.get()

    mensagem = entry1.get("1.0", tkinter.END).strip()
    pwk.sendwhatmsg(telefone,mensagem,datetime.now().hour, datetime.now().minute+2)
    time.sleep(60)
    keyboard.press_and_release('ctrl+w')

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = send_message,
    relief = "flat")

b0.place(
    x = 27, y = 350,
    width = 276,
    height = 53)

window.resizable(False, False)
window.mainloop()
