import video_maker
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras


# Create initial model
def create_model(function_name, layers, neurons):
    # Define the model architecture
    model = keras.Sequential([
        keras.layers.Dense(neurons, activation="sigmoid", input_shape=(1,)),
    ])

    for _ in range(layers - 1):
        model.add(keras.layers.Dense(neurons, activation="sigmoid"))

    model.add(keras.layers.Dense(1))
    model.save(f"models/{function_name}_model.h5")

    model.compile(optimizer="adam", loss="mean_squared_error")

    return model


# Create train/test data for the model
def create_data(function_name, length):
    # Generate sine data
    if function_name == "sine":
        x = np.linspace(0, length * np.pi, length * 100)
        y = np.sin(x)

    elif function_name == "cosine":
        x = np.linspace(0, length * np.pi, length * 100)
        y = np.cos(x)

    elif function_name == "tangent":
        x = np.linspace(-2 * np.pi, 2 * np.pi, length * 250)
        y = np.tan(x)

    elif function_name == "cotangent":
        x = np.linspace(-2 * np.pi, 2 * np.pi, length * 250)
        y = 1 / np.tan(x)

    return x, y


# Train the model. Return a video if desired
def use_model(model, x, y, cycles, function_name, update_label_text, video_check):
    if video_check == 1:
        frame_writer = video_maker.create_video_formatter(function_name)

    # Train the model
    for cycle in range(cycles):
        model.fit(x, y, epochs=100, verbose=1)
        y_pred = model.predict(x)

        fig, ax = plt.subplots()
        ax.plot(x, y, label="Original")
        ax.plot(x, y_pred, label="Predicted")
        ax.set_title(f"{function_name.capitalize()} Wave Prediction")
        ax.legend()

        if function_name == "sine" or function_name == "cosine":
            ax.set_ylim(-1.2, 1.2)

        elif function_name == "tangent" or function_name == "cotangent":
            ax.set_ylim(-5, 5)

        # Save the current plot as an image file
        fig.savefig(f"plot_images/plot_{str(cycle)}.png")
        plt.close(fig)

        if video_check == 1:
            video_maker.add_frame(frame_writer, cycle)

        update_label_text(f"{cycle + 1} / {cycles} Cycles")

    if video_check == 1:
        video_maker.release_video(frame_writer)

    history = model.fit(x, y, epochs=100, verbose=1)
    final_loss = history.history["loss"][-1]
    return str(final_loss)[:7]
