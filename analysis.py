import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
def analysis():
    df = pd.read_csv('.\Renewable Energy Dataset\DEOK_hourly.csv', index_col='Datetime')

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
    # Calculate the monthly average consumption
    monthly_avg_consumption = df.groupby(['year', 'month'])['DEOK_MW'].mean().reset_index()
    monthly_avg_consumption2 = df.groupby(['month'])['DEOK_MW'].mean().reset_index()

    # Display the monthly average consumption
    st.subheader('Monthly Average Energy Consumption Over the Years')
    st.write(monthly_avg_consumption2)
    st.write('It means that July has the highest power consumption while April has the lowest.')

    # Create an empty figure
    fig = go.Figure()
    # Plot the monthly average consumption
    for year in monthly_avg_consumption['year'].unique():
        year_data = monthly_avg_consumption[monthly_avg_consumption['year'] == year]
        fig.add_trace(go.Scatter(x=year_data['month'], y=year_data['DEOK_MW'],mode='lines', name=str(year)))
    # Update the layout
    fig.update_layout(
        title='Monthly Average Energy Consumption Over the Years',
        xaxis_title='Month',
        yaxis_title='Average Energy Consumption (MW)',
        legend_title='Year'
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    #-------------------------------------
    df_2014=df[df['year']==2014]
    daily_avg_consumption = df_2014.groupby(['year', 'month','dayofmonth'])['DEOK_MW'].mean().reset_index()
    daily_avg_consumption2 = df_2014.groupby(['dayofmonth'])['DEOK_MW'].mean().reset_index()


    # Display the monthly average consumption
    st.subheader('Daily Average Energy Consumption in 2014')
    st.write(daily_avg_consumption2)
    st.write('It means that date 15th has the highest power consumption while 27th has the lowest.')


    # Plot the monthly average consumption
    fig2=go.Figure()
    for month in daily_avg_consumption['month'].unique():
        month_data = daily_avg_consumption[daily_avg_consumption['month'] == month]
        fig2.add_trace(go.Scatter(x=month_data['dayofmonth'], y=month_data['DEOK_MW'], mode='lines', name=str(month)))

    fig2.update_layout(
        title='Daily Average Energy Consumption Over the months',
        xaxis_title='Day of Month',
        yaxis_title='Average Energy Consumption (MW)',
        legend_title='Month'
    )
    
    st.plotly_chart(fig2)
