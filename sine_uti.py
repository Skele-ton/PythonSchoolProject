import sine_cosine_model
import numpy as np


def make_sine(name, layers, neurons, cycles, length):
    # Generate sine data
    x = np.linspace(0, length * np.pi, 100)
    y = np.sin(x)

    sine_model = sine_cosine_model.create_model(layers, neurons, name)
    sine_cosine_model.use_model(sine_model, x, y, cycles, name)