import AI_model
import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk
import os
import cv2


def destroy_prev_screen():
    for widget in root.winfo_children():
        widget.destroy()
    root.update()


def release_destroy_return(cap):
    cap.release()
    home_screen()


def release_delete(cap):
    cap.release()
    root.destroy()
    root.quit()


def home_screen():
    destroy_prev_screen()

    sin_img = Image.open("images/sine_tkinter.png")
    sin_img = sin_img.resize((320, 240))
    sin_btn_img = ImageTk.PhotoImage(sin_img)

    cos_img = Image.open("images/cosine_tkinter.png")
    cos_img = cos_img.resize((320, 240))
    cos_btn_img = ImageTk.PhotoImage(cos_img)

    title = ttk.Label(root, text="Choose a function")
    button_grid = ttk.Frame(root)
    sin_button = ttk.Button(button_grid, text="Sine", image=sin_btn_img, compound="bottom", padding=(10, 5, 10, 5),
                            command=lambda: selector_screen("sine"))
    sin_button.image = sin_btn_img

    cos_button = ttk.Button(button_grid, text="Cosine", image=cos_btn_img, compound="bottom", padding=(10, 5, 10, 5),
                            command=lambda: selector_screen("cosine"))
    cos_button.image = cos_btn_img

    tan_button = ttk.Button(button_grid, text="Tangent", padding=(10, 5, 10, 5),
                            command=lambda: selector_screen("tangent"))

    cot_button = ttk.Button(button_grid, text="Cotangent", padding=(10, 5, 10, 5),
                            command=lambda: selector_screen("cotangent"))

    end_button = ttk.Button(root, text="Exit", padding=(10, 5, 10, 5), command=root.destroy)

    # Layout
    title.pack()
    button_grid.pack()
    sin_button.grid(row=1, column=0, padx=10, pady=10)
    cos_button.grid(row=1, column=1, padx=10, pady=10)
    tan_button.grid(row=2, column=0, padx=10, pady=10)
    cot_button.grid(row=2, column=1, padx=10, pady=10)
    end_button.pack()


def selector_screen(function_name):
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
    layers_label = ttk.Label(root, text="Hidden Layers:", compound="left", padding=(10, 5, 10, 5))
    layers_entry = tk.Entry(root)
    layers_entry.insert(tk.END, default_layers)
    layers_err = ttk.Label(root, text="", style="Custom.TLabel")

    neurons_label = ttk.Label(root, text="Neurons per Layer:", padding=(10, 5, 10, 5))
    neurons_entry = tk.Entry(root)
    neurons_entry.insert(tk.END, default_neurons)
    neurons_err = ttk.Label(root, text="", style="Custom.TLabel")

    cycles_label = ttk.Label(root, text="Training Cycles:", padding=(10, 5, 10, 5))
    cycles_entry = tk.Entry(root)
    cycles_entry.insert(tk.END, default_cycles)
    cycles_err = ttk.Label(root, text="", style="Custom.TLabel")

    length_label = ttk.Label(root, text="Data Length x π:", padding=(10, 5, 10, 5))
    length_entry = tk.Entry(root)
    length_entry.insert(tk.END, default_length)
    length_err = ttk.Label(root, text="", style="Custom.TLabel")

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
            var_file_name = "variables/" + function_name + "_vars.txt"
            with open(var_file_name, 'w') as file:
                file.write(f'{layers}\n')
                file.write(f'{neurons}\n')
                file.write(f'{cycles}\n')
                file.write(f'{length}\n')

            during_function_screen(function_name, int(layers), int(neurons), int(cycles), int(length))

    start_button = ttk.Button(root, text="Start", command=entry_error_check, padding=(10, 5, 10, 5))
    home_button = ttk.Button(root, text="Home", command=home_screen, padding=(10, 5, 10, 5))

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


def during_function_screen(function_name, layers, neurons, cycles, length):
    destroy_prev_screen()

    training_text = ttk.Label(root, text="Training Model", padding=(10, 5, 10, 5))
    progress_text = ttk.Label(root, text=f"0 / {cycles} Cycles", padding=(10, 5, 10, 5))
    training_text.pack()
    progress_text.pack()
    root.update()

    model = AI_model.create_model(function_name, layers, neurons)
    x, y = AI_model.create_data(function_name, length)
    print(f"model: {model} \nx: {x} \ny: {y}")

    def update_label_text(text):
        progress_text.configure(text=text)
        root.update()

    final_loss = AI_model.use_model(model, x, y, cycles, function_name, update_label_text)
    print(final_loss)
    # after_function_screen("videos/sine_function_video.mp4")


def after_function_screen(video_name):
    destroy_prev_screen()

    end_button = ttk.Button(root, text="Exit", padding=(10, 5, 10, 5), command=lambda: release_delete(cap))
    home_button = ttk.Button(root, text="Home", padding=(10, 5, 10, 5), command=lambda: release_destroy_return(cap))

    end_button.grid(row=0, column=0, sticky="nw")
    home_button.grid(row=0, column=1, sticky="ne")

    cap = cv2.VideoCapture(video_name)

    # Get the video dimensions :)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a canvas to display the video frames
    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.grid(row=1, columnspan=2, padx=10, pady=10)

    while True:
        while cap.isOpened():
            ret, frame = cap.read()

            if ret:
                # Convert the frame to RGB format
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Create an image from the frame
                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image)

                # Update the canvas with the new image
                canvas.create_image(0, 0, image=photo, anchor=tk.NW)

                time.sleep(0.1)
                root.update()
            else:
                break

        time.sleep(2)

        # Reset the video to the beginning
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("AI Trigonometry Functions Showcase")
    root.geometry("800x600")

    style = ttk.Style(root)
    style.configure('.', font=('Calibri', 20))
    style.configure("Custom.TLabel", foreground="red")

    home_screen()

    root.eval('tk::PlaceWindow . center')
    # root.resizable(False, False)
    root.mainloop()
