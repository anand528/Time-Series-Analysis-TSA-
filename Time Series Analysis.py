## Importing libraries
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
## loading the data
data=pd.read_csv('AirPassengers.csv')
data
# Stats Analysis of data
data.describe()  ##used to view some basic statistical details like percentile, mean, std etc.
# EDA
import matplotlib.pyplot as plt
plt.figure(figsize=(25,15),facecolor='white')#canvas  size
plt.plot(data)#line plot
plt.tight_layout()
## from plot we can see the series given is not stationary
## Plotting the autocorrelation function
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(data)
# ADfuller Test to check stationarity
from statsmodels.tsa.stattools import adfuller
dftest = adfuller(data.Passengers, autolag = 'AIC')
print("1. ADF : ",dftest[0])
print("2. P-Value : ", dftest[1])
print("3. Num Of Lags : ", dftest[2])
print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
print("5. Critical Values :")
for key, val in dftest[4].items():
    print("\t",key, ": ", val)
## making it stationary by taking difference of 1
data1=data.diff(periods=1) 
#pandas diff will subtract 1 cell value from another cell value within the same index.
data1=data1.iloc[1:] #null value discarded
data1
## Creating training and test sets
train=data2[:100]     #from 0th row to 99th row - traning data
test=data2[100:]      #from 100th row to end - testing data
## Applying autoregressive model
#from statsmodels.tsa.ar_model import AR
##from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.ar_model import AutoReg
import warnings
warnings.filterwarnings('ignore')
#ar_select_order : gives the best lags ordered as an array
# to select the optimal values for lags
from statsmodels.tsa.ar_model import ar_select_order
mod = ar_select_order(data2,maxlag=15,glob=True)
mod.ar_lags
## model creation
ar_model=AutoReg(train,lags=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) ## object creation with lags specified
ar_model_fit=ar_model.fit() #training the model
##making prediction
prediction=ar_model_fit.predict(start=100,end=142)
# ARIMA
## importing the library
from statsmodels.tsa.arima.model import ARIMA
model_arima = ARIMA(train, order=(1,1,0))#order
model_arima_fit = model_arima.fit()#training
## evaluate the model
print(model_arima_fit.aic)
predictions = model_arima_fit.forecast(steps=9)
predictions
## Geeting the optimal values of p,q an d
import itertools
p =d= q=range(0,10)#values of p,d,q range from 0 to 4
pdq = list(itertools.product(p,d,q))
# is used to find the cartesian product from the given iterator, output is lexicographic ordered.
pdq          # number of combinaton of pdq
model_arima_fit.predict(steps=50)
errors=[]
for i in tqdm(pdq):
  model=ARIMA(train,order=i)
  model_fit=model.fit()
  pred=model_fit.forecast(steps=42)
  error=np.mean(pred-(test.values.reshape(-1)))
  errors.append(error)
np.argmin(errors)
pdq[20]
model_fit.aic
forecast25 = model_arima_fit.forecast(steps=25)
test1 = test[0:25].values.flatten()
test1
# Comparision of actual vs predicted for 25 values
plt.plot(test[:25])
plt.plot(forecast25,color='green') #line plot for prediction
# Accuracy metrics
import numpy as np
def forecast_accuracy(forecast, actual):
    mse = np.mean((forecast - actual)**2)        # MSE
    mae = np.mean(np.abs(forecast - actual))    # MAE
    rmse = np.mean((forecast - actual)**2)**.5  # RMSE
    return({'mse':mse, 'mae': mae, 'rmse':rmse})
forecast_accuracy(forecast25, test1)
