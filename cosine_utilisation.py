import sine_cosine_model
import numpy as np

# Constants
FILE_NAME = "cosine"

DATA_LENGTH = 2
NEURONS_PER_LAYER = 20
TRAINING_CYCLES = 30
FPS = 10
WINDOW_SIZE = (640, 480)  # Width, height


# Generate sine data
x = np.linspace(0, DATA_LENGTH * np.pi, 100)
y = np.cos(x)

cosine_model = sine_cosine_model.create_model(NEURONS_PER_LAYER)
sine_cosine_model.use_model(cosine_model, x, y, TRAINING_CYCLES, FILE_NAME, FPS, WINDOW_SIZE)
