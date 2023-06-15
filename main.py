import AI_model
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os


# Delete all files from folder "plot_images"
def delete_files():
    folder_path = "plot_images/"
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)


# Run through all the images in "plot_images"
def play_video(plot_video, cycles):
    current_image_number = 0
    max_image_number = cycles - 1
    image_folder = "plot_images/"

    def update_image():
        nonlocal current_image_number
        if current_image_number <= max_image_number:
            image_path = f"{image_folder}plot_{current_image_number}.png"
            plot_image = tk.PhotoImage(file=image_path)
            plot_video.configure(image=plot_image)
            plot_video.image = plot_image
            current_image_number += 1
            root.after(100, update_image)  # Delay between image updates

    update_image()


# Destroy all widgets from previous screen
def destroy_prev_screen():
    for widget in root.winfo_children():
        widget.destroy()


# Starting screen
def home_screen():
    delete_files()
    destroy_prev_screen()

    sin_img = Image.open("images/sine_button_image.png")
    sin_img = sin_img.resize((320, 240))
    sin_btn_img = ImageTk.PhotoImage(sin_img)

    cos_img = Image.open("images/cosine_button_image.png")
    cos_img = cos_img.resize((320, 240))
    cos_btn_img = ImageTk.PhotoImage(cos_img)

    tan_img = Image.open("images/tangent_button_image.png")
    tan_img = tan_img.resize((320, 240))
    tan_btn_img = ImageTk.PhotoImage(tan_img)

    cot_img = Image.open("images/cotangent_button_image.png")
    cot_img = cot_img.resize((320, 240))
    cot_btn_img = ImageTk.PhotoImage(cot_img)

    title = ttk.Label(root, text="Choose a function", style="Heading.TLabel")
    button_frame = ttk.Frame(root)
    sin_button = ttk.Button(button_frame, text="Sine", image=sin_btn_img, compound="bottom",
                            command=lambda: selector_screen("sine"))
    sin_button.image = sin_btn_img

    cos_button = ttk.Button(button_frame, text="Cosine", image=cos_btn_img, compound="bottom",
                            command=lambda: selector_screen("cosine"))
    cos_button.image = cos_btn_img

    tan_button = ttk.Button(button_frame, text="Tangent", image=tan_btn_img, compound="bottom",
                            command=lambda: selector_screen("tangent"))
    tan_button.image = tan_btn_img

    cot_button = ttk.Button(button_frame, text="Cotangent", image=cot_btn_img, compound="bottom",
                            command=lambda: selector_screen("cotangent"))
    cot_button.image = cot_btn_img

    exit_button = ttk.Button(button_frame, text="Exit", command=lambda: [delete_files(), root.destroy()])

    # Layout
    title.pack()
    button_frame.pack()
    sin_button.grid(row=1, column=0, padx=10, pady=10)
    cos_button.grid(row=1, column=1, padx=10, pady=10)
    tan_button.grid(row=2, column=0, padx=10, pady=10)
    cot_button.grid(row=2, column=1, padx=10, pady=10)
    exit_button.grid(row=3, columnspan=2, padx=10, pady=10, sticky="e")


