import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


df = pd.read_csv('datos_ejs/olist_orders_dataset.csv')

#convert purchase and aprroved columns to datetie

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_approved_at'] = pd.to_datetime(df['order_approved_at'])

# get time difference between purchase and approved

df['time_diff'] = df['order_approved_at'] - df['order_purchase_timestamp']

# remove the outliers of time diff
