import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet

dates = pd.date_range(start="2023-01-01", periods = 365)

temperature = (
    30
    + np.sin(np.arange(365) * 0.05) * 5 # seasonality (waves)
    + np.arange(365) * 0.02             # slight warming trend
    + np.random.normal(0, 0.5, 365)     # noise
)


df = pd.DataFrame(
    {
        "ds": dates,
        "y": temperature
    }
)

print(df.head(10))

#visualize part

plt.figure(figsize=(10,5))
plt.plot(df["ds"],df["y"])
plt.title("Daily Temperature (Weather time series)")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.savefig("plot.png")

#training model

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)

model.fit(df)

#We predict next 60 days:

future = model.make_future_dataframe(periods = 60)

forecast = model.predict(future)
print(forecast[["ds","yhat","yhat_lower","yhat_upper"]])

fig = model.plot(forecast)
plt.title("Weather Forecast")
plt.savefig('new.png')