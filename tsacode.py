import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime

def forcasting():
    st.title('Hourly Energy Consumption Forecasting')
    df = pd.read_csv('D:\Sustanability Project\DEOK_hourly.csv\DEOK_hourly.csv', index_col='Datetime')

    df.index = pd.to_datetime(df.index)
    df['date'] = df.index
    df['hour'] = df['date'].dt.hour
    df['dayofweek'] = df['date'].dt.dayofweek
    df['quarter'] = df['date'].dt.quarter
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['date'].dt.day
    df['weekofyear'] = df['date'].dt.isocalendar().week.astype(int)

    st.write("Sample of the data:")
    st.dataframe(df.head())
   
    st.subheader('Energy Consumption Over Time')
    fig,ax=plt.subplots(figsize=(12, 6))
    ax.plot(df.index.to_numpy(), df['DEOK_MW'].to_numpy(), label='Energy Consumption')
    # ax.plot(df.index, df['DEOK_MW'], label='Energy Consumption')
    ax.set_xlabel('Date')
    ax.set_ylabel('Energy Consumption')
    ax.set_title('Hourly Energy Consumption')
    ax.legend()
    st.pyplot(fig)

    def create_lag_features(df, lags):
        for lag in lags:
            df[f'lag_{lag}'] = df['DEOK_MW'].shift(lag)
        df = df.dropna()
        return df

    # Define the lag features to create (e.g., 1, 24, 168 for 1 hour, 1 day, 1 week)
    lags = [1, 24, 168]
    df = create_lag_features(df, lags)

    X = df.drop(columns=['DEOK_MW', 'date'])
    y = df['DEOK_MW']

    # Split the data into train and test sets
    split_date = '2017-01-01'  # Use data before 2017 for training and after for testing
    X_train, X_test = X[X.index < split_date], X[X.index >= split_date]
    y_train, y_test = y[y.index < split_date], y[y.index >= split_date]

    # Scale the data
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train the XGBoost model
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=950, learning_rate=0.05, max_depth=5)
    model.fit(X_train_scaled, y_train)

    # Make predictions
    y_pred = model.predict(X_test_scaled)

    # Plot the predictions vs actual values
    st.subheader('Actual vs Predicted Energy Consumption')
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(y_test.index.to_numpy(), y_test.to_numpy(), label='Actual')
    ax.plot(y_test.index.to_numpy(), y_pred, label='Predicted', alpha=0.7)

    # ax.plot(y_test.index, y_test, label='Actual')
    # ax.plot(y_test.index, y_pred, label='Predicted', alpha=0.7)
    ax.set_xlabel('Date')
    ax.set_ylabel('Energy Consumption')
    ax.set_title('Actual vs Predicted Energy Consumption')
    ax.legend()
    st.pyplot(fig)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    st.write(f'Mean Squared Error: {mse}')
    st.write(f'Mean Absolute Error: {mae}')

    # Display df.describe() summary
    st.subheader("Dataframe Description:")
    st.write(df.describe())