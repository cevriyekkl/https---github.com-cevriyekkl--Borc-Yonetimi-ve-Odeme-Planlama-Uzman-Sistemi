#Borç takibi işlevselliği.

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def track_debt(debts):
    data = pd.DataFrame(debts)
    data.set_index('date', inplace=True)
    model = ARIMA(data['debt_amount'], order=(5, 1, 0))
    model_fit = model.fit(disp=0)
    forecast = model_fit.forecast(steps=3)[0]
    return forecast