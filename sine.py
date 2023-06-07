import video_maker

import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras

# Constants
CYCLES = 20
FPS = 10
VIDEO_NAME = "sine_function_video.mp4"
WINDOW_SIZE = (640, 480)  # Width, height


frame_writer = video_maker.create_video_formatter(VIDEO_NAME, FPS, WINDOW_SIZE)

# Generate sine data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Define the model architecture
model = keras.Sequential([
    keras.layers.Dense(20, activation='sigmoid', input_shape=(1,)),
    keras.layers.Dense(20, activation='sigmoid'),
    keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
for cycle in range(CYCLES):
    model.fit(x, y, epochs=100, verbose=1)
    y_pred = model.predict(x)

    plt.plot(x, y, label='Original')
    plt.plot(x, y_pred, label='Predicted')
    plt.title('Sine Wave Prediction')
    plt.legend()

    # Save the current plot as an image file
    plt.savefig("sine_plot.png")
    plt.clf()

    video_maker.add_frame(frame_writer)

# model.save('sine_model.h5')

video_maker.release_video(frame_writer)
