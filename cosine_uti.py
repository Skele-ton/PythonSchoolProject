import sine_cosine_model
import numpy as np


def make_cosine(name, layers, neurons, cycles, length):
    # Generate sine data
    x = np.linspace(0, length * np.pi, 100)
    y = np.cos(x)

    cosine_model = sine_cosine_model.create_model(neurons)
    sine_cosine_model.use_model(cosine_model, x, y, cycles, name)
