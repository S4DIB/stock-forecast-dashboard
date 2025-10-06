# 📈 Stock Forecast Dashboard (Prophet + ARIMA)

A full-stack interactive dashboard for **stock price forecasting** built with **Streamlit**, integrating **Meta’s Prophet** and **ARIMA** models for accurate, data-driven financial predictions.  
The app provides visual analytics, automatic trend detection, and customizable time-series forecasting in an intuitive web interface.

---

## 🚀 Features

- 🔮 **Dual-Model Forecasting:** Compare predictions from Prophet and ARIMA models.  
- 🧠 **Auto Data Preprocessing:** Cleans and prepares stock data dynamically from Yahoo Finance.  
- 📊 **Interactive Visuals:** Line charts, trends, and forecast intervals rendered via Streamlit.  
- ⚙️ **Model Evaluation:** Includes RMSE and MAPE metrics for transparent performance comparison.  
- 📁 **Cached Data Layer:** Reduces repeated API calls for faster interactions.  
- 🔁 **Robust UI:** Handles API failures and missing data gracefully with custom alerts.  
- 💡 **User Note:** Sometimes Hugging Face may not load properly—simply click the **Submit** button 2–3 times to refresh the session.

---

## 🧩 Tech Stack

| Layer | Technology |
|:------|:------------|
| **Frontend** | Streamlit |
| **Data Source** | Yahoo Finance API |
| **Forecasting Models** | Prophet, ARIMA (statsmodels) |
| **Visualization** | Matplotlib, Plotly |
| **Deployment** | Hugging Face Spaces (Cloud) |
| **Version Control** | Git & GitHub |

---

## 📂 Project Structure

📦 stock-forecast-dashboard
│
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── README.md # Documentation
└── models/ # Saved model files

---