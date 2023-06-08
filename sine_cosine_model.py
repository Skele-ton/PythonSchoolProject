import video_maker
import matplotlib.pyplot as plt
from tensorflow import keras


def create_model(layers, neurons, name):
    # Define the model architecture
    model = keras.Sequential([
        keras.layers.Dense(neurons, activation='sigmoid', input_shape=(1,)),
    ])

    for layer in range(layers - 1):
        model.add(keras.layers.Dense(neurons, activation='sigmoid'))

    model.add(keras.layers.Dense(1))
    model.save(name + "_model.h5")

    model.compile(optimizer='adam', loss='mean_squared_error')

    return model


def use_model(model, x, y, cycles, file_name):
    frame_writer = video_maker.create_video_formatter(file_name)

    # Train the model
    for cycle in range(cycles):
        model.fit(x, y, epochs=100, verbose=1)
        y_pred = model.predict(x)

        plt.plot(x, y, label='Original')
        plt.plot(x, y_pred, label='Predicted')
        plt.title(file_name.capitalize() + ' Wave Prediction')
        plt.legend()

        # Save the current plot as an image file
        plt.savefig(file_name + "_plot.png")
        plt.clf()

        video_maker.add_frame(frame_writer, file_name)

    video_maker.release_video(frame_writer)
    print("All done!")
    return
