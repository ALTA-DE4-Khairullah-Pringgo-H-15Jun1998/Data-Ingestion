import pandas as pd

# Membaca file CSV besar
file_path = './dataset/yellow_tripdata_2020-07.csv'
df = pd.read_csv(file_path)

print("DataFrame created from CSV:")
print(df.head())

# Mengganti nama kolom dengan snake_case
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

print("DataFrame dengan nama kolom snake_case:")
print(df.head())

# Verifikasi nama kolom
print("Nama kolom setelah diubah:")
print(df.columns)

# Memilih kolom yang diperlukan
selected_columns = [
    'vendorid', 'passenger_count', 'trip_distance', 'payment_type', 
    'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 
    'improvement_surcharge', 'total_amount', 'congestion_surcharge'
]
df_selected = df[selected_columns]

# Memilih 10 baris teratas dengan passenger_count tertinggi
top_10_df = df_selected.nlargest(10, 'passenger_count')

print("10 baris teratas dengan passenger_count tertinggi:")
print(top_10_df)

# Mengatasi nilai NaN sebelum mengubah tipe data
df_selected.loc[:, 'vendorid'] = pd.to_numeric(df_selected['vendorid'], errors='coerce').fillna(0).astype(str)
df_selected.loc[:, 'passenger_count'] = pd.to_numeric(df_selected['passenger_count'], errors='coerce').fillna(0).astype(int)
df_selected.loc[:, 'trip_distance'] = pd.to_numeric(df_selected['trip_distance'], errors='coerce').fillna(0.0).astype(float)
df_selected.loc[:, 'payment_type'] = df_selected['payment_type'].astype(str)
df_selected.loc[:, 'fare_amount'] = pd.to_numeric(df_selected['fare_amount'], errors='coerce').fillna(0.0).astype(float)
df_selected.loc[:, 'extra'] = pd.to_numeric(df_selected['extra'], errors='coerce').fillna(0.0).astype(float)
df_selected.loc[:, 'mta_tax'] = pd.to_numeric(df_selected['mta_tax'], errors='coerce').fillna(0.0).astype(float)
df_selected.loc[:, 'tip_amount'] = pd.to_numeric(df_selected['tip_amount'], errors='coerce').fillna(0.0).astype(float)
df_selected.loc[:, 'tolls_amount'] = pd.to_numeric(df_selected['tolls_amount'], errors='coerce').fillna(0.0).astype(float)
df_selected.loc[:, 'improvement_surcharge'] = pd.to_numeric(df_selected['improvement_surcharge'], errors='coerce').fillna(0.0).astype(float)
df_selected.loc[:, 'total_amount'] = pd.to_numeric(df_selected['total_amount'], errors='coerce').fillna(0.0).astype(float)
df_selected.loc[:, 'congestion_surcharge'] = pd.to_numeric(df_selected['congestion_surcharge'], errors='coerce').fillna(0.0).astype(float)

print("DataFrame dengan tipe data yang telah diubah:")
print(df_selected.dtypes)
