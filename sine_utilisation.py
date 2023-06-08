import sine_cosine_model
import numpy as np

# Constants
FILE_NAME = "sine"

NEURONS_PER_LAYER = 20
TRAINING_CYCLES = 5
DATA_LENGTH = 2
FPS = 10


# Generate sine data
x = np.linspace(0, DATA_LENGTH * np.pi, 100)
y = np.sin(x)

sine_model = sine_cosine_model.create_model(NEURONS_PER_LAYER)
sine_cosine_model.use_model(sine_model, x, y, TRAINING_CYCLES, FILE_NAME, FPS)
