import sine_uti
import cosine_uti

import tkinter as tk
from PIL import Image, ImageTk
import os
# import subprocess


def destroy_prev_screen():
    for widget in root.winfo_children():
        widget.destroy()


def create_home_screen():
    destroy_prev_screen()

    sin_img = Image.open("images/sine_tkinter.png")
    sin_img = sin_img.resize((320, 240))
    sin_btn_img = ImageTk.PhotoImage(sin_img)

    cos_img = Image.open("images/cosine_tkinter.png")
    cos_img = cos_img.resize((320, 240))
    cos_btn_img = ImageTk.PhotoImage(cos_img)

    title = tk.Label(root, text="Choose a function")
    button_grid = tk.Frame(root)
    sin_button = tk.Button(button_grid, text="Sine", image=sin_btn_img, compound="bottom",
                           command=lambda: create_pre_start_screen("sine"))
    sin_button.image = sin_btn_img
    cos_button = tk.Button(button_grid, text="Cosine", image=cos_btn_img, compound="bottom",
                           command=lambda: create_pre_start_screen("cosine"))
    cos_button.image = cos_btn_img
    tan_button = tk.Button(button_grid, text="Tangent", height=15, width=30, command=lambda: create_pre_start_screen("tan"))
    cot_button = tk.Button(button_grid, text="Cotangent", height=15, width=30, command=lambda: create_pre_start_screen("cotan"))
    end_button = tk.Button(root, text="Exit", command=root.destroy)

    # Layout
    title.pack()
    button_grid.pack()
    sin_button.grid(row=1, column=0, padx=10, pady=10)
    cos_button.grid(row=1, column=1, padx=10, pady=10)
    tan_button.grid(row=2, column=0, padx=10, pady=10)
    cot_button.grid(row=2, column=1, padx=10, pady=10)
    end_button.pack()


def create_pre_start_screen(function_name):
    destroy_prev_screen()

    var_file_name = "variables/" + function_name + "_vars.txt"
    default_layers = ""
    default_neurons = ""
    default_cycles = ""
    default_length = ""

    if os.path.exists(var_file_name):
        with open(var_file_name, 'r') as file:
            lines = file.readlines()
            if len(lines) == 4:
                default_layers = lines[0].strip()
                default_neurons = lines[1].strip()
                default_cycles = lines[2].strip()
                default_length = lines[3].strip()

    # Function Variables And Buttons
    layers_label = tk.Label(root, text="Model Layers:", justify="left")
    layers_entry = tk.Entry(root)
    layers_entry.insert(tk.END, default_layers)
    layers_err = tk.Label(root, text="", fg="red")

    neurons_label = tk.Label(root, text="Neurons per Layer:")
    neurons_entry = tk.Entry(root)
    neurons_entry.insert(tk.END, default_neurons)
    neurons_err = tk.Label(root, text="", fg="red")

    cycles_label = tk.Label(root, text="Training Cycles:")
    cycles_entry = tk.Entry(root)
    cycles_entry.insert(tk.END, default_cycles)
    cycles_err = tk.Label(root, text="", fg="red")

    length_label = tk.Label(root, text="Data Length x π:")
    length_entry = tk.Entry(root)
    length_entry.insert(tk.END, default_length)
    length_err = tk.Label(root, text="", fg="red")

    def entry_error_check():
        layers = layers_entry.get()
        neurons = neurons_entry.get()
        cycles = cycles_entry.get()
        length = length_entry.get()

        layers_err_text = ""
        neurons_err_text = ""
        cycles_err_text = ""
        length_err_text = ""

        if not layers.isdigit() or not 2 <= int(layers) <= 20:
            layers_err_text = "Must be a Number Between 2 and 20!"
        if not neurons.isdigit() or not 10 <= int(neurons) <= 100:
            neurons_err_text = "Must be Number Between 10 and 100!"
        if not cycles.isdigit() or not 5 <= int(cycles) <= 500:
            cycles_err_text = "Must be a Number Between 5 and 500\n(The More Cycles, The Longer Training Takes)!"
        if not length.isdigit() or not 1 <= int(length) <= 5:
            length_err_text = "Must be a Number Between 1 and 5 (2 is Recommended)"

        layers_err.config(text=layers_err_text)
        neurons_err.config(text=neurons_err_text)
        cycles_err.config(text=cycles_err_text)
        length_err.config(text=length_err_text)

        if not layers_err_text and not neurons_err_text and not cycles_err_text and not length_err_text:
            start_function(function_name, int(layers), int(neurons), int(cycles), int(length))

    start_button = tk.Button(root, text="Start", command=entry_error_check)
    home_button = tk.Button(root, text="Home", command=create_home_screen)

    # Layout
    layers_label.grid(row=0, column=0, padx=10, pady=10)
    layers_entry.grid(row=0, column=1, padx=10, pady=10)
    layers_err.grid(row=1, column=0, padx=10, pady=10)

    neurons_label.grid(row=2, column=0, padx=10, pady=10)
    neurons_entry.grid(row=2, column=1, padx=10, pady=10)
    neurons_err.grid(row=3, column=0, padx=10, pady=10)

    cycles_label.grid(row=4, column=0, padx=10, pady=10)
    cycles_entry.grid(row=4, column=1, padx=10, pady=10)
    cycles_err.grid(row=5, column=0, padx=10, pady=10)

    length_label.grid(row=6, column=0, padx=10, pady=10)
    length_entry.grid(row=6, column=1, padx=10, pady=10)
    length_err.grid(row=7, column=0, padx=10, pady=10)

    start_button.grid(row=8, columnspan=2, padx=10, pady=10)
    home_button.grid(row=8, column=3, padx=10, pady=10)


def start_function(name, layers, neurons, cycles, length):
    print("passed")

    with open("variables/" + name + "_vars.txt", 'w') as file:
        file.write(f'{layers}\n')
        file.write(f'{neurons}\n')
        file.write(f'{cycles}\n')
        file.write(f'{length}\n')

    if name == "sine":
        sine_uti.make_sine(name, layers, neurons, cycles, length)

    if name == "cosine":
        cosine_uti.make_cosine(name, layers, neurons, cycles, length)


root = tk.Tk()
root.title("AI Trigonometry Functions Showcase")
root.geometry("800x600")

create_home_screen()

root.eval('tk::PlaceWindow . center')
# root.resizable(False, False)
root.mainloop()
