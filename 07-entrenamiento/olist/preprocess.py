import pandas as pd
import numpy as np

###ORDERS

def transformar_columnas_datetime(df, columns):
    for column in columns:
        df[column] = pd.to_datetime(df[column])
    return df


def tiempo_de_espera(df):
    one_day_delta = np.timedelta64(24, 'h')
    df['tiempo_de_espera'] = np.where(df['order_status'] == 'delivered', (df['order_delivered_customer_date'] - df['order_purchase_timestamp'])/ one_day_delta, np.nan)
    return df


def tiempo_de_espera_previsto(df):
    one_day_delta = np.timedelta64(24, 'h')
    df['tiempo_de_espera_previsto'] = np.where(df['order_status'] == 'delivered', (df['order_estimated_delivery_date'] - df['order_purchase_timestamp']) / one_day_delta, np.nan)
    return df


def real_vs_esperado(df):
    df['real_vs_esperado'] = df['tiempo_de_espera'] - df['tiempo_de_espera_previsto']
    return df

###REVIEWS

def puntaje_de_compra(df):
    df['es_cinco_estrellas'] = df['review_score'] == 5
    df['es_una_estrella'] = df['review_score'] == 1

    #Reemplazo los true y false por nros.
    df['es_cinco_estrellas'] = df['es_cinco_estrellas'].astype(int)
    df['es_una_estrella'] = df['es_una_estrella'].astype(int)
    return df

###Numero de productos por orden

def calcular_numero_productos(dict_of_dfs):
    df = dict_of_dfs['order_items']
    df = df.groupby('order_id').size().reset_index(name='numero_de_productos')
    return df

###vendedores unicos por orden

def vendedores_unicos(dict_of_dfs):
    df = dict_of_dfs['order_items']
    df = df.groupby('order_id')['seller_id'].nunique().reset_index(name='vendedores_unicos')
    return df

###calcular precio y transporte por orden

def calcular_precio_y_transporte(dict_of_dfs):
    df = dict_of_dfs['order_items']
    df = df.groupby('order_id')['price', 'freight_value'].sum().reset_index()
    return df

###calcular distancia entre vendedor y comprador

def calcular_distancia_vendedor_comprador(data):
    orders = data['orders']
    order_items = data['order_items']
    sellers = data['sellers']
    customers = data['customers']

    geo = data['geolocation']
    geo = geo.groupby('geolocation_zip_code_prefix').first().reset_index()



#select the columns i want to keep in df

