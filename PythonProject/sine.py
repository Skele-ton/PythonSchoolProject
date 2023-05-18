import numpy as np
import math
import argparse
import matplotlib.pyplot as plt
from keras import models
from keras.layers.core import Dense
from keras.layers.recurrent import LSTM
from keras.callbacks import TensorBoard
from keras.optimizers import adam
from shutil import copyfile


INPUTS = 40


def getSineData(a, count):
    return np.array([math.sin(a * i) for i in range(0, count)])


def getXY(data, total):
    x = data[0: total - INPUTS].reshape((total - INPUTS, 1))
    for i in range(1, INPUTS):
        x = np.concatenate((x, data[i: total - INPUTS + i].reshape((total - INPUTS, 1))), axis=1)

    y = data[INPUTS: total]
    return x, y


def loadAI(model):
    try:
        model.load_weights("model.h5")
        print("model loaded")
    except OSError:
        print("Model not found")


def saveAI(model):
    print("Saving model")
    try:
        copyfile('model.h5', 'model.h5.saved')
    except FileNotFoundError:
        print("didn't find model files to save")

    model.save_weights("model.h5", overwrite=True)


def getSeries(a, trainCount, testCount=0):
    data = getSineData(a, trainCount+testCount)
    x, y = getXY(data, trainCount)
    if testCount > INPUTS:
        evalX, evalY = getXY(data[trainCount:], testCount)
    else:
        evalX, evalY = None, None
    return x, y, evalX, evalY


def buildLSTMModel():
    model = models.Sequential()
    model.add(LSTM(100, batch_input_shape=(1, 1, 1), return_sequences=True, stateful=True))
    model.add(LSTM(100, return_sequences=False, stateful=True))
    model.add(Dense(1))
    model.compile(loss='mse', optimizer=adam(lr=0.0001))

    board = TensorBoard(log_dir='model', histogram_freq=1, write_graph=True, write_images=False)
    board.set_model(model)
    return model, board


def testLSTM():
    model, board = buildLSTMModel()

    total = 3300
    trainSize = 3000

    loadAI(model)

    for epoch in range(0, 10):
        for i in range(0, 10):
            data = getSineData(0.06 + i * 0.006, total)
            x = data[0:trainSize].reshape((trainSize, 1, 1))
            y = data[1:trainSize+1]
            evalX = data[trainSize:total-1].reshape((total-1-trainSize, 1, 1))
            evalY = data[trainSize+1:total]
            model.fit(x=x, y=y, validation_data=(evalX, evalY), batch_size=1, epochs=1, shuffle=False)
            model.reset_states()

    saveAI(model)

    plotGeneratedLSTM(model, 0.06)
    plotGeneratedLSTM(model, 0.083)
    plotGeneratedLSTM(model, 0.163)
    plotGeneratedLSTM(model, 0.033)
    return


def render(y, predicted, a, count):
    plt.grid()
    plt.plot(y[0:count])
    plt.plot(predicted[0:count], 'go')
    plt.title("y=sin({}*x)".format(a))
    plt.savefig("plt-{}.png".format(a))
    plt.show()


def plotPredicted(model, a):
    model.reset_states()
    x, y, eX, eY = getSeries(a, 300)
    predicted = model.predict(x=x)
    render(y, predicted, a, 100)


def plotGeneratedLSTM(model, a):
    model.reset_states()
    data = getSineData(a, 300)
    x = data[0:100]

    model.predict(x=x.reshape((100, 1, 1)), batch_size=1)

    y = data[101:201]
    predicted = np.zeros((100,))
    gx = data[0]
    for i in range(100, 200):
        predicted[i-100] = model.predict(x=gx.reshape(1, 1, 1))
        gx = predicted[i-100]

    render(y, predicted, a, 100)


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-m", "--model", help="fc/cnn/lstm")

    args = parser.parse_args()

    if args.model == 'lstm':
        testLSTM()
    else:
        print('unknown model')
    return


if __name__ == '__main__':
    main()
