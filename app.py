import pandas as pd
import plotly.express as px
import streamlit as st
        
vehicles = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Analisis de un dataframe sobre coches')
if st.checkbox('Construir histograma para visualizar la distribución de precios'):
    fig = px.histogram(vehicles, x='price', nbins=50, title='Distribución de Precios')
    st.plotly_chart(fig) # Para actualizar correctamente cuando se marque la casilla


if st.checkbox("Construir un gráfico de barras de la cantidad de vehículos por año de modelo"):
    model_year_counts = vehicles['model_year'].value_counts().reset_index()
    fig = px.bar(model_year_counts, x=model_year_counts.columns[0], y=model_year_counts.columns[1], 
                labels={model_year_counts.columns[0]: 'Año del Modelo', 
                        model_year_counts.columns[1]: 'Cantidad'},
                title='Cantidad de Vehículos por Año de Modelo')
    st.plotly_chart(fig)

if st.checkbox("Construir un diagrama de caja sobre el precio vs condición del vehículo"):
    fig = px.box(vehicles, x='condition', y='price', title='Precio vs Condición del Vehículo')
    st.plotly_chart(fig)

if st.checkbox("Construir un gráfico de dispersión sobre la relación entre odómetro y precio"):
    fig = px.scatter(vehicles, x='odometer', y='price', 
                 title='Relación entre Odómetro y Precio', 
                 labels={'odometer': 'Kilometraje', 'price': 'Precio'})
    st.plotly_chart(fig)

    
if st.checkbox("Crear un diagrama de barras sobre la distribución de tipos de combustible"):
    fuel_counts = vehicles['fuel'].value_counts().reset_index()

    fig = px.bar(fuel_counts, x=fuel_counts.columns[0], y=fuel_counts.columns[1], 
                labels={fuel_counts.columns[0]: 'Tipo de Combustible', 
                        fuel_counts.columns[1]: 'Cantidad'},
                title='Distribución de Tipos de Combustible')

    st.plotly_chart(fig)