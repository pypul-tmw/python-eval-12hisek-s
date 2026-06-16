import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

# 1. CREATE DATA


dates = pd.date_range(start="2023-01-01", periods=200)

# wave + trend + small noise (more realistic)
values = (
    np.sin(np.arange(200) * 0.1) * 10 +
    np.arange(200) * 0.2 +
    np.random.normal(0, 1, 200)
)

df = pd.DataFrame({
    "ds": dates,
    "y": values
})

print(df.head())


# 2. VISUALIZE DATA
plt.figure(figsize=(10, 5))
plt.plot(df["ds"], df["y"])
plt.title("Time Series Data")
plt.show()


# 3. TRAIN PROPHET MODEL
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)

model.fit(df)


# 4. FUTURE PREDICTION
future = model.make_future_dataframe(periods=180)
forecast = model.predict(future)

print("\nForecast preview:")
print(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail())


# 5. PLOT FORECAST
fig1 = model.plot(forecast)
plt.title("Forecast with Prophet")
plt.show()


# 6. COMPONENTS
fig2 = model.plot_components(forecast)
plt.show()

# 7. CROSS VALIDATION (FIXED LOGIC)


df_cv = cross_validation(
    model,
    initial="120 days",   # first training window
    period="30 days",     # shift every 30 days
    horizon="30 days"     # predict 30 days ahead
)

df_metrics = performance_metrics(df_cv)

print("\nCross-validation metrics:")
print(df_metrics.head())


# 8. ERROR METRICS


mae = mean_absolute_error(df_cv["y"], df_cv["yhat"])
mse = mean_squared_error(df_cv["y"], df_cv["yhat"])
rmse = np.sqrt(mse)

print("\nFINAL MODEL PERFORMANCE:")
print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")