# Model attribute selector screen
def selector_screen(function_name):
    destroy_prev_screen()

    var_file_name = f"parameters/{function_name}_params.txt"
    default_layers = ""
    default_neurons = ""
    default_cycles = ""
    default_length = ""
    video_check = 0

    if os.path.exists(var_file_name):
        with open(var_file_name, "r") as file:
            lines = file.readlines()
            if len(lines) == 4:
                default_layers = lines[0].split(":")[1].strip()
                default_neurons = lines[1].split(":")[1].strip()
                default_cycles = lines[2].split(":")[1].strip()
                default_length = lines[3].split(":")[1].strip()

    attributes_label = ttk.Label(root, text=f"{function_name.capitalize()} Attributes", style="Heading.TLabel")
    selector_frame = ttk.Frame(root)
    select_button_frame = ttk.Frame(root)

    layers_label = ttk.Label(selector_frame, text="Hidden Layers:")
    layers_entry = ttk.Entry(selector_frame, font=(None, 20), width=15)
    layers_entry.insert(tk.END, default_layers)
    layers_err = ttk.Label(selector_frame, text="", style="Red.TLabel")

    neurons_label = ttk.Label(selector_frame, text="Neurons per Layer:")
    neurons_entry = ttk.Entry(selector_frame, font=(None, 20), width=15)
    neurons_entry.insert(tk.END, default_neurons)
    neurons_err = ttk.Label(selector_frame, text="", style="Red.TLabel")

    cycles_label = ttk.Label(selector_frame, text="Training Cycles:")
    cycles_entry = ttk.Entry(selector_frame, font=(None, 20), width=15)
    cycles_entry.insert(tk.END, default_cycles)
    cycles_err = ttk.Label(selector_frame, text="", style="Red.TLabel")

    length_label = ttk.Label(selector_frame, text="Data Length x π:")
    length_entry = ttk.Entry(selector_frame, font=(None, 20), width=15)
    length_entry.insert(tk.END, default_length)
    length_err = ttk.Label(selector_frame, text="", style="Red.TLabel")

    # Check if the data in the entries is valid
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
            cycles_err_text = "Whole Number Between 5 and 500\nThe More Cycles, The Longer Training Takes!"
        if not length.isdigit() or not 1 <= int(length) <= 5:
            length_err_text = "Whole Number Between 1 and 5\nThe Longer Data, The Longer Training Takes!"

        layers_err.config(text=layers_err_text)
        neurons_err.config(text=neurons_err_text)
        cycles_err.config(text=cycles_err_text)
        length_err.config(text=length_err_text)

        if not layers_err_text and not neurons_err_text and not cycles_err_text and not length_err_text:
            with open(var_file_name, "w") as file:
                file.write(f"Layers:{layers}\n")
                file.write(f"Neurons:{neurons}\n")
                file.write(f"Cycles:{cycles}\n")
                file.write(f"Length:{length}\n")

            during_training_screen(function_name, int(layers), int(neurons), int(cycles), int(length), video_check)

    def train_with_video():
        nonlocal video_check
        video_check = 1
        entry_error_check()

    train_button = ttk.Button(select_button_frame, text="Train", command=entry_error_check)
    train_with_video_button = ttk.Button(select_button_frame, text="Train & Save Video", command=train_with_video)
    home_button = ttk.Button(select_button_frame, text="Home", command=home_screen)

    # Layout
    attributes_label.grid(row=0, column=0, padx=10, pady=10, sticky="")
    selector_frame.grid(row=1, column=0, padx=10, pady=10, sticky="we")
    select_button_frame.grid(row=2, column=0, padx=10, pady=20, sticky="we")

    root.grid_columnconfigure(0, weight=1)

    layers_label.grid(row=0, columnspan=2, padx=10, pady=10, sticky="w")
    layers_entry.grid(row=0, column=2, padx=10, pady=10, sticky="e")
    layers_err.grid(row=1, columnspan=2, padx=10, pady=10, sticky="w")

    neurons_label.grid(row=2, columnspan=2, padx=10, pady=10, sticky="w")
    neurons_entry.grid(row=2, column=2, padx=10, pady=10, sticky="e")
    neurons_err.grid(row=3, columnspan=2, padx=10, pady=10, sticky="w")

    cycles_label.grid(row=4, columnspan=2, padx=10, pady=10, sticky="w")
    cycles_entry.grid(row=4, column=2, padx=10, pady=10, sticky="e")
    cycles_err.grid(row=5, columnspan=2, padx=10, pady=10, sticky="w")

    length_label.grid(row=6, columnspan=2, padx=10, pady=10, sticky="w")
    length_entry.grid(row=6, column=2, padx=10, pady=10, sticky="e")
    length_err.grid(row=7, columnspan=2, padx=10, pady=10, sticky="w")

    train_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    train_with_video_button.grid(row=0, column=1, padx=10, pady=10, sticky="we")
    home_button.grid(row=0, column=2, padx=10, pady=10)

    # Center labels and entries
    selector_frame.grid_columnconfigure((0, 1, 2), weight=1)

    # Center buttons
    select_button_frame.grid_columnconfigure((0, 1, 2), weight=1)


# Screen during training the model
def during_training_screen(function_name, layers, neurons, cycles, length, video_check):
    destroy_prev_screen()

    training_frame = ttk.Frame(root)
    training_text = ttk.Label(training_frame, text="Training Model...", style="Heading.TLabel")
    progress_text = ttk.Label(training_frame, text=f"0 / {cycles} Cycles", style="Heading.TLabel")

    training_frame.pack(anchor="center", expand=True)
    training_text.grid(row=0, column=0, padx=10, pady=10)
    progress_text.grid(row=1, column=0, padx=10, pady=10)
    root.update()

    model = AI_model.create_model(function_name, layers, neurons)
    x, y = AI_model.create_data(function_name, length)

    def update_label_text(text):
        progress_text.configure(text=text)
        root.update()

    final_loss = AI_model.use_model(model, x, y, cycles, function_name, update_label_text, video_check)
    after_training_screen(cycles, final_loss)


# Screen after training the model
def after_training_screen(cycles, final_loss):
    destroy_prev_screen()

    end_frame = tk.Frame(root)

    play_video_button = ttk.Button(end_frame, text="Play Video",
                                   command=lambda: play_video(plot_video, cycles))

    plot_image = tk.PhotoImage(file=f"plot_images/plot_{cycles - 1}.png")
    plot_video = tk.Label(end_frame, image=plot_image)
    plot_video.image = plot_image

    loss_label = ttk.Label(end_frame, text=f"Final Loss: {final_loss}", style="Heading.TLabel")

    exit_button = ttk.Button(end_frame, text="Exit", command=lambda: [delete_files(), root.destroy()])
    home_button = ttk.Button(end_frame, text="Home", command=home_screen)

    # Layout
    end_frame.pack()
    play_video_button.grid(row=0, columnspan=2, padx=10, pady=10)
    plot_video.grid(row=1, columnspan=2, padx=10, pady=10)
    loss_label.grid(row=2, columnspan=2, padx=10, pady=15)
    home_button.grid(row=3, column=0, padx=10, pady=10)
    exit_button.grid(row=3, column=1, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: [delete_files(), root.destroy()])
    root.title("AI Trigonometry Functions Showcase")

    width = 800
    height = 750
    screen_width = root.winfo_screenwidth()  # Width of the screen
    screen_height = root.winfo_screenheight()  # Height of the screen
    coord_x = (screen_width / 2) - (width / 2)
    coord_y = (screen_height / 2) - (height / 2)

    root.geometry(f"{width}x{height}+{int(coord_x)}+{int(coord_y)}")

    # Create styles
    style = ttk.Style(root)
    style.configure(".", font=("Calibri", 20))
    style.configure("Heading.TLabel", font=(None, 35, "bold"))
    style.configure("Red.TLabel", foreground="red")

    home_screen()

    root.resizable(False, False)  # Make window unresizable
    root.mainloop()
