# 📈 Stock Forecast Dashboard (Prophet + ARIMA)

A full-stack interactive dashboard for **stock price forecasting** built with **Gradio**, integrating **Meta’s Prophet** and **ARIMA** models for accurate, data-driven financial predictions.  
The app provides visual analytics, automatic trend detection, and customizable time-series forecasting in an intuitive web interface.

---

## 🚀 Features

- 🔮 **Dual-Model Forecasting:** Compare predictions from Prophet and ARIMA models.  
- 🧠 **Auto Data Preprocessing:** Cleans and prepares stock data dynamically from Yahoo Finance.  
- 📊 **Interactive Visuals:** Line charts, trends, and forecast intervals rendered via Gradio.  
- ⚙️ **Model Evaluation:** Includes RMSE and MAPE metrics for transparent performance comparison.  
- 📁 **Cached Data Layer:** Reduces repeated API calls for faster interactions.  
- 🔁 **Robust UI:** Handles API failures and missing data gracefully with custom alerts.  
- 💡 **User Note:** Sometimes Hugging Face may not load properly—simply click the **Submit** button 2–3 times to refresh the session.

---

## 🧩 Tech Stack

| Layer | Technology |
|:------|:------------|
| **Frontend** | Gradio |
| **Data Source** | Yahoo Finance API |
| **Forecasting Models** | Prophet, ARIMA (statsmodels) |
| **Visualization** | Matplotlib, Plotly |
| **Deployment** | Hugging Face Spaces (Cloud) |
| **Version Control** | Git & GitHub |

---

## 📂 Project Structure
```
📦 stock-forecast-dashboard
│
├── app.py # Main Gradio app
├── requirements.txt # Dependencies
├── README.md # Documentation
└── models/ # Saved model files
```
---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/stock-forecast-dashboard.git
cd stock-forecast-dashboard
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Application
python app.py
4️⃣ Access in Browser
Navigate to http://localhost:8501

📊 Usage Guide

Enter a valid stock ticker (e.g., AAPL, GOOGL, TSLA).

Choose a forecast period (days, months, or years).

Click Submit to view forecasts and metrics.

Toggle between Prophet and ARIMA results to compare trends.

Re-click submit (2–3 times) if data doesn’t load immediately due to Hugging Face session delay.

🧠 Example Forecast Visualization
Historical Data  ────────────────▶
Prophet Forecast ────────────────▶
ARIMA Forecast   ────────────────▶

Both models generate their own confidence intervals and trend projections, allowing for model comparison and hybrid insights.

📈 Future Enhancements

 Add LSTM for deep learning forecasting.

 Integrate real-time financial news sentiment to enhance prediction signals.

 Deploy via AWS Lambda or Gradio Cloud for auto-scaling.

 Enable multi-stock portfolio forecasting and analytics comparison.

🧾 License

This project is released under the MIT License — free for personal and commercial use with attribution.

🤝 Contributions

Pull requests are welcome!
For significant changes, please open an issue first to discuss the proposal.

📬 Contact

Developer: Sadib

Email: shahsadib25@gmail.com

⚡ "Forecasting the future is never certain, but intelligent modeling brings us closer to clarity."
— Stock Forecast Dashboard Team
