import pandas as pd
import glob
import os

#Merge csv files in ventas comercial

os.chdir(r"UCEMA_POO\03-pandas\analysis\data\ventas_comercial")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
















