import AI_model
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os


def delete_files():
    folder_path = "plot_images/"
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)


def destroy_prev_screen():
    for widget in root.winfo_children():
        widget.destroy()
    root.update()


def home_screen():
    delete_files()
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

    end_button = ttk.Button(root, text="Exit", padding=(10, 5, 10, 5), command=lambda: [delete_files(), root.destroy()])

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

    var_file_name = f"variables/{function_name}_vars.txt"
    default_layers = ""
    default_neurons = ""
    default_cycles = ""
    default_length = ""
    video_check = 0

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
            layers_err_text = "Whole Number Between 2 and 20!"
        if not neurons.isdigit() or not 10 <= int(neurons) <= 100:
            neurons_err_text = "Whole Number Between 10 and 100!"
        if not cycles.isdigit() or not 5 <= int(cycles) <= 500:
            cycles_err_text = "Whole Number Between 5 and 500\n(The More Cycles, The Longer Training Takes!)"
        if not length.isdigit() or not 1 <= int(length) <= 5:
            length_err_text = "Whole Number Between 1 and 5 (2 is Recommended)"

        layers_err.config(text=layers_err_text)
        neurons_err.config(text=neurons_err_text)
        cycles_err.config(text=cycles_err_text)
        length_err.config(text=length_err_text)

        if not layers_err_text and not neurons_err_text and not cycles_err_text and not length_err_text:
            with open(var_file_name, 'w') as file:
                file.write(f"{layers}\n")
                file.write(f"{neurons}\n")
                file.write(f"{cycles}\n")
                file.write(f"{length}\n")

            during_function_screen(function_name, int(layers), int(neurons), int(cycles), int(length), video_check)

    def start_with_video():
        nonlocal video_check
        video_check = 1
        entry_error_check()

    start_button = ttk.Button(root, text="Start", padding=(10, 5, 10, 5), command=entry_error_check)
    start_with_video_button = ttk.Button(root, text="Start And Make Video", padding=(10, 5, 10, 5), command=start_with_video)
    home_button = ttk.Button(root, text="Home", padding=(10, 5, 10, 5), command=home_screen)

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

    start_button.grid(row=8, column=0, padx=10, pady=10)
    start_with_video_button.grid(row=8, column=1, padx=10, pady=10)
    home_button.grid(row=8, column=3, padx=10, pady=10)


def during_function_screen(function_name, layers, neurons, cycles, length, video_check):
    destroy_prev_screen()

    print(video_check)

    training_text = ttk.Label(root, text="Training Model...", padding=(10, 5, 10, 5))
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

    final_loss = AI_model.use_model(model, x, y, cycles, function_name, update_label_text, video_check)
    print(final_loss)
    after_function_screen(function_name, cycles)


def play_video(plot_video, cycles):
    current_image_number = 0  # Starting image number
    max_image_number = cycles - 1  # Maximum image number
    image_folder = "plot_images/"  # Folder containing the images

    def update_image():
        nonlocal current_image_number
        if current_image_number <= max_image_number:
            image_path = f"{image_folder}plot_{current_image_number}.png"
            plot_image = tk.PhotoImage(file=image_path)
            plot_video.configure(image=plot_image)
            plot_video.image = plot_image
            current_image_number += 1
            root.after(100, update_image)  # Delay between image updates in milliseconds

    update_image()


def after_function_screen(function_name, cycles):
    destroy_prev_screen()

    end_button = ttk.Button(root, text="Exit", padding=(10, 5, 10, 5),
                            command=lambda: [delete_files(), root.destroy()])
    home_button = ttk.Button(root, text="Home", padding=(10, 5, 10, 5), command=home_screen)
    play_video_button = ttk.Button(root, text="Play Video", padding=(10, 5, 10, 5),
                                   command=lambda: play_video(plot_video, cycles))

    plot_image = tk.PhotoImage(file=f"plot_images/plot_{cycles - 1}.png")
    plot_video = tk.Label(root, image=plot_image)
    plot_video.image = plot_image

    end_button.grid(row=0, column=0)
    play_video_button.grid(row=0, column=1)
    home_button.grid(row=0, column=2)
    plot_video.grid(row=1, columnspan=3)


if __name__ == "__main__":
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: [delete_files(), root.destroy()])
    root.title("AI Trigonometry Functions Showcase")
    root.geometry("800x600")

    style = ttk.Style(root)
    style.configure('.', font=('Calibri', 20))
    style.configure("Custom.TLabel", foreground="red")

    home_screen()

    root.eval('tk::PlaceWindow . center')
    # root.resizable(False, False)
    root.mainloop()
