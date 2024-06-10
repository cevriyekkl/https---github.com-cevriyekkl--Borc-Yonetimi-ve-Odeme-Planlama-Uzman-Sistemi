#Borç ödeme stratejileri geliştirme.

from keras.models import Sequential
from keras.layers import Dense
import numpy as np

def determine_payment_strategy(features, strategies, new_data):
    model = Sequential()
    model.add(Dense(12, input_dim=3, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    X = np.array(features)
    y = np.array(strategies)
    model.fit(X, y, epochs=150, batch_size=2, verbose=0)
    strategy_score = model.predict(np.array([new_data]))
    return strategy_score
