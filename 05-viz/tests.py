import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data_nps.csv')

df['detected_null'] = df['TAGS'].where(df['TAGS'].notnull(), 'No tags')