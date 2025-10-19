import datetime

import pandas as pd
from prophet import Prophet

raw_data = pd.read_csv("data/output.csv")

tidy_data = raw_data.rename(columns = {'date':'ds', 'price':'y'})[['ds', 'y']]

model = Prophet()

model.fit(tidy_data)

future_period = model.make_future_dataframe(periods=12 * 7)

forecast = model.predict(future_period)

print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())


fig1 = model.plot(forecast)

fig1.savefig("data/forecast.png")