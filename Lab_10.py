import serial
import time
import tkinter as tk

# Configuración del puerto serial
arduino = serial.Serial('COM3', 9600)  # Cambia 'COM3' por el puerto adecuado en tu sistema

def send_command(command):
    arduino.write(command.encode())

def read_from_arduino():
    while arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        print(line)
        if line == "ButtonD Pressed":
            print("Arduino: ButtonD was pressed on Arduino")
        elif line == "ButtonI Pressed":
            print("Arduino: ButtonI was pressed on Arduino")

def button_d_pressed():
    send_command('D')
    print("Python: ButtonD pressed in Python")

def button_i_pressed():
    send_command('I')
    print("Python: ButtonI pressed in Python")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Control de Motor")

buttonD = tk.Button(root, text="ButtonD", command=button_d_pressed)
buttonD.pack(pady=10)

buttonI = tk.Button(root, text="ButtonI", command=button_i_pressed)
buttonI.pack(pady=10)

def check_arduino():
    read_from_arduino()
    root.after(100, check_arduino)

root.after(100, check_arduino)
root.mainloop()

# Cierra el puerto serial al terminar
arduino.close()
