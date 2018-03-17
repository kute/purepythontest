#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: test.py
@ __mtime__: 2017/7/27 20:14

"""
import keras
from keras.models import Sequential, Model, model_from_json, model_from_config, model_from_yaml
from keras.layers import Dense, Activation
import numpy as np


def main():
    model = Sequential()
    model.add(Dense(32, activation='relu', input_dim=100))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

    model.summary()

    # get config obj
    config = model.get_config()

    # construct model obj with exists config
    # model = Model.from_config(config)
    model = model_from_config(config)
    # model = model_from_json(model.to_json)

    # or construct Sequential model obj with exists config
    model = Sequential.from_config(config)

    dense_1 = model.get_layer(name='dense_1')
    # dense_1 = model.get_layer(index=1)



    # data = np.random.random(size=(1000, 100))
    #
    # labels = np.random.randint(2, size=(1000, 1))
    #
    # model.fit(data, labels, epochs=10, batch_size=32)


if __name__ == "__main__":
    main()
