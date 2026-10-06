# Time-Series-Analysis
Time Series Analysis (TSA)  using AR (Auto Regression ) and ARIMA Algorithms for Predictions future values. 

---

# 📈 Time Series Analysis with AR & ARIMA
## 🔎 Overview
This project demonstrates time series forecasting using Autoregressive (AR) and Autoregressive Integrated Moving Average (ARIMA) models.
We apply these algorithms to real-world datasets (e.g., airline passenger counts) to explore stationarity, autocorrelation, model selection, and forecast accuracy.

---

# 🛠️ Features
- Exploratory Data Analysis (EDA) of time series data
- Stationarity checks using ADF (Augmented Dickey-Fuller) test
- Autocorrelation and Partial Autocorrelation plots (ACF & PACF)
- AR and ARIMA model fitting with different (p,d,q) parameters
- Error handling for invalid parameter combinations
- Forecast evaluation using MAE, MSE, RMSE
- Comparison of models using AIC (Akaike Information Criterion)

---

# 📂 Project Structure
- ├── Time_Series.ipynb   Jupyter Notebook with full analysis
- ├── README.md           Project documentation
- ├── requirements.txt    Python dependencies
- └── data/               Dataset(s) used

---

# ⚙️ Installation
- Clone the repository and install dependencies:
- git clone https://[github.com/anand528/time-series-arima.git](https://github.com/anand528/Time-Series-Analysis-TSA-/tree/main)
- cd time-series-arima
- pip install -r requirements.txt

---

# 📊 Usage
Open the notebook:
* jupyter notebook Time_Series.ipynb
* 1.inside the notebook, you’ll find:
* 2.ADF Test → Check stationarity
* 3.ACF & PACF plots → Identify AR/MA orders
* 4.ARIMA fitting loop → Try multiple (p,d,q) combinations
* 5.Error metrics → Evaluate forecast accuracy
* 6.AIC comparison → Select the best model

---

# 📈 Example Output
- ADF Test Results: p-value < 0.05 → Stationary after differencing
- ACF/PACF Plots: Guide AR and MA order selection
- Forecast Accuracy: RMSE, MAE, MSE values for test set
- Best ARIMA Order: Selected based on lowest AIC and error score

---

# 🚀 Future Work
- Implement SARIMA for seasonal datasets
- Add auto_arima for automated parameter selection
- Extend to LSTM/GRU deep learning models for sequence forecasting

---

# 📜 License
This project is licensed under the MIT License.
