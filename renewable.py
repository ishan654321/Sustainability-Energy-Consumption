import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
wind_df=pd.read_csv('D:\Sustanability Project\wind_share_energy.csv')
wind_df.drop('Code',axis=1,inplace=True)
wind_df.rename(columns={'Entity':'Country'},inplace=True)
wind_df['Year']=wind_df['Year'].astype(int)

solar_df=pd.read_csv('D:\Sustanability Project\solar_share_energy.csv')
solar_df.drop('Code',axis=1,inplace=True)
solar_df['Year']=solar_df['Year'].astype(int)
solar_df.rename(columns={'Entity':'Country'},inplace=True)


hydro_df=pd.read_csv('D:\Sustanability Project\hydro_share_energy.csv')
hydro_df.drop('Code',axis=1,inplace=True)
hydro_df['Year']=hydro_df['Year'].astype(int)
hydro_df.rename(columns={'Entity':'Country'},inplace=True)
def RenewableEnergy():
    #Here is the wind only section:
    st.header('Wind Energy')
    st.write(wind_df.sample(10))
    
    wind_df_time_series = wind_df.groupby('Year')['Wind (% equivalent primary energy)'].mean().reset_index()
    fig = go.Figure(
        data=[go.Scatter(x=wind_df_time_series['Year'], y=wind_df_time_series['Wind (% equivalent primary energy)'], mode='lines+markers')],
        layout=go.Layout(
            xaxis=dict(range=[wind_df_time_series['Year'].min(), wind_df_time_series['Year'].max()], autorange=False),
            yaxis=dict(range=[wind_df_time_series['Wind (% equivalent primary energy)'].min(), wind_df_time_series['Wind (% equivalent primary energy)'].max()], autorange=False),
            title="Global Wind Energy Usage Over Years",
            ),
    )
    fig.update_xaxes(title_text='Year')

    fig.update_yaxes(title_text='Wind Energy Usage (% equivalent primary energy)')

    st.plotly_chart(fig)

    # Filter for year 2021 first
    wind_df_2021 = wind_df[wind_df['Year'] == 2021]

    # Then group by 'Country' (or 'Entity') and calculate mean
    wind_df_top_production = wind_df_2021.groupby('Country')['Wind (% equivalent primary energy)'].mean().reset_index()

    # Sort values in descending order and get top 10
    wind_df_top_production = wind_df_top_production.sort_values('Wind (% equivalent primary energy)', ascending=False).head(10)

    fig2 = go.Figure(
        data=[go.Bar(x=wind_df_top_production['Country'], y=wind_df_top_production['Wind (% equivalent primary energy)'])],
        layout=go.Layout(
            title="Top 10 Country by Wind Energy Usage (2021)",
            xaxis_title='Country',
            yaxis_title='Percentage Usage of Wind Energy from Total'
            ),
    )
    st.plotly_chart(fig2)

    continents = ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"]
    continent_wind_data = wind_df[wind_df['Country'].isin(continents)]
    # Then group by 'Country' (well here obiously continent but the column name is given country so... :(  )
    continent_wind_data = continent_wind_data.groupby('Country')['Wind (% equivalent primary energy)'].mean().reset_index()

    # Sort values in descending order and get top 10
    continent_wind_data = continent_wind_data.sort_values('Wind (% equivalent primary energy)', ascending=False)

    fig3 = go.Figure(
        data=[go.Bar(x=continent_wind_data['Country'], y=continent_wind_data['Wind (% equivalent primary energy)'])],
        layout=go.Layout(
            title="Continent Ranking by Wind Energy Usage (2021)",
            xaxis_title='Continent',
            yaxis_title='Percentage Usage of Wind Energy from Total'
            ),
    )
    st.plotly_chart(fig3)

    #Now Solar only section
    st.header('Solar Energy')
    st.write(solar_df.sample(10))
    
    solar_df_time_series = solar_df.groupby('Year')['Solar (% equivalent primary energy)'].mean().reset_index()
    fig4 = go.Figure(
        data=[go.Scatter(x=solar_df_time_series['Year'], y=solar_df_time_series['Solar (% equivalent primary energy)'], mode='lines+markers')],
        layout=go.Layout(
            xaxis=dict(range=[solar_df_time_series['Year'].min(), solar_df_time_series['Year'].max()], autorange=False),
            yaxis=dict(range=[solar_df_time_series['Solar (% equivalent primary energy)'].min(), solar_df_time_series['Solar (% equivalent primary energy)'].max()], autorange=False),
            title="Global Solar Energy Usage Over Years",
            ),
    )
    fig.update_xaxes(title_text='Year')

    fig.update_yaxes(title_text='Solar Energy Usage (% equivalent primary energy)')

    st.plotly_chart(fig4)

    # Filter for year 2021 first
    solar_df_2021 = solar_df[solar_df['Year'] == 2021]

    # Then group by 'Country' (or 'Entity') and calculate mean
    solar_df_top_production = solar_df_2021.groupby('Country')['Solar (% equivalent primary energy)'].mean().reset_index()

    # Sort values in descending order and get top 10
    solar_df_top_production = solar_df_top_production.sort_values('Solar (% equivalent primary energy)', ascending=False).head(10)

    fig5 = go.Figure(
        data=[go.Bar(x=solar_df_top_production['Country'], y=solar_df_top_production['Solar (% equivalent primary energy)'])],
        layout=go.Layout(
            title="Top 10 Country by Solar Energy Usage (2021)",
            xaxis_title='Country',
            yaxis_title='Percentage Usage of Solar Energy from Total'
            ),
    )
    st.plotly_chart(fig5)

    continent_solar_data = solar_df[solar_df['Country'].isin(continents)]
    # Then group by 'Country' (well here obiously continent but the column name is given country so... :(  )
    continent_solar_data = continent_solar_data.groupby('Country')['Solar (% equivalent primary energy)'].mean().reset_index()

    # Sort values in descending order and get top 10
    continent_solar_data = continent_solar_data.sort_values('Solar (% equivalent primary energy)', ascending=False)

    fig6 = go.Figure(
        data=[go.Bar(x=continent_solar_data['Country'], y=continent_solar_data['Solar (% equivalent primary energy)'])],
        layout=go.Layout(
            title="Continent Ranking by Solar Energy Usage (2021)",
            xaxis_title='Continent',
            yaxis_title='Percentage Usage of Solar Energy from Total'
            ),
    )
    st.plotly_chart(fig6)

