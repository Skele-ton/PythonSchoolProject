import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from video_maker import make_video

# Constants
NUMBER_OF_EPOCHS = 10
FPS = 10
OUTPUT_VIDEO = "sine_function_video.mp4"
FRAME_SIZE = (640, 480)  # Width, height

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
for epoch in range(NUMBER_OF_EPOCHS):
    model.fit(x, y, epochs=100, verbose=1)
    y_pred = model.predict(x)

    plt.plot(x, y, label='Original')
    plt.plot(x, y_pred, label='Predicted')
    plt.title('Sine Wave Prediction')
    plt.legend()

    # Save the current plot as an image file
    plt.savefig(f"plot_{epoch:04d}.png")
    plt.clf()

model.save('sine_model.h5')

make_video(FPS, OUTPUT_VIDEO, FRAME_SIZE, NUMBER_OF_EPOCHS)

# # Create the video
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec
# video_writer = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, FPS, FRAME_SIZE)

# # Write each frame to the video
# for epoch in range(NUMBER_OF_EPOCHS):
#     # Read the frame image
#     frame_path = f"plot_{epoch:04d}.png"
#     frame = cv2.imread(frame_path)

#     # Write the frame to the video
#     video_writer.write(frame)

#     # Remove the frame image file
#     os.remove(frame_path)

# # Release the VideoWriter and close the video file
# video_writer.release()
