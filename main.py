import tkinter as tk
# import subprocess


def destroy_prev_screen():
    for widget in root.winfo_children():
        widget.destroy()


def create_home_screen():
    destroy_prev_screen()

    title = tk.Label(root, text="Choose a function")
    button_grid = tk.Frame(root)
    sin_button = tk.Button(button_grid, text="Sine", height=15, width=30, command=lambda: create_pre_start_screen("sine"))
    cos_button = tk.Button(button_grid, text="Cosine", height=15, width=30, command=lambda: create_pre_start_screen("cosine"))
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

    # Sine Options And Buttons
    neurons_label = tk.Label(root, text="Neurons per Layer:")
    neurons_entry = tk.Entry(root)

    cycles_label = tk.Label(root, text="Training Cycles:")
    cycles_entry = tk.Entry(root)

    length_label = tk.Label(root, text="Data Length x π:")
    length_entry = tk.Entry(root)

    fps_label = tk.Label(root, text="Video Frames per Second:")
    fps_entry = tk.Entry(root)

    start_button = tk.Button(root, text="Start", command=lambda: start_function(
        function_name,
        int(neurons_entry.get()),
        int(cycles_entry.get()),
        int(length_entry.get()),
        int(fps_entry.get())
    ))
    home_button = tk.Button(root, text="Home", command=create_home_screen)

    # Layout
    neurons_label.grid(row=0, column=0, padx=10, pady=10)
    neurons_entry.grid(row=0, column=1, padx=10, pady=10)

    cycles_label.grid(row=1, column=0, padx=10, pady=10)
    cycles_entry.grid(row=1, column=1, padx=10, pady=10)

    length_label.grid(row=2, column=0, padx=10, pady=10)
    length_entry.grid(row=2, column=1, padx=10, pady=10)

    fps_label.grid(row=3, column=0, padx=10, pady=10)
    fps_entry.grid(row=3, column=1, padx=10, pady=10)

    start_button.grid(row=4, columnspan=2, padx=10, pady=10)
    home_button.grid(row=4, column=3, padx=10, pady=10)


def start_function(name, neurons, cycles, length, fps):
    with open("variables/" + name + "_vars.txt", 'w') as file:
        file.write(f'{neurons}\n')
        file.write(f'{cycles}\n')
        file.write(f'{length}\n')
        file.write(f'{fps}\n')


root = tk.Tk()
root.title("AI Trigonometry Functions Showcase")
root.geometry("600x600")

create_home_screen()

root.eval('tk::PlaceWindow . center')
root.resizable(False, False)
root.mainloop()