#=========================================================================================================================
    #Now Hydro only section
    st.header('Hydro Energy')
    st.write(hydro_df.sample(10))
    
    hydro_df_time_series = hydro_df.groupby('Year')['Hydro (% equivalent primary energy)'].mean().reset_index()
    fig7 = go.Figure(
        data=[go.Scatter(x=hydro_df_time_series['Year'], y=hydro_df_time_series['Hydro (% equivalent primary energy)'], mode='lines+markers')],
        layout=go.Layout(
            xaxis=dict(range=[hydro_df_time_series['Year'].min(), hydro_df_time_series['Year'].max()], autorange=False),
            yaxis=dict(range=[hydro_df_time_series['Hydro (% equivalent primary energy)'].min(), hydro_df_time_series['Hydro (% equivalent primary energy)'].max()], autorange=False),
            title="Global Hydro Energy Usage Over Years",
            ),
    )
    fig.update_xaxes(title_text='Year')

    fig.update_yaxes(title_text='Hydro Energy Usage (% equivalent primary energy)')

    st.plotly_chart(fig7)

    # Filter for year 2021 first
    hydro_df_2021 = hydro_df[hydro_df['Year'] == 2021]

    # Then group by 'Country' (or 'Entity') and calculate mean
    hydro_df_top_production = hydro_df_2021.groupby('Country')['Hydro (% equivalent primary energy)'].mean().reset_index()

    # Sort values in descending order and get top 10
    hydro_df_top_production = hydro_df_top_production.sort_values('Hydro (% equivalent primary energy)', ascending=False).head(10)

    fig8 = go.Figure(
        data=[go.Bar(x=hydro_df_top_production['Country'], y=hydro_df_top_production['Hydro (% equivalent primary energy)'])],
        layout=go.Layout(
            title="Top 10 Country by Hydro Energy Usage (2021)",
            xaxis_title='Country',
            yaxis_title='Percentage Usage of Hydro Energy from Total'
            ),
    )
    st.plotly_chart(fig8)
    continent_hydro_data = hydro_df[hydro_df['Country'].isin(continents)]
    # Then group by 'Country' (well here obiously continent but the column name is given country so... :(  )
    continent_hydro_data = continent_hydro_data.groupby('Country')['Hydro (% equivalent primary energy)'].mean().reset_index()

    # Sort values in descending order and get top 10
    continent_hydro_data = continent_hydro_data.sort_values('Hydro (% equivalent primary energy)', ascending=False)

    fig9 = go.Figure(
        data=[go.Bar(x=continent_hydro_data['Country'], y=continent_hydro_data['Hydro (% equivalent primary energy)'])],
        layout=go.Layout(
            title="Continent Ranking by Hydro Energy Usage (2021)",
            xaxis_title='Continent',
            yaxis_title='Percentage Usage of Hydro Energy from Total'
            ),
    )
    st.plotly_chart(fig9)