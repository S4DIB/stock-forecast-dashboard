import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gradio as gr
import os

# Company list
company_names = ["APPLE", "AMAZON", "GOOGLE"]

# Load Prophet and ARIMA models
prophet_models = {}
arima_models = {}

# Folder containing model files
model_dir = "models"

for company in company_names:
    # Prophet
    prophet_path = os.path.join(model_dir, f"prophet_{company}.pkl")
    if os.path.exists(prophet_path):
        with open(prophet_path, "rb") as f:
            prophet_models[company] = pickle.load(f)
        print(f"✅ Loaded Prophet model for {company}")
    else:
        prophet_models[company] = None
        print(f"⚠️ Prophet model missing: {prophet_path}")

    # ARIMA
    arima_path = os.path.join(model_dir, f"arima_{company}.pkl")
    if os.path.exists(arima_path):
        with open(arima_path, "rb") as f:
            arima_models[company] = pickle.load(f)
        print(f"✅ Loaded ARIMA model for {company}")
    else:
        arima_models[company] = None
        print(f"⚠️ ARIMA model missing: {arima_path}")


def forecast(company, months):
    """
    Generate future forecasts using Prophet and ARIMA models.
    """
    months = int(months)
    prophet_model = prophet_models.get(company)
    arima_model = arima_models.get(company)

    if prophet_model is None and arima_model is None:
        return pd.DataFrame({"Message": [f"No trained models found for {company}"]}), None

    # --- Prophet Forecast ---
    prophet_df = None
    if prophet_model is not None:
        future = prophet_model.make_future_dataframe(periods=months, freq='MS')
        forecast = prophet_model.predict(future)
        prophet_df = forecast[['ds', 'yhat']].tail(months)
        prophet_df = prophet_df.rename(columns={'ds': 'Date', 'yhat': 'Prophet_Pred'})

    # --- ARIMA Forecast ---
    arima_df = None
    if arima_model is not None:
        try:
            y_pred = arima_model.forecast(steps=months)
        except:
            try:
                y_pred = arima_model.predict(n_periods=months)
            except:
                y_pred = [np.nan] * months

        # Use Prophet’s last date if available; otherwise use dummy dates
        if prophet_model is not None:
            last_date = pd.to_datetime(prophet_model.history['ds'].iloc[-1])
        else:
            last_date = pd.to_datetime("2023-01-01")

        future_dates = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=months, freq='MS')
        arima_df = pd.DataFrame({'Date': future_dates, 'ARIMA_Pred': y_pred})

    # --- Merge results ---
    if prophet_df is not None and arima_df is not None:
        merged = pd.merge(prophet_df, arima_df, on='Date', how='outer')
    elif prophet_df is not None:
        merged = prophet_df
    else:
        merged = arima_df

    # --- Plot ---
    fig, ax = plt.subplots(figsize=(8, 4))
    if prophet_df is not None:
        ax.plot(prophet_df['Date'], prophet_df['Prophet_Pred'], label="Prophet Forecast", linestyle='--')

    if arima_df is not None:
        ax.plot(arima_df['Date'], arima_df['ARIMA_Pred'], label="ARIMA Forecast", linestyle=':')

    ax.set_title(f"{company} Forecast (Next {months} Months)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    plt.tight_layout()

    return merged, fig


# --- Gradio Interface ---
interface = gr.Interface(
    fn=forecast,
    inputs=[
        gr.Dropdown(company_names, label="Select Company"),
        gr.Number(value=12, label="Forecast Months")
    ],
    outputs=[
        gr.Dataframe(label="Forecast Table"),
        gr.Plot(label="Forecast Plot")
    ],
    title="Stock Forecast Dashboard (Prophet + ARIMA)*Note:* Sometimes Hugging Face Spaces may take a moment to load results. If nothing appears, click the **Submit** button 2–3 times to refresh the output.",
    description="Forecasts future stock prices using Prophet and ARIMA models trained for APPLE, AMAZON, and GOOGLE."
)

if __name__ == "__main__":
    interface.launch()
