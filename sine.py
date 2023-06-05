import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Define the model architecture
model = keras.Sequential([
    keras.layers.Dense(20, activation='sigmoid', input_shape=(1,)),
    keras.layers.Dense(20, activation='sigmoid'),
    keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
for epoch in range(0, 10):
    model.fit(x, y, epochs=100, verbose=1)  
    y_pred = model.predict(x)

    plt.plot(x, y, label='Original')
    plt.plot(x, y_pred, label='Predicted')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sine Wave Prediction')
    plt.legend()
    plt.savefig("graphs/plot_" + "{:04d}".format(epoch) + ".png")
    plt.clf()

model.save('sine_model.h5')
